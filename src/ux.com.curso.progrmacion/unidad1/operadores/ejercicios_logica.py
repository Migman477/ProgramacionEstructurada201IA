#Ejercicios de operadres logica
def operadores ():

    a = True
    b = False

    print(a and b)
    print(a or b)
    print(not a)
    print(not b)

    numero_1 = 10
    numero_2 = 20

    if numero_1 > numero_2:
        print("Numero 1 es mayor que Numero 2")

    else:
        print("Numero 2 mayor que Numero 1")

def main():
    operadores()

if __name__ == "__main__":
    main()