
def division_entera():
    dividendo = int(input("Ingrese el dividendo: "))
    divisor= int(input("Ingrese el divisor: "))
    resultado = 0

    if divisor == 0:
        print("Error: No se puede dividir por cero.")
        return

    while True:
        if dividendo >= divisor:
            dividendo -= divisor
            resultado += 1
        else:
            break
    
    print("El resultado de la división entera es:", resultado)
    print("El residuo de la división es:", dividendo)
            


def main():
    division_entera()

if __name__ == "__main__":
    main()