#Limpieza de datos
UMBRAL_ALTO = 0.7
UMBRAL_BAJO= 0.3

def clasificar_pixel():

    #Solicitar datos al usuario
    intensidad = float(input("Ingrese la intensidad del pixel (0.0 a 1.0): "))

    #si la es menor a 0.0 y mayor a 1.0, es un valor no valido
    if intensidad < 0.0 or intensidad > 1.0:
        print("Valor no valido. La intensidad debe estar entre 0.0 y 1.0.")
        return
    if 0.0 <= intensidad < UMBRAL_BAJO:
        print("Clasificacion (Fondo oscuro)")
        return
    if UMBRAL_BAJO < intensidad < UMBRAL_ALTO:
        print("Clasificacion (Fondo gris)")

    if intensidad >= UMBRAL_ALTO:
        print("Clasificacion (Objeto brillante)")
        return
    
    print("Analisis de imagen finalizado")

def main():
    clasificar_pixel()

if __name__ == "__main__":
    main()