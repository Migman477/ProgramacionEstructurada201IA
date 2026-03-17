
import math as m

#demostracion del uso de funcionws de math

def mostran_funciones_math(numero):


    #Calcular la raiz cuadrada
    sen_x = m.sin(numero)
    cos_x = m.cos(numero)

    print(f"El seno de {numero} es {sen_x}")
    print(f"El seno de {numero} es {sen_x}")

    resultado = cos_x**2 + sen_x**2

    print(f"El resultado de la suma de los cuadrados del sen y cos de ex es {resultado}")

def main ():

    numero = float(input("Ingrese in numero: "))
    mostran_funciones_math(numero)

if __name__ == "__main__":
    main()