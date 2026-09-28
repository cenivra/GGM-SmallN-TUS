# Integridad del repositorio

## Manifiestos SHA-256

`manifests/` conserva la huella de los archivos publicados, para que cualquiera pueda comprobar que
lo que tiene es lo que se publicó.

```bash
bash tests/check_hashes.sh          # verifica el repositorio completo
python tests/generar_manifiesto.py  # regenera el manifiesto después de un cambio
```

Reglas:

- El manifiesto **no se incluye a sí mismo**: que el número de archivos en disco supere las líneas
  del manifiesto es lo esperado, no un fallo.
- La huella de un archivo de texto se calcula con los finales de línea normalizados y la de un
  binario sobre sus bytes: la misma regla en el generador y en el verificador, o la comprobación
  falla entera por un cambio de terminador de línea entre máquinas.
- Se regenera **después** de cada cambio publicado y se declara en `CHANGELOG.md`.

## Registro de experimentos

El registro de `experimentos/` fija qué se corrió y cuándo, con el hash de las entradas y de las
salidas. No publica el motor, los pesos ni los resultados: sirve para poder afirmar cuándo se hizo
algo y con qué, que es lo que hace verificable una prioridad.

## Qué se comprueba antes de cada publicación

1. Que no haya rutas absolutas ni nombre de usuario en el árbol (receta en `limpiar_rutas.txt`).
2. Que ninguna tabla contenga una fila por persona ni texto libre largo.
3. Que los conteos declarados en `data_spec/` coincidan con la base.
4. Que el manifiesto esté regenerado y la verificación pase.
