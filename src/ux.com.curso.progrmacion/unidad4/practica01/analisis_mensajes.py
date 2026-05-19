#crear una funcion que liste las librerias en este codigo
import re
import numpy as np


def listar_librerias(codigo):
    # Utilizamos una expresión regular para encontrar las líneas que importan librerías
    librerias = re.findall(r'^\s*(import|from)\s+(\w+)', codigo, re.MULTILINE)
    # Extraemos solo los nombres de las librerías
    nombres_librerias = [lib[1] for lib in librerias]
    return "Funciones Externas (Bibliotecas):\n" + "\n".join(nombres_librerias)

# 1. IMPORTACIÓN
# Importamos la biblioteca externa y le asignamos un alias 'np' para facilitar su uso

def procesar_estadisticas(lista_mensajes):
 """
 Función que recibe datos y utiliza funciones externas de
 la biblioteca NumPy para procesarlos.
 """
 # Invocación de función externa para el promedio
 promedio = np.mean(lista_mensajes)

  # Invocación de función externa para encontrar el valor máximo
 pico_maximo = np.max(lista_mensajes)

 # Invocación de función externa para la desviación estándar
 desviacion = np.round(np.std(lista_mensajes), 1)

 mediana = np.median(lista_mensajes)

 return promedio, pico_maximo, desviacion, mediana
# --- Programa Principal ---
# Datos: Mensajes enviados cada hora durante un turno de 8 horas
datos_servidor = [15, 42, 88, 30, 120, 55, 72, 20]
# Llamada a nuestra función enviando los parámetros de entrada
prom, maximo, ds , mediana = procesar_estadisticas(datos_servidor)
print("=== REPORTE DE ACTIVIDAD DEL SERVIDOR ===")
print(f"Promedio de mensajes por hora: {prom:.2f}")
print(f"Pico de actividad registrado: {maximo} mensajes")
print(f"Variabilidad del tráfico (Desviación): {ds:.2f}")
print(f"Mediana del tráfico: {mediana}")

"""
Si eliminas la importaciond e Numpy saltara un name error ya que no esta definido
"""
