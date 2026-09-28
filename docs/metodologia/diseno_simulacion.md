# Diseño de simulación

Dos fases con propósitos distintos, y por eso con unidades distintas.

## Fase I — simulación

- **Bloque de subescala**: seis tamaños muestrales y tres números de variables.
- **Bloque de ítem**: dos números de variables y cuatro tamaños muestrales, elegidos de modo que
  el régimen n < p exista de verdad.
- **Factores**: tipo de escala (continua y dos ordinales), asimetría, arquitectura topológica y
  calidad del prior.
- **Marcos comparados sobre el mismo diseño**: la familia regularizada con dos valores de rigor
  distintos, el motor de este proyecto y la familia bayesiana.
- **Réplicas**: mínimo 30 por celda, objetivo 100.
- **Resultado primario**: la tasa de redes vacías, porque un método que devuelve una red vacía no
  está fallando en silencio: está fallando de forma medible.
- **Secundarios**: recuperación de aristas y de su ausencia, con el denominador declarado en cada
  cifra.

## Fase II — datos clínicos reales

- Muestras clínicas de trastorno por consumo de sustancias, incluida una con más de 90 variables y
  menos observaciones que variables.
- Aquí **no se mide recuperación estructural** (no existe grafo verdadero): se reportan el estado
  calculado, la acción recomendada y la estabilidad de las aristas.

## Por qué el diseño no se cambia a mitad del camino

Los factores, los niveles y el número de réplicas se fijan antes de ver resultados. Ajustar el
diseño después de mirar las tasas convierte una prueba en una búsqueda, y el repositorio dejaría
de poder declarar qué se probó.
