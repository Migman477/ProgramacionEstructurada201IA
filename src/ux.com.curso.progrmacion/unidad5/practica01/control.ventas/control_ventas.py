

# ==================FUNCIONES==================

# Declaración de estructuras

productos = ["Laptop", "Smartphone", "Tablet"]

ventas = [[0] * 3 for _ in range(3)]

#obtener ventas de cada producto por día pidiendolas al usuario


def obtener_ventas():

    for i in range(3):

        print(f"--- Registro para {productos[i]} ---")

        for j in range(3):

            ventas[i][j] = int(input(f"Ventas del día {j+1}: "))

 

# Lectura de datos

def lectura_datos():

    for i in range(3):

        print(f"--- Registro para {productos[i]} ---")

        for j in range(3):

            ventas[i][j] = int(input(f"Ventas del día {j+1}: "))

    return ventas

 

# Escritura y Reporte

def reporte_ventas(ventas, productos):

    print("\nRESUMEN DE VENTAS")

    total_general = 0



    print("\nRESUMEN DE VENTAS")

    total_general = 0

    

    for i in range(3):

        suma_producto = sum(ventas[i])

        total_general += suma_producto

        print(f"{productos[i]}: {ventas[i]} | Total: {suma_producto}")

    

    print(f"\nEl total de ventas de la semana es: {total_general}")

    print(f"El promedio de ventas es: {total_general / 9:.2f}")

def producto_mas_vendido():

    max_ventas = 0

    producto_mas_vendido = ""

 

    for i in range(3):

        suma_producto = sum(ventas[i])

        if suma_producto > max_ventas:

            max_ventas = suma_producto

            producto_mas_vendido = productos[i]

 

    print(f"\nEl producto más vendido es: {producto_mas_vendido} con {max_ventas} ventas.")

def main():
    obtener_ventas()

    reporte_ventas(ventas, productos)

    producto_mas_vendido()
 

if __name__ == "__main__":

    main()