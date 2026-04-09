

UMBRAL_ALTO = 80.0 #(Confianza suficiente para actuar).
UMBRAL_MINIMO = 40.0 #(Confianza mínima para intentar sugerir algo).

def captura_datos():
    instruccion = input("Ingrese su instrucción: ")
    nivel_confianza = float(input("Ingrese el nivel de confianza (0-100): "))
    return instruccion, nivel_confianza

def evaluar_confianza(nivel_confianza,instruccion):

    if nivel_confianza >= UMBRAL_ALTO:
        print(f"Ejecutando la acción: {instruccion}... (Éxito)")
    elif nivel_confianza >= UMBRAL_MINIMO and nivel_confianza < UMBRAL_ALTO:
        print(f"Confianza insuficiente. ¿Se refiere a: {instruccion}? Por favor confirme.")
    else:
        print("Error 404: No pude entender la instrucción. Intente hablar más claro.")

    if nivel_confianza >= 95.0:
        print("Aviso: El modelo ha sido reforzado con éxito debido a la alta precisión.")

    print("Sesion de procesamiento finalizada.")

def main():
    instruccion, nivel_confianza = captura_datos()
    evaluar_confianza(nivel_confianza,instruccion)

if __name__ == "__main__":
    main()


