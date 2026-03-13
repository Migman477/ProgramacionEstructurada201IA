#Programa para dicernir Calificaciones

def asignar_calificaciones ():
    calificacion = int(input("Ingresa tu calificacion: "))

    if calificacion >= 90:
        print("Tu calificacion es A")

    elif calificacion >=80 and calificacion <90:
        print("Tu calificacion es B")
    
    elif calificacion >=70 and calificacion <80:
        print("Tu calificacion es C")
    
    elif calificacion == 69:
        print("Tu calificacion es D")
    
    else:
        print("Tu calificacion es F")

def main():
    asignar_calificaciones()

if __name__ == "__main__":
    main()
        
