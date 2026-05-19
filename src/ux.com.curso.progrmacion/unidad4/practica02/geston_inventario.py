import re
def listar_librerias(codigo):
    # Utilizamos una expresión regular para encontrar las líneas que importan librerías
    librerias = re.findall(r'^\s*(import|from)\s+(\w+)', codigo, re.MULTILINE)
    # Extraemos solo los nombres de las librerías
    nombres_librerias = [lib[1] for lib in librerias]
    return "Funciones Externas (Bibliotecas):\n" + "\n".join(nombres_librerias)

import numpy as np
# 1. DEFINICIÓN DE UN VECTOR
# Precios de los productos: [Poción, Espada, Escudo]
precios = np.array([50, 150, 100])
# 2. DEFINICIÓN DE UNA MATRIZ
# Cantidades que tienen 3 usuarios diferentes
# Fila 0: Usuario A, Fila 1: Usuario B, Fila 2: Usuario C
inventarios = np.array([
 [5, 1, 0], # Usuario A: 5 pociones, 1 espada, 0 escudos
 [2, 0, 1], # Usuario B
 [10, 2, 2] # Usuario C
])
# 3. OPERACIONES SOBRE ARREGLOS
# Calcular cuánto dinero tiene cada usuario en objetos (Matriz x Vector)
riqueza_total = np.dot(inventarios, precios)
print("=== REPORTE DE ECONOMÍA DEL SERVIDOR ===")
print(f"Precios unitarios: {precios}")
print(f"Riqueza por usuario: {riqueza_total}")
print(f"El usuario más rico tiene: {np.max(riqueza_total)} monedas.")

def cambiar_precios(precios):
    """
    Crea una función que permita al "Administrador" (tú,
    por consola) cambiar el precio de las Espadas. El programa debe pedir el
    nuevo precio y actualizar el vector precios.
    """
    validacion = False

    val = input(f"¿Desea cambiar el precio de algún producto? (sí/no): ").lower()

    if val == "sí":
        validacion = True
    
    if validacion == True:
        variabe_cambio_precio = input(f"¿De que quiere cambiar el precio? (Poción, Espada, Escudo): ").lower()

        nuevo_precio = float(input(f"Ingrese el nuevo precio para las {variabe_cambio_precio} (actual: {precios[1 if variabe_cambio_precio == "espada" else (0 if variabe_cambio_precio == "poción" else 2)
        ]}): "))

        precios[1 if variabe_cambio_precio == "espada" else (0 if variabe_cambio_precio == "poción" else 2)
        ] = nuevo_precio
        return precios

def calcular_pociones_globales(inventarios):
    """
    Crea una función que calcule el total de pociones que hay en el servidor.
    """
    total_pociones = np.sum(inventarios[:, 0])  # Suma de la primera columna (pociones)
    return total_pociones

def felicitacion_riquesa(riqueza_total):
    """
    Muestra un mensaje especial si la riqueza total de un
    usuario supera las 500 monedas (usa un ciclo for para recorrer el arreglo
    riqueza_total).
    """
    for i, riqueza in enumerate(riqueza_total):
        if riqueza > 500:
            print(f"¡Felicitaciones, usuario {i+1}! Has alcanzado una riqueza de {riqueza} monedas.")

def matriz_identidad(inventarios):
    """
    Crea una función que genere una matriz identidad del mismo tamaño que el arreglo inventarios.
    """
    identidad = np.eye(inventarios.shape[0])  # Genera una matriz identidad del mismo tamaño que el número de filas de inventarios
    return identidad

def main():
    print("=== GESTIÓN DE INVENTARIO ===")
    print(f"Precios actuales: {precios}")
    precios_actualizados = cambiar_precios(precios)
    print(f"Precios actualizados: {precios_actualizados}")
    total_pociones = calcular_pociones_globales(inventarios)
    print(f"Total de pociones en el servidor: {total_pociones}")
    matriz_id = matriz_identidad(inventarios)
    print(f"Matriz identidad:\n{matriz_id}")
    felicitacion_riquesa(riqueza_total)

if __name__ == "__main__":
    main()