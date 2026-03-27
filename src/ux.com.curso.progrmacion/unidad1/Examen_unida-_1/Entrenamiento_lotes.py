#Simulación de entrenamiento por lotes con límite de memoria RAM .31336..
# El programa solicita al usuario que ingrese el peso de cada lote en MB y acumula el peso total. Si el peso total supera los 2500 MB, se muestra un mensaje de "Out of memory" y el programa termina.
def obtener_lotes():
    V_RAM = 0
    while V_RAM <= 2500:
        tensor = float(input("ingresa el peso del lote en  MB: "))
        V_RAM = V_RAM + tensor

        if V_RAM > 2500:
            print("Out of memory")
            break
        
        
def main():
    obtener_lotes()

if __name__ == "__main__":
    main()