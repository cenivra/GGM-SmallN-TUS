# Calibración por régimen

La calibración fija los hiperparámetros **en función del régimen** en que cae el conjunto de
datos, en lugar de usar un valor único. Es una de las piezas centrales del motor.

## Estructura

- Seis regímenes, definidos por el cociente entre el tamaño muestral efectivo y el número de
  variables.
- Para cada régimen: un valor de rigor en la selección de modelos, un umbral de decisión sobre los
  pesos estimados y una estrategia declarada (de ultraconservadora a estándar).
- Un ajuste por tipo de escala, porque las correlaciones sobre datos ordinales no se comportan
  igual que sobre datos continuos.

## Los valores no se publican aquí

**Los cortes de los regímenes y los valores de calibración se reservan hasta que el artículo esté
publicado.** Publicarlos ahora permitiría reproducir el comportamiento del motor sin la
calibración que le da sentido, y el trabajo de calibración es una contribución del artículo.

Se documentan aquí la estructura, el criterio y el hecho de que la calibración está cerrada y
verificada; los números van con el manuscrito.

## Regla de integridad

Los cortes y los valores son **una sola definición** para el documento y para el código: la
función que los implementa es la misma que cita el artículo. Cualquier cambio invalida la tabla
publicada y obliga a regenerarla, y por eso se registra como decisión.
