# Pruebas

Dos cosas distintas conviven aquí:

1. **Integridad del repositorio**: `generar_manifiesto.py` y `check_hashes.sh`, que producen y
   verifican las huellas SHA-256 de `manifests/`.
2. **Pruebas del sistema de registro** (cuando el código se publique): apertura y cierre de una
   corrida, estabilidad de identificadores, detección de artefactos nuevos, modificados y
   eliminados, y el caso de fallo controlado.

## Regla

Un cambio en una prueba es un cambio de comportamiento y se revisa como tal: quitar una aserción
de forma debilita la garantía, y publicar así es publicar una garantía que ya no se sostiene.
