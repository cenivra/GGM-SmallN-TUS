# Changelog

Convención: fecha ISO (AAAA-MM-DD), tipos Added / Changed / Fixed / Removed / Deprecated, y una
sección **Unreleased** para lo que aún no se publica. El changelog es curado: no se vuelca el
historial de git.

## Unreleased

### Added (2026-09-27) — Estructura inicial del repositorio
- `README.md`, `CHANGELOG.md`, `CITATION.cff`, `LICENSE`, `.gitattributes`, `.gitignore`.
- `R/`, `analysis/` (con `diseno_simulacion/`, `calibracion/`, `resultados/`), `docs/`,
  `manuscript/`, `verificacion/`, `results/`, `tests/`, `.github/`.
- Cada carpeta con su `README.md` que declara qué recibirá.

### No creado todavía (declarado para que la estructura no prometa de más)
- **Código del motor**: los scripts de R existen en el proyecto de trabajo y aún no se han
  copiado aquí.
- **Resultados**: ninguna tabla ni figura está publicada aún en este repositorio; las carpetas
  `results/` y `analysis/` describen lo que alojarán.
- **Datos**: no se versiona ningún dato de personas. Ver `docs/NOTA_sobre_los_datos.md`.
- **Manuscrito**: las fuentes LaTeX viven en el proyecto de trabajo; su copia aquí está pendiente
  de la decisión de embargo.
- **`LICENSE`**: aplicado MIT para el código; si el propietario prefiere otra licencia para la
  documentación, se cambia en un solo archivo.
