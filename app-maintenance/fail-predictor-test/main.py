from fail_predictor import FailPredictor

predictor = FailPredictor()
aq = int(input("Ingrese el valor de la Calidad del Aire (aq): "))
uss = int(input("Ingrese el valor del Ultrasonido (uss): "))
voc = int(input("Ingrese el valor del Compuesto Volatil Cercano (voc): "))
temperature = int(input("Ingrese el valor de la Temperatura: "))

fail = predictor.predict(aq, uss, voc, temperature)
print(f"El estado de la máquina resulta: {fail:.2f}")