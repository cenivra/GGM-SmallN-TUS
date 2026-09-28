# Resultados

Lo que alojará esta carpeta, cuando el material se copie:

- La **rejilla de la Fase I** en CSV, con una fila por configuración y las columnas de régimen,
  marco, métricas y estado de la corrida.
- Las **figuras** del manuscrito (tasa de redes vacías por régimen, F1 frente a n/p, estabilidad
  de aristas).
- El **registro de experimentos**: cada corrida con su identificador, su estado de ejecución y
  los artefactos que produjo.

## Saneado obligatorio antes de publicar

El registro generado en el equipo contiene rutas absolutas y nombres de archivo locales. Antes de
versionarlo hay que sustituirlas por rutas relativas: una ruta absoluta revela el nombre de
usuario y el modo en que se produjo cada archivo. La comprobación es una búsqueda literal del
nombre de usuario en todo el árbol.

## Regla

Ninguna tabla de esta carpeta contiene una fila por persona. Son resultados agregados por
configuración o por grupo.
