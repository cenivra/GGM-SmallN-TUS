# Pruebas

Pruebas del sistema de registro experimental, que es la parte del proyecto cuya corrección no se
puede verificar leyendo: un registrador que pierde un asiento o reutiliza un identificador produce
evidencia que parece buena y no lo es.

Cubre: apertura y cierre de una corrida, asignación y estabilidad de identificadores, detección de
artefactos nuevos, modificados, sin cambios y eliminados, escritura del asiento con el estado de
ejecución, y el caso de fallo con su aviso.

## Regla

Un cambio en una prueba es un cambio de comportamiento y se revisa como tal: quitar una aserción
de forma debilita la garantía, y publicar así es publicar una garantía que ya no se sostiene.
