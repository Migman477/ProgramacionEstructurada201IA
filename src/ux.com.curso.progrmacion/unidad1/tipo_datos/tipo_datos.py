#Demomstracion tipos de datos


def datos ():
    entero = 23
    decimal = 3.14
    cadena = "Hola, mundo"
    booleano = True

    print(entero)
    print(decimal)
    print(cadena)
    print(booleano)

def tipos_datos_compuestos ():
    lista = [10,20,3,40]
    tupla = (19,29,39,49)
    diccionarios = {"nombre": "Juan","edad": 30, "ciudad": "Madrid"}

    print(lista)
    print(tupla)
    print(diccionarios)


def main ():

    datos()

if __name__ == "__main__":
    main()