# Calculo de identidad trigonometrica
import math

def identidad_trigonometrica(x):
    
    numero_radianes = math.radians(x)

    seno_x = math.pow(math.sin(numero_radianes), 2)
    coseno_x = math.pow(math.cos(numero_radianes), 2)
    identidad = seno_x + coseno_x
    return identidad

def main():
     x = float(input("Ingrese el valor de x en grados: "))
     identidad = identidad_trigonometrica(x)
    
     print("La identidad trigonometrica para x =", x, "es:", identidad)

if __name__ == "__main__":
    main()