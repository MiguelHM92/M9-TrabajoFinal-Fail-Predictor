# M9-TrabajoFinal-Fail-Predictor
Predictor de fallas mecánicas de máquinas a partir de sus valores de funcionamiento - Trabajo Final Modulo 9

El Modelo fue elaborado a partir de una base de datos de parámetros de funcionamiento de diversas máquinas, que según sus valores se tiene registro de su estado como falla o no.

Por tanto, realizando un análisis correlacional de los valores de funcionamiento con el estado de la máquina, se seleccionó las variables con mejor coeficiente correlación para lograr predecir si la máquina fallará. Estas variables resultaron:

- Calidad del Aire (aq)
- Ultrasonido (uss)
- Compuesto Volátil Cercano (voc)
- Temperatura (Temperature)

Para este modelo se realizó un testeo con diversos modelos, resultando el más adecuado: Red Neural MLP.
