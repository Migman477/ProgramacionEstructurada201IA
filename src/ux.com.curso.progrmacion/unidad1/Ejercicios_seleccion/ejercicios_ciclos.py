#Ejemplo de repeticion 
#imprimir numeros del 1 al 10 con for

def ejemplo_for():
    print("Estructura FOR")

    frutas = ["manzana", "banana", "naranja"]

    #For para iterar listas

    for fruta in frutas:
        print(fruta)
    
    #For para iterar rangos

    for i in range (1,5):
        print(i)

    #For para iterar rangos paso a paso (de dos en dos por ejeplo)

    for i in range (1, 10, 2):
        print(i)

#Ejemplo de While

def ejemplo_while():
    print("Estructura WHILE")

    contador = 0

    while contador < 5 :
        print(contador)
        contador +=1

#Ejemplo de Do While
def ejemplo_do_while ():
    print("Estritura  DO WHILE")

    secreto = "python12"
    intentos = 0

    while True:
        intentos_usuario = "python12" # Simulamos la entrada del usuario
        intentos += 1

        if intentos_usuario == secreto:
            print("¡Acceso concedido!")
            break
        else:
            print("¡Acceso denegado! Intenta de nuevo.")
            break
        print("\n")

def main ():
    ejemplo_for()
    ejemplo_while()
    ejemplo_do_while()

if __name__ == "__main__":
    main()       