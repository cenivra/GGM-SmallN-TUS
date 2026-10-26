# Resultados

Tablas y figuras derivadas, **sin identificadores**: recuentos por régimen y por configuración,
métricas con su denominador declarado y conjuntos de resultados de simulación controlada.

## Regla

Ninguna tabla contiene una fila por persona ni texto clínico, y la admisibilidad se comprueba **por
contenido**, no por el nombre del archivo: se abren los CSV y se comprueba que ninguna celda
contenga texto libre largo, y que ninguna tabla tenga una fila por participante.

## Estructura actual

- **`results/simulacion/`**: resultados cuantitativos abiertos derivados de experimentos de simulación
  sintética (sin datos de personas ni variables clínicas):
  - `EXP-018_resultados_ppi.csv`: 360 evaluaciones de filtrado marginal bayesiano (MAP vs PPI) y frecuentista en muestras pequeñas ($n \in \{15, 30, 60\}$).
  - `EXP-019_resultados_conservadora.csv`: 300 evaluaciones factoriales de calibración de umbrales post-hoc sobre EBIC ($\gamma = 0.50$).
- Los resultados de Fase II (análisis sobre muestras clínicas reales) se reservan para su publicación junto con el manuscrito formal.
