
suma = 0

def calcular_suma():
    global suma
    while suma <= 500:
        numero = int(input("Ingrese un número: "))
        suma += numero
    return suma

def main():
   calcular_suma()

print(f"La suma de los números ingresados es: {calcular_suma()}")

if __name__ == "__main__":
    main()
    
