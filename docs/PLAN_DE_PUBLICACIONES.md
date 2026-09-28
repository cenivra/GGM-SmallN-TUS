# Plan de publicaciones: qué unidades contiene este trabajo

La pregunta es si de este proyecto salen más artículos además del principal. La respuesta es sí —
el trabajo contiene **unidades de evidencia distintas**, y cada una responde una pregunta que las
otras no responden. Eso es lo que evita que se lean como trozos del mismo resultado.

## 1. Marco metodológico (el artículo principal)

- **Pregunta**: ¿cómo decidir y reportar la estimación de una red cuando la estructura no está
  identificada por los datos?
- **Contribución**: los cuatro principios, la formulación como problema de decisión y una
  arquitectura que lo aproxima.
- **Destino**: *Psychometrika*, Theory and Methods.
- **Evidencia**: la formulación, la demostración con simulación de las propiedades de la política
  y su aplicación clínica.

## 2. Estudio de simulación sobre el fallo del pipeline estándar

- **Pregunta**: ¿cuándo —y con qué frecuencia— el procedimiento estándar produce redes vacías o
  irrecuperables, según el régimen?
- **Contribución**: la tasa de redes vacías como resultado primario, la taxonomía de regímenes y la
  evidencia de que el fallo es sistemático y predecible por n/p, no aleatorio.
- **Destino**: revista de métodos cuantitativos (*Behavior Research Methods* o *Multivariate
  Behavioral Research*).
- **Evidencia**: la rejilla completa de la Fase I. Es un artículo de evidencia, no de marco.
- **Nota**: se sostiene sin el artículo 1 si se publica primero, pero lo natural es que el marco
  aparezca antes y este lo cite.

## 3. Aplicación clínica: estructura de red en tratamiento residencial

- **Pregunta**: ¿cómo se organiza la red de impulsividad, regulación emocional y consumo en la
  población del programa, y qué cambia al estimarla en régimen desfavorable?
- **Contribución**: la red clínica leída con la incertidumbre declarada, y la diferencia entre lo
  que se puede afirmar y lo que no con estos tamaños muestrales.
- **Destino**: revista clínica de adicciones (*Addictive Behaviors*, *Journal of Substance Use and
  Addiction Treatment*, o una revista mexicana indexada).
- **Evidencia**: Fase II.

## 4. Propiedades psicométricas de los instrumentos en esta población

- **Pregunta**: ¿cómo se comportan los instrumentos aplicados (en particular los más breves) en
  esta población, y qué se puede decir de su estructura?
- **Contribución**: la estructura factorial y la confiabilidad observadas frente a las publicadas,
  con la diferencia declarada como tal.
- **Destino**: revista de psicometría o de salud mental en español.
- **Evidencia**: los datos de aplicación de instrumentos y su análisis factorial.
- **Nota**: es el único que puede escribirse sin el motor; su interés está en la comparación con
  los valores publicados.

## 5. Guía práctica (tutorial)

- **Pregunta**: ¿qué hace un investigador aplicado con estas decisiones, paso a paso?
- **Contribución**: un procedimiento reproducible con el código, del diagnóstico del régimen a la
  decisión y al reporte.
- **Destino**: *Advances in Methods and Practices in Psychological Science* o una revista de
  metodología aplicada.
- **Evidencia**: el código del motor y los ejemplos de la Fase II.

## 6. Nota de software (si el interés está en el código)

- **Pregunta**: ¿cómo se usa la implementación?
- **Destino**: *Journal of Open Source Software* o una nota de artículo en *Behavior Research
  Methods*.
- **Evidencia**: el repositorio, con pruebas y ejemplos reproducibles.

## Regla contra el troceado

Un artículo solo entra en esta lista si responde una pregunta que los demás no responden. Las
métricas de una misma corrida no se reparten entre dos artículos: si dos manuscritos necesitan la
misma tabla, uno de los dos se está justificando con el otro. Y el orden importa: el artículo 1
fija el vocabulario y la taxonomía que los demás citan.

## Lo que cada artículo necesita del repositorio

| artículo | sección del repositorio |
|---|---|
| 1 (marco) | `manuscript/` y `R/` |
| 2 (simulación) | `analysis/diseno_simulacion/`, `analysis/calibracion/`, `analysis/resultados/` |
| 3 (clínica) | `analysis/resultados/`, `docs/diccionario_variables.md` |
| 4 (psicometría) | `analysis/resultados/`, `docs/diccionario_variables.md` |
| 5 (tutorial) | `R/`, `tests/`, `results/` |
| 6 (software) | el repositorio completo |
