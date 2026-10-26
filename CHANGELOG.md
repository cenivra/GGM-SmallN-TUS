# Changelog

Convención: fecha ISO (AAAA-MM-DD), tipos Added / Changed / Fixed / Removed / Deprecated, y una
sección **Unreleased**. El changelog es curado: no se vuelca el historial de git.

## 2026-10-25 — Incorporación de la serie experimental EXP-018 y EXP-019

### Added
- `experimentos/entradas/`:
  - `2026-10-25_EXP-018.md`: diario de laboratorio de EXP-018 (evaluación de filtrado marginal bayesiano PPI 0.40, 0.50, 0.60 vs MAP sobre cadenas MCMC de BDgraph).
  - `2026-10-25_EXP-019.md`: diario de laboratorio de EXP-019 (calibración paramétrica de umbrales post-hoc sobre EBIC $\gamma=0.50$ y causa raíz del colapso).
- `results/simulacion/`:
  - `EXP-018_resultados_ppi.csv`: 360 evaluaciones de simulación ordinal emparejadas (SHA-256 verificado: `95c73280b657...`).
  - `EXP-019_resultados_conservadora.csv`: 300 evaluaciones factoriales de simulación ordinal (SHA-256 verificado: `a513a998e42d...`).
- `tests/verificar_experimentos.py`: prueba automatizada independiente que comprueba la integridad de réplicas, invarianza paramétrica y tasas de colapso sin requerir datos clínicos.
- `docs/decisiones.md`: adición de dos decisiones formales:
  1. Adopción del Modelo de Probabilidad Mediana ($PPI \ge 0.50$) como regla de selección posterior bayesiana.
  2. Descontinuación de la penalización combinatoria asintótica $\gamma = 0.50$ para regímenes $n \le 30$ en EBIC.

### Changed
- `experimentos/registro.csv`: poblado con los asientos formales correspondientes a EXP-015, EXP-017, EXP-018 y EXP-019, incluyendo semillas, configuraciones y hashes criptográficos de entrada y salida.
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
