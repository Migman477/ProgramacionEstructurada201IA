
def act2():
    N = input("Ingresa un número entero: ")
    factorial = 1
    i = 1

    while i <= int(N):
        
        factorial *= i
        i += 1

    return factorial

def main():
    print(f"El factorial del número ingresado es: {act2()}")

if __name__ == "__main__":
    main()