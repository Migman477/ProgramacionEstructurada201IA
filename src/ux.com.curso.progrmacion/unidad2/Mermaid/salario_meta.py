
def salario_meta():
    total_acumulado = 0
    semanas = 0
    meta = 2500

    while total_acumulado <= meta:
        salario_semanal = input("Ingrese el salario semanal: ")
        total_acumulado += float(salario_semanal)
        semanas += 1
    print(f"Semanas trabajadas: {semanas}, Total acumulado: {total_acumulado}")    

def main():
    salario_meta()
    
if __name__ == "__main__":
    main()