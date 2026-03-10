#Desarrollo de algoritmos Contador de positivos

#Declaracion de variables
"""
Esta Funcion inicia con el contador igual a 0
 le pide al usuario que ingrese un numero postivo y si inserta un numero negativo el bucle termina
"""
def contador_positivos():
    contador = 0
    while True:
        numero = int(input("Ingrese u numero (-1 para terminar): "))
        if numero<0:
            break
        contador +=1
    print("Cantidad de numeros positivos ingresados: ", contador)

#Definicion de la funcion Main

"""
Funcion Main 
DA un mensaje de bienvenida y llama a la fucion 
contador_positivos
"""

def main():
    print("Bienvenido al contador de positivos")
    contador_positivos()

#Llamada a la funcion main

"""
Mantiene main activa mientras el programa se este ejecutando
"""

if __name__ == "__main__":
    main()
    
