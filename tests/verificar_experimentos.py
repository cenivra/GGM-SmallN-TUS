"""Verificación científica y de integridad de los experimentos reproducibles publicados.

Comprueba:
1. Existencia e integridad de las tablas de resultados de EXP-018, EXP-019, EXP-020 y EXP-021.
2. Emparejamiento perfecto (mismas condiciones, réplicas y semillas) entre variantes MCMC de EXP-018.
3. Inmunidad bayesiana al colapso a red vacía (tasa de red vacía == 0.0%).
4. Invarianza matemática demostrada en EXP-019 entre los 4 umbrales post-hoc (u=0.08, 0.05, 0.02, 0.00).
5. Capacidad latente del camino LASSO en EXP-020 (AUC > 0.70) y brecha con EBIC.
6. Calibración de gamma y diagnóstico estratificado en EXP-021 (rescate en camino vs colapso EBIC).
7. Coincidencia entre los hashes de experimentos/registro.csv y los archivos en results/simulacion/.
"""
import sys
import hashlib
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def test_exp018():
    csv_path = RAIZ / "results" / "simulacion" / "EXP-018_resultados_ppi.csv"
    assert csv_path.exists(), f"No se encuentra {csv_path}"
    df = pd.read_csv(csv_path)
    assert len(df) == 360, f"EXP-018 debe tener 360 filas, tiene {len(df)}"
    
    # 1. Emparejamiento de réplicas
    map_df = df[df["pipeline"] == "bayesiana_map"].set_index(["condicion_id", "replica"])
    p50_df = df[df["pipeline"] == "bayesiana_ppi50"].set_index(["condicion_id", "replica"])
    assert (map_df["semilla"] == p50_df["semilla"]).all(), "Las semillas entre MAP y PPI-50 no coinciden"
    assert (map_df["aristas_verdaderas"] == p50_df["aristas_verdaderas"]).all(), "Las redes verdaderas difieren"
    
    # 2. Cero redes vacías en variantes bayesianas
    bayes_df = df[df["pipeline"].str.startswith("bayesiana")]
    assert bayes_df["red_vacia"].sum() == 0, f"Colapsos en bayesiana: {bayes_df['red_vacia'].sum()}"
    
    # 3. Colapso en frecuentistas en n=15
    frec_n15 = df[(df["n"] == 15) & (df["pipeline"].str.startswith("frecuentista"))]
    assert (frec_n15["red_vacia"] == 1).all(), "Frecuentista no colapsó al 100% en n=15"
    print("  [OK] EXP-018: 360 evaluaciones verificadas, emparejamiento MCMC y cero colapsos confirmados.")

def test_exp019():
    csv_path = RAIZ / "results" / "simulacion" / "EXP-019_resultados_conservadora.csv"
    assert csv_path.exists(), f"No se encuentra {csv_path}"
    df = pd.read_csv(csv_path)
    assert len(df) == 300, f"EXP-019 debe tener 300 filas, tiene {len(df)}"
    
    # Invarianza entre umbrales post-hoc
    u008 = df[df["pipeline"] == "conservadora_u008"].set_index(["condicion_id", "replica"])
    u005 = df[df["pipeline"] == "conservadora_u005"].set_index(["condicion_id", "replica"])
    u002 = df[df["pipeline"] == "conservadora_u002"].set_index(["condicion_id", "replica"])
    u000 = df[df["pipeline"] == "conservadora_u000"].set_index(["condicion_id", "replica"])
    
    assert (u008["aristas_estimadas"] == u000["aristas_estimadas"]).all(), "Diferencias entre u008 y u000"
    assert (u005["aristas_estimadas"] == u000["aristas_estimadas"]).all(), "Diferencias entre u005 y u000"
    assert (u002["aristas_estimadas"] == u000["aristas_estimadas"]).all(), "Diferencias entre u002 y u000"
    
    vac_count = u000["red_vacia"].sum()
    assert vac_count == 49, f"Esperadas 49 redes vacías en conservadora, encontradas {vac_count}"
    print("  [OK] EXP-019: 300 evaluaciones verificadas, invarianza absoluta entre umbrales post-hoc confirmada.")

