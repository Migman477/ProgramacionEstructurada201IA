"""
Ejercicio: Validación de Contraseña
Escribe un programa que solicite al usuario que ingrese una contraseña.
El programa debe permitir al usuario ingresar la contraseña hasta tres veces.
Si el usuario ingresa la contraseña correcta, el programa debe mostrar un mensaje de "Acceso concedido".
"""
def validar_contrasena():
    intentos = 0
    clave_correcta = "1234"

    while intentos < 3:
        contrasena = input("Ingrese la contraseña: ")
        if contrasena == clave_correcta:
            print("Acceso concedido.")
            return True
        else:
            intentos += 1
            if intentos < 3:
                print("Contraseña incorrecta. Intente nuevamente.")
    print("Cuenta bloqueada. Demasiados intentos fallidos.")
    return False
    
def main():
    validar_contrasena()

if __name__ == "__main__":
    main()  