#Ejercicio de match por dias

def demstracion():
    print("--Ejemplo Match- Dias --")
    opcion = input("Ingrese una opcion (1-7)")

    match opcion:
        case"1":
            print ("Lunes")
        case"2":
            print ("Martes")
        case"3":
            print ("Miercoles")
        case"4":
            print ("Jueves")
        case"5":
            print ("Viernes")
        case"6":
            print ("Sabado")
        case"7":
            print ("Domingo")
  
        case _:
            print("Opcion no valida")

def main():
    demstracion()

if __name__ == "__main__":
    main()
