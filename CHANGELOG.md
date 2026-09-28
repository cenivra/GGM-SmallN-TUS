# Changelog

Convención: fecha ISO (AAAA-MM-DD), tipos Added / Changed / Fixed / Removed / Deprecated, y una
sección **Unreleased**. El changelog es curado: no se vuelca el historial de git.

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
