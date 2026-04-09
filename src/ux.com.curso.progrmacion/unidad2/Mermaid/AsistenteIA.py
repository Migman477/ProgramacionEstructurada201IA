

UMBRAL_ALTO = 80.0 #(Confianza suficiente para actuar).
UMBRAL_MINIMO = 40.0 #(Confianza mínima para intentar sugerir algo).

def captura_datos():
    instruccion = input("Ingrese su instrucción: ")
    nivel_confianza = float(input("Ingrese el nivel de confianza (0-100): "))
    return instruccion, nivel_confianza