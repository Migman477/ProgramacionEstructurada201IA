#idenificadores validos
nombre_usuario = "Alumno" #inicia con letra y tiene guin bajo
sensor = "Temperatura" # Inicia con letra
_id_interno = 12 # puede contener guin bajo y numeros

#NOmbre correcto para funciones
"""
Imprime calcula el area
"""
def calcular_area ():
    print("Calculando el area...")

"""
Imprime los identificadores de usuario
"""

def imprimir_identificadores():

    print(nombre_usuario)
    print(sensor)
    print(_id_interno)

"""
Llama a las funciones de programa
"""

def main ():
    imprimir_identificadores()
    calcular_area()
"""
Llama a main
"""
if __name__ == "__main__":
    main()