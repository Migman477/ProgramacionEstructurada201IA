def obtener_numeros():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    return a, b

def realizar_operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b

    return suma, resta, multiplicacion

def imprimir_resultados(suma, resta, multiplicacion):
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")  

def main():
    a, b = obtener_numeros()
    suma, resta, multiplicacion = realizar_operaciones(a, b)
    imprimir_resultados(suma, resta, multiplicacion)

if __name__ == "__main__":
    main()

