#imprimir las tablas de multplicar

def tabla_de_multiplicar():
    tabla_final  = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15\n"
    for numero in range(1, 16):
        tabla_final += f"{i} {numero}:\n"
        for i in range(1, 16):
            resultado = numero * i
            tabla_final += f"{numero} x {i} = {resultado}\n"
    print(tabla_final)

def main():
    tabla_de_multiplicar()

if __name__ == "__main__":
    main()