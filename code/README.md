# Características del motor

El motor de estimación resuelve un problema concreto: **estimar y decidir en una red gaussiana
gráfica cuando el cociente entre observaciones y variables es desfavorable**, en lugar de aplicar
un procedimiento único a cualquier conjunto de datos.

Este documento describe **qué hace** el motor. No incluye los pesos, los hiperparámetros de
calibración ni la lógica interna de decisión: esa parte se publica con el artículo.

## Qué recibe y qué devuelve

- **Entrada**: una matriz de datos (o de correlaciones) y los metadatos del contexto — tamaño
  muestral, número de variables, tipo de escala y el instrumento de origen.
- **Salida**: una red estimada con sus pesos, un conjunto de métricas de recuperación (para
  simulación), la incertidumbre declarada y la acción recomendada por la política.
- **Diagnóstico**: un veredicto sobre la propia estimación, que es lo que permite decidir si lo
  que devuelve es informativo o es una red vacía.

## Qué familias implementa

1. **Regularizada frecuentista** con criterio de selección de modelos por información extendida.
2. **Bayesiana** con priors que incorporan la estructura psicométrica del instrumento.
3. **Robusta para muestras pequeñas**: correlación policórica, corrección del sesgo de
   contracción, proyección a la matriz definida positiva más cercana y consenso por remuestreo.

Las tres se comparan sobre **el mismo diseño simulado**, de modo que la comparación no dependa de
los datos de una sola muestra.

## Cómo se organiza internamente

Dos versiones del mismo pipeline que deben comportarse igual (una con el bucle de decisión
completo, otra sin él) y módulos compartidos: clasificación del régimen, calibración, métricas,
recompensa y registro de artifacts. La correspondencia entre ambas se comprueba: una diferencia
entre las dos versiones es un defecto, no una variante.

## Lo que se publica y lo que no

| se publica | se reserva hasta la publicación |
|---|---|
| qué familias implementa y con qué criterio se comparan | los valores de calibración por régimen |
| qué métricas usa y cómo se declaran sus denominadores | los pesos de la función de decisión |
| el formato de entrada y salida | la lógica de la política y del suavizado |
| el sistema de registro y sus manifiestos | el código (`code/`, más abajo) |

## Estado del código

**No está en el repositorio.** Se incorpora cuando el artículo esté publicado, para que la
evidencia sea atribuible a una versión concreta del motor sin anticipar su contenido. Mientras
tanto, el repositorio conserva el **registro de experimentos** (ver `experimentos/`), que fija
qué se corrió, cuándo y con qué entradas, sin publicar el motor.
