
def obtener_numeros():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    return a, b

def realizar_operaciones(a, b):
    division_entera = a//b

    division = a/b

    return division_entera, division

def main():
    a, b = obtener_numeros()
    division_entera, division = realizar_operaciones(a, b)
    print(f"División entera: {division_entera}")
    print(f"División: {division}")

if __name__ == "__main__":
    main()