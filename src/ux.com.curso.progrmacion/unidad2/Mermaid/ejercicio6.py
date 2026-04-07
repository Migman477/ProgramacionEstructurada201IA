"""
Ejercicio 3: Ahorro de meta
Escribe un programa que simule el proceso de ahorro para alcanzar una meta financiera.
El programa debe permitir al usuario ingresar depósitos hasta que alcance o supere la cantidad objetivo.
Al final, muestra el saldo total y un mensaje de felicitación.
"""
def fondos():

    saldo = 0
    meta = 1000

    while saldo < meta:
        deposito = float(input("Ingrese el monto del depósito: "))
        saldo += deposito
    print(f"El saldo total es: {saldo}")
    print("¡Felicidades! Has alcanzado tu meta de ahorro.")

def main():
    fondos()

if __name__ == "__main__":
    main()