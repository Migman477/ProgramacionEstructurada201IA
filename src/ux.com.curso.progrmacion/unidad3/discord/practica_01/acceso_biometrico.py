# --- SISTEMA DE CONTROL BIOMÉTRICO ---
print("--- SISTEMA DE CONTROL BIOMÉTRICO ---")

# Configuración de Variables (Simulación de Escaneo)
nombre = input("Nombre del Ingeniero: ")
id_empleado = int(input("ID de Empleado: "))

# Lectura de datos con limpieza .lower() integrada
iris_coincide = input("¿El escaneo de Iris coincide con la base de datos? (si/no): ").lower().strip()
facial_correcto = input("¿El reconocimiento facial es mayor al 95%? (si/no): ").lower().strip()

print("\n> Diagnóstico: ", end="")

# Lógica de Acceso (Estructuras Condicionales)
if id_empleado <= 0:
    # INTRUSO (Alarma)
    print("¡ALERTA DE SEGURIDAD! ID inválido detectado. Bloqueando accesos y notificando a la policía.")

elif iris_coincide == "si" and facial_correcto == "si":
    # Ambos escaneos son correctos, se evalúa el nivel por ID
    if id_empleado < 100:
        # ACCESO TOTAL
        print(f"Bienvenido, Ingeniero {nombre}. Acceso nivel SENIOR concedido a todas las áreas.")
    else:
        # ACCESO RESTRINGIDO
        print(f"Bienvenido, Ingeniero {nombre}. Acceso nivel JUNIOR concedido. Áreas de servidores restringidas.")
    
    # Reto Adicional: Generación de log si el acceso fue concedido
    print(f"Generando log de entrada para el usuario: {id_empleado}...")

else:
    # PROTOCOLO DE FALLO BIOMÉTRICO (ID válido pero al menos un escaneo falló)
    print("Error Biométrico: Identidad no verificada al 100%. Por favor, contacte a seguridad.")

def main():
    pass

if __name__ == "__main__":
    main()