# Procedencia de los datos y condiciones de acceso

Esta nota describe de dónde salen los datos del proyecto y bajo qué condiciones pueden
consultarse. Su finalidad es la transparencia y el cumplimiento ético con las personas que
participaron.

## Procedencia

Los análisis parten de registros clínicos de un programa de tratamiento residencial para
trastornos por uso de sustancias en Jalisco, México, y se complementan con un conjunto de datos
abierto de la misma población.

- **Muestras propias**: aplicaciones de instrumentos en la población del programa, con los
  tamaños muestrales por escala que declara `diccionario_variables.md`. De ahí se derivó una base
  pseudonimizada: cada persona recibe un identificador secuencial, sin nombre, sin fecha de
  nacimiento y sin campo que permita reidentificarla.
- **Conjunto abierto de comparación**: la base pública de conectividad en trastornos por consumo
  de sustancias (SUDMEX_CONN, `doi:10.5281/zenodo.7491740`, licencia CC-BY-4.0), que incluye
  controles sanos y pacientes y una escala de 90 ítems. Es la que permite el régimen n < p con
  datos clínicos reales.

## Qué no se distribuye, y por qué

- **La base pseudonimizada.** Aun sin nombres, contiene datos clínicos de personas identificables
  por combinación de variables, y la muestra es pequeña.
- **Los registros originales** de captura, que sí contienen nombres y datos administrativos.
- **Cualquier archivo con identificadores** directos o indirectos, incluidas las hojas de cálculo
  de origen.

## Condiciones de acceso

Mediante el comité de ética del proyecto, con el protocolo aprobado y un acuerdo de uso que fije
el propósito, el plazo y la prohibición de intentar reidentificar a los participantes. El acceso a
los registros originales requiere solicitud formal con justificación del uso previsto.

## Cómo se comprueba que el repositorio no contiene datos

Antes de cada publicación se recorre el árbol completo buscando los identificadores y los nombres
de los registros de origen, uno por uno, y se verifica que ninguna tabla versionada contenga texto
clínico. Las tablas de `results/` son agregados por configuración, sin una fila por persona.

## Advertencias

- Las cifras de un conjunto **no** son las del otro: dos muestras del mismo fenómeno con edades,
  instrumentos y momentos distintos no se suman. Cada tabla declara de qué conjunto sale.
- Los análisis con datos reales no pueden reportar recuperación estructural, porque no existe
  grafo verdadero: eso se sostiene con simulación o con un banco semisintético, y así se declara.
