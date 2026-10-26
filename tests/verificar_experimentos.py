"""Verificación científica y de integridad de los experimentos reproducibles publicados.

Comprueba:
1. Existencia e integridad de las tablas de resultados de EXP-018 y EXP-019.
2. Emparejamiento perfecto (mismas condiciones, réplicas y semillas) entre variantes MCMC de EXP-018.
3. Inmunidad bayesiana al colapso a red vacía (tasa de red vacía == 0.0%).
4. Invarianza matemática demostrada en EXP-019 entre los 4 umbrales post-hoc (u=0.08, 0.05, 0.02, 0.00).
5. Coincidencia entre los hashes de experimentos/registro.csv y los archivos en results/simulacion/.
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

def test_registro_hashes():
    reg_path = RAIZ / "experimentos" / "registro.csv"
    assert reg_path.exists(), "No existe experimentos/registro.csv"
    reg = pd.read_csv(reg_path)
    
    row18 = reg[reg["id"] == "EXP-018"].iloc[0]
    file18 = RAIZ / "results" / "simulacion" / "EXP-018_resultados_ppi.csv"
    assert sha256_file(file18) == row18["hash_salida"], "Hash de salida EXP-018 no coincide"
    
    row19 = reg[reg["id"] == "EXP-019"].iloc[0]
    file19 = RAIZ / "results" / "simulacion" / "EXP-019_resultados_conservadora.csv"
    assert sha256_file(file19) == row19["hash_salida"], "Hash de salida EXP-019 no coincide"
    print("  [OK] Registro de experimentos: hashes criptográficos SHA-256 contrastados con éxito.")

if __name__ == "__main__":
    print("Ejecutando verificaciones científicas y de reproducibilidad...")
    try:
        test_exp018()
        test_exp019()
        test_registro_hashes()
        print("\nTodas las pruebas de reproducibilidad pasaron exitosamente.")
        sys.exit(0)
    except AssertionError as e:
        print(f"\n[ERROR DE REPRODUCIBILIDAD] {e}", file=sys.stderr)
        sys.exit(1)
