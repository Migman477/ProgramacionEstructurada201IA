#crear una funcion que liste las librerias en este codigo
import re
def listar_librerias(codigo):
    # Utilizamos una expresión regular para encontrar las líneas que importan librerías
    librerias = re.findall(r'^\s*(import|from)\s+(\w+)', codigo, re.MULTILINE)
    # Extraemos solo los nombres de las librerías
    nombres_librerias = [lib[1] for lib in librerias]
    return "Funciones Externas (Bibliotecas):\n" + "\n".join(nombres_librerias)