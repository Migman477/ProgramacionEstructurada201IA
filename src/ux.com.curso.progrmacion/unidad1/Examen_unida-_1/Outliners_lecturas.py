# Filtrado de Outliers en Sensores de Visión Computacional

import numpy as np

#Un sistema de percepción robótica toma 10 lecturas de confianza de un sensor de profundidad. Diseñar un algoritmo que calcule el promedio de las lecturas que se encuentren dentro del "Rango de Inferencia Válido" (entre 65% y 85% de precisión, ambos inclusive). Las lecturas fuera de este rango deben ser consideradas como ruido u outliers y deben ser ignoradas para el cálculo del promedio final.
def obtener_lecturas():
    lecturas = []
    for i in range(10):
        lectura = float(input(f"Ingrese la lectura {i+1} (en porcentaje): "))
        lecturas.append(lectura)
    return lecturas

def calcular_promedio_lecturas(lecturas):
    rango_inferencias_validas = [lectura for lectura in lecturas if lectura >= 65 and lectura <= 85]

    if len(rango_inferencias_validas) == 0:
        return "No hay lecturas válidas para calcular el promedio."

    promedio = np.mean(rango_inferencias_validas)
    return promedio

def main():
    lecturas = obtener_lecturas()
    resultado = calcular_promedio_lecturas(lecturas)
    print(f"El promedio de las lecturas válidas es: {resultado}")

if __name__ == "__main__":
    main()

