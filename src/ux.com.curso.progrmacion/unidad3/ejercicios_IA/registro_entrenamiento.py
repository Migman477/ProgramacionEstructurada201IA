class MonitorEntrenamiento:
    def __init__(self, umbral_convergencia=0.01):
        self.historial_errores = []
        self.umbral_convergencia = umbral_convergencia

    def registrar_epoca(self, valor_error):
        # Agregamos el valor al historial
        self.historial_errores.append(valor_error)
        print("> Registro exitoso.")
        
        # Verificamos si se alcanzó el umbral
        if valor_error < self.umbral_convergencia:
            print(f"[SISTEMA] Entrenamiento completado: Se alcanzó el objetivo de precisión.")
            return True # Retornamos True para indicar convergencia
        return False

# --- Flujo Principal ---
monitor = MonitorEntrenamiento(umbral_convergencia=0.01)

print("--- Iniciando Monitor de Red Neuronal ---")

epocas_a_registrar = 5
contador = 1

while contador <= epocas_a_registrar:
    try:
        entrada = input(f"Ingrese el error de la Época {contador}: ")
        valor_error = float(entrada)

        if valor_error < 0:
            print("> [ERROR] El error no puede ser un número negativo.")
            continue # Reintenta la misma época

        # Registramos y verificamos convergencia
        alcanzo_objetivo = monitor.registrar_epoca(valor_error)
        
        contador += 1
        
        if alcanzo_objetivo:
            break

    except ValueError:
        print("> [ERROR] Entrada inválida. Por favor, ingrese un número decimal.")

# --- Análisis de Datos Final ---
if monitor.historial_errores:
    print("\n--- Resumen de Entrenamiento ---")
    print(f"Historial: {monitor.historial_errores}")
    
    promedio = sum(monitor.historial_errores) / len(monitor.historial_errores)
    mejor_error = min(monitor.historial_errores)
    
    print(f"Promedio de Error: {promedio:.4f}")
    print(f"Mejor resultado obtenido: {mejor_error}")
else:
    print("\nNo se registraron datos válidos.")