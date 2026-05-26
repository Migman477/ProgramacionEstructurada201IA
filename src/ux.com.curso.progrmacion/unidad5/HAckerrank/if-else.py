
def obtener_numero():

    numero = int(input("Ingrese un número: "))
    return numero

def evaluar_numero(numero):

    if numero % 2 == 0 and numero >= 2 and numero <= 5:
        print("Not Weird")
    
    elif numero % 2 == 0 and numero >= 6 and numero <= 20:
        print("Weird")
    
    elif numero % 2 == 0 and numero > 20:
        print("Not Weird")
    else:
        print("Weird")

def main():
    numero = obtener_numero()
    evaluar_numero(numero)

if __name__ == "__main__":
    main()