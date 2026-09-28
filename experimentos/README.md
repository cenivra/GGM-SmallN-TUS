# Diario de experimentos

Aquí se registra **qué se corrió, cuándo y con qué**, sin publicar el motor ni sus resultados.
Es el cuaderno de laboratorio del proyecto, y existe por una razón concreta: poder afirmar después
cuándo se hizo algo y con qué, sin depender de la memoria de nadie.

## Qué se registra

| campo | por qué |
|---|---|
| `id` | identificador estable del experimento, asignado una vez y nunca reutilizado |
| `fecha_inicio` / `fecha_cierre` | cuándo empezó y cuándo terminó |
| `fase` | Fase I (simulación) o Fase II (clínicas) |
| `escenario` | qué se estaba probando, en una línea |
| `n`, `p` | tamaño muestral y número de variables de la corrida |
| `marco` | qué familia de estimación se corrió |
| `estado_ejecucion` | terminó, red vacía o falló (un fallo registrado es un dato) |
| `estado_registro` | si el asiento quedó completo; separado del anterior |
| `semilla` | para poder repetir sin adivinar |
| `hash_entrada` / `hash_salida` | SHA-256 de la entrada y de la salida |
| `nota` | lo que no cabe en una columna |

## Qué NO se registra aquí

- **Los valores de los resultados.** El registro fija que una corrida existió y qué produjo en
  términos de estado; los números van al manuscrito. Un registro con las cifras finales sería
  publicar los resultados antes del artículo.
- **Los pesos, los hiperparámetros y la lógica del motor.**
- **Datos de personas**: el registro guarda el hash de la entrada, nunca su contenido.

## Cómo se usa

1. Al abrir una corrida, se añade la fila con fecha de inicio y estado «en curso».
2. Al cerrarla, se completan fecha, estado de ejecución y hashes.
3. Se regenera el manifiesto (`tests/generar_manifiesto.py`) y se declara en `CHANGELOG.md` si el
   cambio es material.

La plantilla de una entrada larga está en `PLANTILLA_diario.md`.
