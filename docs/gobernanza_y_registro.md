# Gobernanza y registro experimental

El proyecto se apoya en un **registro que se escribe antes y después de cada corrida**, para que
un resultado sea auditable sin depender de la memoria de quien lo corrió.

## Qué registra cada experimento

- **Identificador estable** (`EXP-###`): se asigna una vez y no se reutiliza.
- **Estado de ejecución** (terminó bien, red vacía, falló) separado del **estado de registro**
  (si el asiento quedó completo). Un fallo registrado es un dato; un fallo sin registrar es un
  hueco.
- **Artefactos** con identificador estable (`ART-###`), con su hash, incluso cuando un artefacto
  se elimina después (se conserva la lápida en vez de reutilizar el identificador).
- **Antes y después** de la sesión: qué archivos cambiaron (`NEW` / `MODIFIED` / `UNCHANGED` /
  `DELETED`) y el estado del entorno, para que la corrida sea reconstruible.
- **Decisiones**: un archivo por decisión con su alternativa considerada, su criterio y su fecha.

## Reglas de la casa

- La separación entre lo **interno** (cómo trabajamos, qué se decidió) y la **evidencia externa**
  (lo que dice una fuente publicada) se mantiene en todos los documentos: las reglas del proyecto
  no se citan como hallazgos, y ninguna afirmación atribuida a un artículo se sostiene sin haber
  visto ese artículo.
- Las notas de auditoría no se convierten en secciones del producto auditado.
- Ninguna función se escribe sin llamarse, y ninguna línea se elimina sin declararlo: se añade, y
  si algo no encaja se marca para revisión.
