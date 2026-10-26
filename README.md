# GGM Small-n — Redes psicométricas en muestras pequeñas

![Estado: investigación en proceso](https://img.shields.io/badge/estado-investigaci%C3%B3n%20en%20proceso-orange)
![Datos: no incluidos](https://img.shields.io/badge/datos-no%20incluidos-lightgrey)

Material de investigación para estimar y **decidir** en redes gaussianas gráficas cuando el
cociente entre observaciones y variables es desfavorable, con el trastorno por consumo de
sustancias (TUS) como banco de pruebas clínico.

> Investigación en proceso. Este repositorio publica la especificación de los datos, la
> documentación metodológica, el registro de experimentos, los resultados abiertos de simulación
> sintética y las huellas de integridad. **No** incluye el motor de estimación completo, el
> manuscrito ni datos de personas.

## Qué contiene

- **`data_spec/`** — qué instrumentos y variables existen, con los recuentos confirmados contra la
  base pseudonimizada.
- **`docs/`** — metodología (diseño de simulación y calibración, esta última sin sus valores),
  gobernanza del registro, integridad, decisiones metodológicas y plan de publicaciones.
- **`code/`** — las **características** del motor: qué recibe, qué devuelve, qué familias
  implementa y qué se reserva hasta la publicación. El código de producción se incorpora tras la
  publicación del artículo.
- **`experimentos/`** — el diario de laboratorio (`entradas/`) y el registro tabular (`registro.csv`)
  de las corridas cerradas (EXP-015, EXP-017, EXP-018, EXP-019): qué se corrió, cuándo, con qué
  entradas y su estado.
- **`manifests/`** — huellas criptográficas SHA-256 de todo el árbol publicado.
- **`results/`** — tablas cuantitativas derivadas sin identificadores personales:
  - `results/simulacion/`: resultados brutos de simulación sintética de EXP-018 (MPM bayesiano) y
    EXP-019 (calibración EBIC).
- **`tests/`** — el generador de manifiestos, el verificador de hashes y la suite de pruebas
  de reproducibilidad científica (`verificar_experimentos.py`).

## Estructura

```
code/            características del motor (el código de producción, tras la publicación)
data_spec/       codebook y convenciones: instrumentos, variables, llaves, valores ausentes
docs/            metodología, gobernanza, integridad, decisiones, plan de publicaciones
  metodologia/     diseño de simulación y calibración (estructura, sin valores)
experimentos/    diario de laboratorio (entradas/) y registro tabular de corridas (registro.csv)
manifests/       huellas SHA-256 de lo publicado
results/         tablas derivadas abiertas sin datos personales (results/simulacion/)
tests/           generar_manifiesto.py · check_hashes.sh · verificar_experimentos.py
```

## Qué se mide, y qué se puede concluir

- El proyecto estudia **cuándo el procedimiento estándar falla** al estimar una red con pocas
  observaciones, y cómo decidir en consecuencia. Un resultado que aquí importa es la **tasa de
  redes vacías**: un método que devuelve una red vacía no falla en silencio, falla de forma
  medible.
- Con datos clínicos reales **no se puede hablar de recuperación estructural**: no existe grafo
  verdadero. Eso se sostiene con simulación, y así se declara en cada tabla.
- Las dos fases son **muestras distintas con propósitos distintos**: la de simulación prueba
  propiedades del motor; las clínicas describen una población. Las cifras de una no son las de la
  otra y no se suman.

## Cómo se reproduce

1. El código de producción se incorpora cuando el artículo esté publicado; mientras tanto, este
   repositorio permite auditar **qué** se hizo, **cuándo** y con qué estado, sosteniendo la
   trazabilidad.
2. Los datos clínicos viven fuera del repositorio. Ver `docs/NOTA_sobre_los_datos.md`.
3. Los resultados de simulación sintética pueden verificarse directamente con la suite automatizada:

```bash
python tests/verificar_experimentos.py
```

4. La integridad criptográfica de todos los archivos del repositorio se audita con:

```bash
bash tests/check_hashes.sh
```

Para regenerar el manifiesto después de una modificación controlada:

```bash
python tests/generar_manifiesto.py
```

## Datos no incluidos

Ningún dato de personas, ni pseudonimizado. La base clínica vive fuera del repositorio y su acceso se
solicita al comité de ética del proyecto. Los conteos por instrumento están en
`data_spec/codebook.md`; las condiciones de acceso, en `docs/NOTA_sobre_los_datos.md`.

## Cita

Ver `CITATION.cff`.

## Licencia

MIT para el material de este repositorio (ver `LICENSE`).
