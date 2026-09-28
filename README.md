# GGM Small-n — Redes psicométricas en muestras pequeñas (TUS)

Material de investigación del proyecto **GGM Small-n**: un marco para estimar y decidir en
redes gaussianas gráficas cuando el cociente entre observaciones y variables es desfavorable, con
el trastorno por consumo de sustancias (TUS) como banco de pruebas.

El repositorio contiene **el código del motor, el diseño de simulación congelado, los resultados
agregados y la verificación de la bibliografía**. No contiene datos de pacientes.

Estado: **en preparación** (el manuscrito principal va a *Psychometrika*, sección Theory and
Methods). Lo que aún no existe se declara como tal en `CHANGELOG.md`, en la sección «Qué NO está
aquí».

## Estructura

```
R/                    El motor: dos versiones del pipeline y sus módulos
  README.md             qué hace cada script y en qué orden se ejecutan
analysis/
  README.md             el análisis: diseño, calibración y resultados reproducibles
  diseno_simulacion/    el diseño factorial congelado (Fase I y Fase II)
  calibracion/          la tabla de calibración por régimen (gamma, lambda, umbral)
  resultados/           resultados agregados, figuras y el registro de experimentos
docs/                 Documentación técnica y gobernanza
  NOTA_sobre_los_datos.md    procedencia de los datos y condiciones de acceso
  diccionario_variables.md   instrumentos, subescalas y tamaños muestrales (sin filas)
  gobernanza_y_registro.md   cómo se registra cada corrida y qué la hace auditable
  PLAN_DE_PUBLICACIONES.md   qué artículos salen de este trabajo y qué evidencia usa cada uno
manuscript/           Las fuentes LaTeX del artículo principal y su verificación
verificacion/         Informes de verificación: bibliografía, trazabilidad, auditorías
results/              Tablas y figuras derivadas, sin identificadores
tests/                Pruebas del sistema de registro experimental
```

## Cómo reproducir

1. Instala R (4.x) y los paquetes que declaran los scripts del motor; requieren `qgraph`,
   `glasso`, `huge`, `BDgraph`, `bootnet` y `parallel`.
2. Los scripts esperan la base clínica **fuera del repositorio**. La ruta se configura en el
   script; no se versiona ninguna ruta local.
3. El motor se ejecuta en dos versiones (pipeline psicométrico y pipeline de aprendizaje) y
   comparte los módulos de calibración, métricas y registro.
4. Las tablas y figuras de `results/` se regeneran desde `analysis/resultados/`.

## Resultados que reproducirá este repositorio

| tabla del manuscrito | de dónde sale |
|---|---|
| Tasa de redes vacías y métricas por régimen | `analysis/resultados/` (rejilla de Fase I) |
| Tabla de calibración por banda de n/p | `analysis/calibracion/` |
| Correspondencia entre la utilidad del artículo y la recompensa del motor | `docs/` y el anexo del manuscrito |

## Qué NO está aquí, y por qué

- **Datos de pacientes.** La base clínica pseudonimizada vive fuera del repositorio y no se
  distribuye. Ver `docs/NOTA_sobre_los_datos.md`.
- **Los microdatos de simulación por réplica** con rutas locales: la rejilla agregada sí entra,
  los archivos con rutas absolutas del equipo se sanean antes de publicarse.
- **Los informes de delegación** (auditorías internas de los agentes y sus refutaciones): son
  material de proceso y viven en el proyecto de trabajo.
- **Los datos originales** de captura (hojas de cálculo) y cualquier archivo con identificadores.

## Cita

Ver `CITATION.cff`.

## Licencia

MIT para el código (ver `LICENSE`). La documentación y las tablas se comparten con la misma
licencia salvo que un archivo diga otra cosa.
