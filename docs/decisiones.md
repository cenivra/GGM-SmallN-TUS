# Decisiones

Convención: fecha ISO, la decisión, la alternativa considerada y el criterio. Se registran las
decisiones que cambian el análisis o la publicación, no las de formato.

## 2026-09-27 — El repositorio no incluye el motor, ni el manuscrito, ni los datos

- **Decisión**: el repositorio publica características del motor, especificación de datos,
  documentación, registro de experimentos y manifiestos; no publica el código, ni el manuscrito,
  ni ningún dato de personas.
- **Alternativa considerada**: publicar el motor desde el inicio (más útil para terceros, y la
  práctica habitual en repositorios de métodos).
- **Criterio**: el motor y su calibración son la contribución del artículo en preparación. Se
  publican cuando el artículo esté publicado, de modo que la evidencia sea atribuible a una versión
  concreta y sin anticipar el contenido.

## 2026-09-27 — Los valores de calibración se reservan

- **Decisión**: los cortes de los regímenes y los valores de los hiperparámetros no se publican en
  el repositorio.
- **Alternativa considerada**: publicarlos con la documentación (son, por sí solos, poco útiles sin
  el motor).
- **Criterio**: con el motor publicado serían reproducibles de inmediato. La calibración es una
  contribución, no un detalle de implementación.

## 2026-09-27 — El repositorio se publica privado

- **Decisión**: privado mientras el artículo no esté enviado.
- **Criterio**: el material de proceso y los avances previos al envío no se exponen; el registro de
  experimentos y los manifiestos ya fijan la trazabilidad.

## 2026-10-25 — Adopción del Modelo de Probabilidad Mediana (PPI >= 0.50) en estimación bayesiana

- **Decisión**: sustituir la regla de selección modal MAP (*Maximum A Posteriori*) por el Modelo de Probabilidad Mediana ($PPI \ge 0.50$, Barbieri & Berger, 2004) como criterio de inclusión de aristas en las cadenas MCMC de `BDgraph`.
- **Alternativa considerada**: mantener MAP o aplicar umbrales marginales más liberales ($PPI \ge 0.40$) o conservadores ($PPI \ge 0.60$).
- **Criterio**: en muestras ultra-pequeñas ($n=15$), la masa posterior de grafos está dispersa; MAP selecciona aristas con baja frecuencia marginal, deprimiendo la precisión al $9.8\%$. El corte $PPI \ge 0.50$ reduce sustancialmente los falsos descubrimientos (+30.8% a +45.2% de precisión) manteniendo cero colapsos a redes vacías (0.0%).

## 2026-10-25 — Descontinuación de la penalización asintótica gamma = 0.50 para n <= 30 en EBIC

- **Decisión**: no utilizar EBICglasso con $\gamma = 0.50$ en regímenes de muestra pequeña ($n \le 30$).
- **Alternativa considerada**: calibrar el umbral numérico de poda post-hoc ($|r| > 0.08 \to 0.00$).
- **Criterio**: la experimentación controlada (EXP-019) demostró invarianza idéntica entre umbrales post-hoc ($81.67\%$ de redes vacías en todas las condiciones de umbral). El colapso es causado directamente por la penalización combinatoria $4\gamma |E| \log(p)$ en la función objetivo EBIC, que domina sobre la log-verosimilitud en muestras pequeñas y fuerza la selección de la red vacía.