def test_exp020():
    camino_path = RAIZ / "results" / "simulacion" / "EXP-020_resultados_camino_completo.csv"
    auc_path = RAIZ / "results" / "simulacion" / "EXP-020_capacidad_latente_auc.csv"
    assert camino_path.exists(), f"No se encuentra {camino_path}"
    assert auc_path.exists(), f"No se encuentra {auc_path}"
    
    df_camino = pd.read_csv(camino_path)
    df_auc = pd.read_csv(auc_path)
    
    assert len(df_camino) == 6000, f"EXP-020 camino debe tener 6000 filas, tiene {len(df_camino)}"
    assert len(df_auc) == 60, f"EXP-020 AUC debe tener 60 filas, tiene {len(df_auc)}"
    
    # 1. Comprobar capacidad discriminativa latente del camino (AUC medio > 0.70)
    mean_auc = df_auc["AUC_ROC_max_path"].mean()
    assert mean_auc > 0.70, f"El AUC latente del camino es {mean_auc:.4f}, menor a 0.70"
    
    # 2. Comprobar brecha con selección EBIC estándar (AUC ~ 0.50 en grafos vacíos)
    ebic_auc = df_auc["AUC_EBIC_g050"].mean()
    assert ebic_auc < 0.55, f"EBIC no debió haber colapsado a red vacía (AUC={ebic_auc:.4f})"
    
    # 3. Techo de F1 en el camino sustancialmente superior a cero
    assert df_auc["F1_max_path"].mean() > 0.40, "El F1 máximo en el camino es demasiado bajo"
    print(f"  [OK] EXP-020: 6,000 puntos de camino verificados. AUC latente={mean_auc:.4f} vs EBIC={ebic_auc:.4f}.")

def test_exp021():
    gamma_path = RAIZ / "results" / "simulacion" / "EXP-021_resultados_calibracion_gamma.csv"
    diag_path = RAIZ / "results" / "simulacion" / "EXP-021_diagnostico_n30_p6.csv"
    assert gamma_path.exists(), f"No se encuentra {gamma_path}"
    assert diag_path.exists(), f"No se encuentra {diag_path}"
    
    df_gamma = pd.read_csv(gamma_path)
    df_diag = pd.read_csv(diag_path)
    
    assert len(df_gamma) == 240, f"EXP-021 gamma debe tener 240 filas, tiene {len(df_gamma)}"
    assert len(df_diag) == 150, f"EXP-021 diagnóstico debe tener 150 filas, tiene {len(df_diag)}"
    
    # 1. Monotonía de penalización en redes vacías
    res_gamma = df_gamma.groupby("gamma")["red_vacia"].mean()
    assert res_gamma[0.00] < res_gamma[0.50], "BIC (gamma=0) no redujo redes vacías respecto a EBIC (gamma=0.5)"
    assert res_gamma[0.00] >= 0.60, "BIC no debería haber resuelto el colapso (esperado colapso >= 60%)"
    
    # 2. Diagnóstico estratificado n=30, p=6: aristas fuertes
    fuertes = df_diag[df_diag["estrato_fuerza"] == "fuerte"]
    assert len(fuertes) > 0, "No se encontraron aristas verdaderas fuertes"
    assert (fuertes["recuperada_best_path"] == 1).all(), "Las aristas fuertes no se recuperaron en el camino"
    assert (fuertes["recuperada_EBIC_g050"] == 0).all(), "EBIC 0.50 seleccionó indebidamente en n=30 p=6"
    print("  [OK] EXP-021: 240 calibraciones y diagnóstico estratificado n=30 p=6 confirmados con éxito.")

def test_registro_hashes():
    reg_path = RAIZ / "experimentos" / "registro.csv"
    assert reg_path.exists(), "No existe experimentos/registro.csv"
    reg = pd.read_csv(reg_path)
    
    # Hash EXP-018 salida
    row18 = reg[reg["id"] == "EXP-018"].iloc[0]
    file18 = RAIZ / "results" / "simulacion" / "EXP-018_resultados_ppi.csv"
    assert sha256_file(file18) == row18["hash_salida"], "Hash de salida EXP-018 no coincide"
    
    # Hash EXP-019 salida
    row19 = reg[reg["id"] == "EXP-019"].iloc[0]
    file19 = RAIZ / "results" / "simulacion" / "EXP-019_resultados_conservadora.csv"
    assert sha256_file(file19) == row19["hash_salida"], "Hash de salida EXP-019 no coincide"

    # Hash EXP-020 salida
    row20 = reg[reg["id"] == "EXP-020"].iloc[0]
    file20 = RAIZ / "results" / "simulacion" / "EXP-020_resultados_camino_completo.csv"
    assert sha256_file(file20) == row20["hash_salida"], "Hash de salida EXP-020 no coincide"

    # Hash EXP-021 salida
    row21 = reg[reg["id"] == "EXP-021"].iloc[0]
    file21 = RAIZ / "results" / "simulacion" / "EXP-021_resultados_calibracion_gamma.csv"
    assert sha256_file(file21) == row21["hash_salida"], "Hash de salida EXP-021 no coincide"

    print("  [OK] Registro de experimentos: hashes criptográficos SHA-256 contrastados con éxito (EXP-018..EXP-021).")

if __name__ == "__main__":
    print("Ejecutando verificaciones científicas y de reproducibilidad...")
    try:
        test_exp018()
        test_exp019()
        test_exp020()
        test_exp021()
        test_registro_hashes()
        print("\nTodas las pruebas de reproducibilidad pasaron exitosamente.")
        sys.exit(0)
    except AssertionError as e:
        print(f"\n[ERROR DE REPRODUCIBILIDAD] {e}", file=sys.stderr)
        sys.exit(1)
