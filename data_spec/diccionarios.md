# Diccionarios y convenciones

## Cómo se nombran las columnas

- Los identificadores conservan el nombre de origen (`id_origen`); todo lo demás se normaliza.
- Los acentos se sustituyen por guion bajo (`activaci_n`), de modo que el nombre es ASCII.
- Las columnas de origen que no se mapearon a una subescala quedan como `col_NN`: existen para no
  perder información, no como variables analizables.

## Qué es un valor ausente

- El valor ausente es un vacío en la celda, **nunca** un cero ni un texto. Un cero es una
  respuesta observada.
- En el registro de experimentos, «NA» significa que la etapa no aplica, no que no se haya
  declarado: la convención se declara en cada archivo porque confundirla convierte una corrida
  exitosa en una falla.

## Llaves de identidad

- La base usa `id_origen` como identificador seudonimizado y estable.
- Cualquier tabla derivada se une **por esa llave**, nunca por posición de fila: dos archivos del
  mismo programa no coinciden en todos los campos y una unión por posición desalinea los registros
  en silencio.
- El tipo de la llave se normaliza antes de unir (la misma llave puede estar como texto en un
  archivo y como número en otro).
