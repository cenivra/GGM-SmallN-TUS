# Changelog

Convención: fecha ISO (AAAA-MM-DD), tipos Added / Changed / Fixed / Removed / Deprecated, y una
sección **Unreleased**. El changelog es curado: no se vuelca el historial de git.

## 2026-10-25 — Incorporación de la serie experimental EXP-018 a EXP-021

### Added
- `experimentos/entradas/`:
  - `2026-10-25_EXP-018.md`: diario de laboratorio de EXP-018 (evaluación de filtrado marginal bayesiano PPI 0.40, 0.50, 0.60 vs MAP sobre cadenas MCMC de BDgraph).
  - `2026-10-25_EXP-019.md`: diario de laboratorio de EXP-019 (calibración paramétrica de umbrales post-hoc sobre EBIC $\gamma=0.50$ y causa raíz del colapso).
  - `2026-10-25_EXP-020.md`: diario de laboratorio de EXP-020 (exploración del camino continuo de regularización $\ell_1$ con $\lambda_{\min\text{-ratio}}=0.001$, $n_\lambda=100$, y evaluación de capacidad latente AUC ROC).
  - `2026-10-25_EXP-021.md`: diario de laboratorio de EXP-021 (calibración emparejada de hiperparámetro $\gamma \in \{0.00, 0.10, 0.25, 0.50\}$ y diagnóstico estratificado por fuerza de arista en $n=30, p=6$).
- `results/simulacion/`:
  - `EXP-018_resultados_ppi.csv`: 360 evaluaciones de simulación ordinal emparejadas (SHA-256 verificado: `95c73280b657...`).
  - `EXP-019_resultados_conservadora.csv`: 300 evaluaciones factoriales de simulación ordinal (SHA-256 verificado: `a513a998e42d...`).
  - `EXP-020_resultados_camino_completo.csv`: 6,000 puntos del camino continuo de regularización (SHA-256 verificado: `b25bc350c036...`).
  - `EXP-020_capacidad_latente_auc.csv`: 60 evaluaciones resumen de capacidad latente AUC ROC y brecha con EBIC.
  - `EXP-021_resultados_calibracion_gamma.csv`: 240 evaluaciones emparejadas de la calibración de $\gamma$ (SHA-256 verificado: `6496e6ce51fb...`).
  - `EXP-021_diagnostico_n30_p6.csv`: 150 aristas analizadas en detalle para $n=30, p=6$ estratificadas por magnitud real.
- `tests/verificar_experimentos.py`: prueba automatizada independiente que comprueba la integridad de réplicas, invarianza paramétrica, capacidad discriminativa latente del camino, y tasas de colapso en EXP-018 a EXP-021 sin requerir datos clínicos.
- `docs/decisiones.md`: adición de cuatro decisiones formales:
  1. Adopción del Modelo de Probabilidad Mediana ($PPI \ge 0.50$) como regla de selección posterior bayesiana.
  2. Descontinuación de la penalización combinatoria asintótica $\gamma = 0.50$ para regímenes $n \le 30$ en EBIC.
  3. Demostración de capacidad latente en el camino LASSO ($AUC_{\text{ROC}} \approx 0.71-0.81$) atribuyendo el colapso al criterio de selección y no a ausencia de señal.
  4. Insuficiencia de BIC clásico ($\gamma = 0.00$) y necesidad de criterios de estabilidad (StARS / Stability Selection).

### Changed
- `experimentos/registro.csv`: poblado con los asientos formales correspondientes a EXP-015, EXP-017, EXP-018, EXP-019, EXP-020 y EXP-021, incluyendo semillas, configuraciones y hashes criptográficos de entrada y salida.
- `README.md`, `results/README.md`, `tests/README.md`, `experimentos/README.md`: actualizados para documentar la presencia de los resultados de simulación abiertos y la suite de pruebas.
- `manifests/SHA256_REPO.txt`: manifiesto regenerado con las huellas criptográficas actualizadas.

## 2026-09-27 — Reestructuración al layout de repositorios similares

### Added
- `code/README.md`: características del motor, sin pesos ni lógica interna.
- `data_spec/`: `codebook.md` (recuentos confirmados contra la base el 2026-09-27) y
  `diccionarios.md` (nombres, valores ausentes, llaves).
- `experimentos/`: diario, plantilla de entrada y registro tabular (`registro.csv`).
- `manifests/`, `tests/generar_manifiesto.py`, `tests/check_hashes.sh`, `docs/integridad.md`.
- `docs/metodologia/` (diseño y calibración), `docs/decisiones.md`, `docs/requisitos_entorno.md`.
- `limpiar_rutas.txt`: la receta de saneado de rutas.

### Removed
- `manuscript/` y `analysis/` — el manuscrito no se publica en el repositorio y el layout se
  alinea con los repositorios similares del propio proyecto.
- `docs/diccionario_variables.md`, duplicado: el codebook vive en `data_spec/codebook.md`
  (un solo hogar por artefacto).
- **La tabla de calibración con valores** (`gamma`, `lambda`, `umbral`): se reserva hasta la
  publicación del artículo. En su lugar, `docs/metodologia/calibracion.md` documenta la estructura
  y el criterio.

### No creado todavía (declarado para que la estructura no prometa de más)
- **Código del motor**: se incorpora tras la publicación del artículo.
- **Resultados**: las tablas y figuras se publican con el artículo; `results/` está vacía.
- **Manuscrito**: vive en el proyecto de trabajo, no aquí.
- **Datos**: no se versiona ningún dato de personas.

### Fixed
- Rutas absolutas y nombre de usuario: verificados en cero en todo el árbol (la única aparición
  del nombre de usuario es `limpiar_rutas.txt`, que es la receta con la que se buscan).
