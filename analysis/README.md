# Análisis

Tres bloques, en este orden:

1. **`diseno_simulacion/`** — el diseño factorial congelado: qué se simula, con qué factores y
   cuántas réplicas. Es la definición de la evidencia; no se cambia después de ver resultados.
2. **`calibracion/`** — la tabla que fija, para cada banda del cociente n/p, el valor de los
   hiperparámetros (gamma del EBIC, lambda y umbral de decisión de la familia regularizada) y el
   ajuste por tipo de escala.
3. **`resultados/`** — la rejilla de resultados agregados, las figuras y el registro de
   experimentos. Aquí es donde el manuscrito toma sus cifras.

Regla de procedencia: cada cifra de `resultados/` declara el archivo del que sale y el hash del
script que la produjo.
