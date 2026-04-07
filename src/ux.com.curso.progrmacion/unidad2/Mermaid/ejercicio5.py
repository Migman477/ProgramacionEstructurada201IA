"""
Ejercicio 4: Suma de números hasta superar 500
Escribe un programa que solicite al usuario ingresar números enteros y los sume. El programa debe continuar solicitando números hasta que la suma total supere los 500.
Una vez que se alcance o supere ese límite, el programa debe mostrar la suma total de los números ingresados.
"""
suma = 0

def calcular_suma():
    global suma

    while True:

        numero = float(input("Ingrese un número: "))
        
        if numero >10 and numero <= 50:
            suma += numero
        else:
            break
    return suma
        

def main():
    calcular_suma()

print(f"La suma de los números ingresados es: {calcular_suma()}")

if __name__ == "__main__":
    main()