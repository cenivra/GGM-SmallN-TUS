# Diseño de simulación (congelado)

Dos fases, con propósitos distintos y por eso con unidades distintas:

## Fase I — simulación

- **Bloque de subescala**: n en {25, 30, 50, 80, 120, 150} y p en {6, 10, 14}.
- **Bloque de ítem**: p en {45, 60} y n en {30, 50, 75, 100} — aquí sí existe el régimen n < p real.
- **Factores**: tipo de escala (continua, ordinal de 5, ordinal de 7), asimetría, arquitectura
  topológica, calidad del prior y el régimen n/p como variable de clasificación.
- **Marcos comparados** en el mismo archivo de resultados: EBICglasso con gamma 0.5, EBICglasso
  con gamma 0.25, el motor GGM Small-n y la familia bayesiana.
- **Réplicas**: mínimo 30 por celda, objetivo 100.
- **Resultado primario**: tasa de redes vacías. Secundarios: MCC, F1, sensibilidad y
  especificidad, cada uno con su denominador declarado.

## Fase II — validación con datos clínicos reales

- Muestras clínicas de TUS, incluida una con 90 ítems y n menor que p, de modo que el régimen
  n < p se comprueba con datos reales y no solo simulados.
- Aquí **no se mide recuperación estructural** (no hay grafo verdadero): se reportan estado,
  acción recomendada por la política y estabilidad de aristas.

## Qué falta

- Escalón de réplicas intermedias para el análisis de sensibilidad.
- El banco semisintético que permite hablar de recuperación con estructura clínica plausible.
