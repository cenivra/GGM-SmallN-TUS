# Seguridad y datos sensibles

## Qué no debe aparecer nunca

- Datos de pacientes, pseudonimizados o no, en cualquier formato.
- Credenciales, claves de API o rutas con nombre de usuario.
- Hojas de cálculo de captura o cualquier archivo con identificadores.

## Cómo reportar

Si encuentras datos de personas o credenciales en el repositorio, no abras un *issue* público:
informa directamente a la persona responsable del proyecto. Un issue público deja constancia
permanente y difunde lo que hay que retirar.

## Si ya se publicó

Lo primero es medir la exposición antes de decidir, y lo reversible primero (cambiar la
visibilidad del repositorio) antes que lo costoso (reescribir la historia). Retirar un archivo en
un commit posterior **no** lo borra: el contenido sigue alcanzable en la historia.
