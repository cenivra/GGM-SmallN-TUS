# Requisitos del entorno

## Para correr los análisis (cuando el código se publique)

- **R** 4.x con los paquetes de estimación de redes (`qgraph`, `glasso`, `huge`, `BDgraph`,
  `bootnet`) y `parallel` para el remuestreo.
- **Python** 3.x para el registrador de experimentos y los manifiestos (sólo biblioteca estándar).
- Un compilador de C++ para los paquetes que lo requieren (en Windows, `Rtools`).

## Notas de entorno que ya costaron tiempo

- La ruta del compilador se fija **por variable de entorno propia**, no en el `PATH` del sistema:
  añadirla al `PATH` rompe la carga de R.
- El remuestreo en paralelo necesita que los procesos hijos reciban las funciones y los objetos del
  entorno; sin eso, el fallo aparece como «objeto no encontrado» y se confunde con un error del
  motor. El camino en serie sirve para distinguir uno de otro.
- Un `RData` de sesión no es un respaldo del script: se conserva como evidencia, no como fuente.
