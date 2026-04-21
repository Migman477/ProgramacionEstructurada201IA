def validar_fecha():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))

    if año >= 0:
        if 1 <= mes <= 12:
            if dia <= 31:
                if mes == 2:
                    if año % 4 == 0:
                        if dia <= 29:
                            print("La fecha es válida.")
                        else:
                            print("La fecha no es válida.")
                    else:
                        if dia <= 28:
                            print("La fecha es válida.")
                        else:
                            print("La fecha no es válida.")
                else:
                    if mes % 2 == 0:
                        if dia <= 30:
                            print("La fecha es válida.")
                        else:
                            print("La fecha no es válida.")
                    else:
                        if dia <= 31:
                            print("La fecha es válida.")
                        else:
                            print("La fecha no es válida.")
            else:
                print("La fecha no es válida.")
        else:
            print("La fecha no es válida.")
    else:
        print("La fecha no es válida.")

def main():
    validar_fecha()

if __name__ == "__main__":
    main()