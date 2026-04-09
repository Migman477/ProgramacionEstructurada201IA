

UMBRAL_ALTO = 80.0 #(Confianza suficiente para actuar).
UMBRAL_MINIMO = 40.0 #(Confianza mínima para intentar sugerir algo).

def captura_datos():
    instruccion = input("Ingrese su instrucción: ")
    nivel_confianza = float(input("Ingrese el nivel de confianza (0-100): "))
    return instruccion, nivel_confianza

def evaluar_confianza(nivel_confianza,instruccion):

    if nivel_confianza >= UMBRAL_ALTO:
        print("Confianza alta. Procediendo con la acción.")
    elif nivel_confianza >= UMBRAL_MINIMO:
        print("Confianza moderada. Sugerencia: revise la instrucción antes de proceder.")
    else:
        print("Confianza baja. No se recomienda proceder con esta instrucción.")