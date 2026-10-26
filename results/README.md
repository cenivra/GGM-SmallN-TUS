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
  - `EXP-020_resultados_camino_completo.csv`: 6,000 puntos del camino continuo de regularización $\ell_1$ ($n_\lambda=100$) evaluando densidad, F1 y log-verosimilitud.
  - `EXP-020_capacidad_latente_auc.csv`: 60 evaluaciones de capacidad discriminativa latente del estimador (AUC ROC) vs EBIC.
  - `EXP-021_resultados_calibracion_gamma.csv`: 240 evaluaciones emparejadas de la calibración de hiperparámetro $\gamma \in \{0.00, 0.10, 0.25, 0.50\}$.
  - `EXP-021_diagnostico_n30_p6.csv`: 150 aristas analizadas para diagnosticar la tasa de recuperación de aristas según su fuerza empírica en $n=30, p=6$.
- Los resultados de Fase II (análisis sobre muestras clínicas reales) se reservan para su publicación junto con el manuscrito formal.
