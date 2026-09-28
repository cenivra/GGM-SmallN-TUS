# Manifiestos

Huellas SHA-256 de los archivos publicados, para que cualquiera pueda comprobar que lo que tiene
es lo que se publicó y en qué versión.

| archivo | contenido |
|---|---|
| `SHA256_REPO.txt` | huella de cada archivo versionado (excepto el propio manifiesto) |
| `INVENTARIO_ARCHIVOS.csv` | ruta, bytes y fecha de cada archivo |

## Cómo se generan y se verifican

```bash
python tests/generar_manifiesto.py     # regenerar (después de un cambio publicado)
bash   tests/check_hashes.sh           # verificar
```

Se regeneran después de cada cambio material y se anota en `CHANGELOG.md`. El manifiesto no se
incluye a sí mismo.
