#Ejemplo para visualizar la identacion en python

def explicar_identacion():
    #nivel 1
    mensaje = "Nivel 1 de identacion"
    print(mensaje)

    puntos = 10

    if puntos > 9:
        #Nivel 2
        print("Entra al flujo del if")

        if puntos == 10:
            #Nivel 3
            print("Puntos = 10")

    #Cierra Nivel 1

def main ():
    explicar_identacion()

if __name__ == "__main__":
    main()    
