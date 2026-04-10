#Calculo del radio de una esfera

import math

def define_esfera():
    radio = float(input("Ingrese el radio de la esfera: "))
    
    volume = (4/3) * math.pi * pow(radio, 3)

    return volume

def main():
    volume = define_esfera()
    print("El volumen de la esfera es:", volume)

if __name__ == "__main__":
    main()









