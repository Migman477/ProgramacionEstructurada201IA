#Desarrollo de algoritmos Contador de positivos

#Declaracion de variables

def contador_positivos():
    contador = 0
    while True:
        numero = int(input("Ingrese u numero (-1 para terminar): "))
        if numero<0:
            break
        contador +=1
    print("Cantidad de numeros positivos ingresados: ", contador)

#Definicion de la funcion Main

def main():
    print("Bienvenido al contador de positivos")
    contador_positivos()

#Llamada a la funcion main

if __name__ == "__main__":
    main()
    
