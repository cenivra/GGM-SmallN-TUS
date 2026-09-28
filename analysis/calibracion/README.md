# Calibración por régimen

La calibración fija los hiperparámetros en función del régimen n/p, en lugar de usar un valor
único para todos los conjuntos de datos. La tabla vigente (datos continuos):

| n/p | banda | gamma | lambda | umbral | estrategia |
|---|---|---|---|---|---|
| 1.00 | ultracrítico | 0.50 | 0.500 | 0.060 | ultra_conservadora |
| 2.00 | crítico | 0.50 | 0.350 | 0.080 | ultra_conservadora |
| 3.00 | difícil | 0.30 | 0.150 | 0.100 | crítica |
| 5.00 | moderado | 0.15 | 0.050 | 0.120 | moderada |
| 8.00 | conservador | 0.10 | 0.010 | 0.150 | conservadora |
| 15.00 | estándar | 0.00 | 0.001 | 0.180 | estándar |

Con datos ordinales se aplica el ajuste declarado (×1.2, ×1.3 y ×0.9 según el caso).

Las bandas son una **sola definición** para el documento y para el código: la función que las
implementa es la misma que se cita en el manuscrito. Cualquier cambio aquí invalida la tabla del
artículo y obliga a regenerarla.
