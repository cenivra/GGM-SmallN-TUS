# El motor

Aquí va el código de estimación. El proyecto mantiene **dos versiones del mismo motor**, y la
razón es que deben comportarse igual: cualquier diferencia entre ellas es un defecto que se
comprueba, no una variante aceptada.

| archivo (en el proyecto de trabajo) | qué hace |
|---|---|
| `GGM_SMALL_n_PSICOMETRICO.R` (motor psicométrico) | generación de datos por arquitectura, correlaciones robustas, estimación por familia, métricas, recompensa y calibración |
| `GGM_SMALL_n_PSICOMETRICO_V_Aprendizaje_automatico.R` (motor de aprendizaje) | la misma cadena más el bucle de decisión, el suavizado por núcleo y el registro de artefactos |
| módulo de extensiones (IA) | detector de redes degeneradas, validación por dejar-uno-fuera, apilado, agrupamiento y registro de contexto |
| registrador de experimentos (Python) | abre y cierra cada corrida, inventaría artefactos con `ART-###` estable y escribe el registro maestro |

## Contrato entre las dos versiones

- La **taxonomía del régimen** (las seis bandas de n/p) es una sola definición, compartida.
- Las **métricas** y la **recompensa** se calculan con las mismas fórmulas en ambas.
- Las **firmas** de las funciones compartidas no se cambian sin cambiar las dos versiones a la vez.

## Estado

Los scripts viven aún en el proyecto de trabajo. Al copiarlos aquí se conservan byte a byte, con
su hash declarado, para que los resultados publicados sean atribuibles a la versión que corrió.
