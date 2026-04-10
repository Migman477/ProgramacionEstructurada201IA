"""
# Filtro de seguridad para datos de sensores térmicos
Este programa simula un filtro de seguridad para datos provenientes de sensores térmicos.
"""


def FILTRO():
    LIMITE_SUPERIOR = 100.0
    LIMITE_INFERIOR = 0.0

    LECTURA = float(input("Ingrese la lectura del sensor termico: "))

    if LECTURA >= LIMITE_INFERIOR and LECTURA <= LIMITE_SUPERIOR:
        DATO_NORMALIZADO = LECTURA / LIMITE_SUPERIOR
        print("!Señal aceptada¡ valor normalizado para el modelo: ", DATO_NORMALIZADO)
    
    else:
        print("!Error¡: Lectura fuera de rango. La señal se considera ruido.")
    
    print("Fin del proceso de filtrado de datos")

    return LECTURA

def main():
    FILTRO()

if __name__ == "__main__":
    main()