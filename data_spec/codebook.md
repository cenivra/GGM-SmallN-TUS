# Codebook: instrumentos y variables

Recuentos **confirmados contra la base pseudonimizada** (consulta de lectura, 2026-09-27), no
copiados del diseño. Este documento describe variables y recuentos; no incluye ninguna fila.

## Instrumentos

| instrumento | ítems | subescalas registradas | registros con puntuación |
|---|---|---|---|
| BIS-11 (impulsividad de Barratt) | 30 | total, atención, motor, perseverancia, autocontrol | 141 |
| BSL-23 (síntomas limítrofes, versión breve) | 23 | general + 20 ítems puntuados individualmente | 141 |
| GAD-7 (ansiedad generalizada) | 7 | gad_total, interpretación, z, percentil | 141 |
| BADS (evitación y desregulación) | 25 | activación, evitación-rumia, afectación del trabajo, + series sin nombre | 141 |
| EROS (refuerzo ambiental observado) | 10 | pd, pc, z, puntuación T | 141 |
| OCI-R (obsesivo-compulsivo revisado) | 18 | lavado, verificación, orden, obsesiones, acumulación, neutralización, total | 142 |
| STAXI-2 (ira estado-rasgo) | 49 | sent, exp_f, exp_v, total_estado, temp, reacc, total_rasgo | 141 |

Participantes en la tabla maestra: **141** (`id_origen`, sexo, edad, razón de salida). No hay
nombre, fecha de nacimiento ni identificador directo.

## Conjunto abierto de comparación

- **SUDMEX_CONN** — base pública de conectividad en trastornos por consumo de sustancias,
  `doi:10.5281/zenodo.7491740`, licencia CC-BY-4.0. Incluye controles sanos y pacientes y una
  escala de 90 ítems, que es lo que permite el régimen n < p con datos reales.

## Advertencias de integridad (declaradas, no resueltas)

- **OCI-R tiene una fila más que participantes**: 142 registros con puntuación frente a 141
  personas, y el identificador de esa fila no aparece en la tabla maestra. Antes de usarla hay que
  decidir si es un registro de otra fuente, un error de captura o una fila duplicada con distinto
  identificador.
- **Columnas sin nombre** (`col_34`, `col_35`, …) en BADS y GAD-7: son columnas de origen que no
  se mapearon a una subescala. Se conservan para no perder información, pero no entran a los
  modelos hasta identificarlas.
- **Los nombres llevan el acento normalizado** (`activaci_n`): es la convención de la base, no una
  errata del documento.
- **Un registro con puntuación no equivale a datos completos**: los recuentos de arriba cuentan
  registros, no casos sin valores ausentes. La completitud por ítem se mide y se declara antes de
  usarse como N efectivo.
