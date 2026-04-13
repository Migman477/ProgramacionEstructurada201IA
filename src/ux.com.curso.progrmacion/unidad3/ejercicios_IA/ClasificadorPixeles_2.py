UMBRAL_ALTO = 0.7
UMBRAL_BAJO= 0.3

def clasificar_pixel(intensidad):

    #si la es menor a 0.0 y mayor a 1.0, es un valor no valido
    if intensidad < 0.0 or intensidad > 1.0:
        print("Valor no valido. La intensidad debe estar entre 0.0 y 1.0.")
        return 
    if 0.0 <= intensidad < UMBRAL_BAJO:
        return "Fondo oscuro"
        
    if UMBRAL_BAJO < intensidad < UMBRAL_ALTO:
        return "Gris (Ruido)"

    if intensidad >= UMBRAL_ALTO:
        print("Clasificacion (Objeto brillante)")
        return "Objeto brillante"
    
    print("Analisis de imagen finalizado")

import os

def cargar_y_procesar(nombre_archivo):
    datos_limpios = []
    ruido_detectado = 0
    fondo_oscuro = 0
    gris_ruido = 0
    objeto_brillante = 0

    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_script, nombre_archivo)

    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                valor_crudo = float(linea.strip())
                #clasificar el valor de pixel
                clasificacion = clasificar_pixel(valor_crudo)

                if clasificacion is None:
                    ruido_detectado += 1
                else:
                    datos_limpios.append(clasificacion)
                    if clasificacion == "Fondo oscuro":
                        fondo_oscuro += 1
                    elif clasificacion == "Gris (Ruido)":
                        gris_ruido += 1
                    elif clasificacion == "Objeto brillante":
                        objeto_brillante += 1
                          
    except FileNotFoundError:

        print(f"Error: El archivo '{nombre_archivo}' no se encontro.") 
    print("Resultados de clasificacion:")
    print(f"Ruido: {ruido_detectado}\n Fondo oscuro: {fondo_oscuro}\n Gris ruido {gris_ruido}\n Objeto brillante {objeto_brillante} ")                          

def main ():
    cargar_y_procesar("lecturas_sensores.txt")

if __name__ == "__main__":
    main()