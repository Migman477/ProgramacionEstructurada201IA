
def depostos():
    saldo = 0
    meta = 1000

    while saldo < meta:
        deposito = float(input("Ingrese el monto del depósito: "))
        saldo += deposito
    
    print(f"¡Meta alcanzada! El saldo total es: {saldo}")

def main():
    depostos()

if __name__ == "__main__":
    main()