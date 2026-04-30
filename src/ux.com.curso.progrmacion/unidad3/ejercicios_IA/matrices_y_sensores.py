# --- PARTE 1: El Vector de Proximidad (1D) ---
print("--- MÓDULO DE SENSORES (VECTORES) ---")
sensores_distancia = []

for i in range(3):
    distancia = float(input(f"Ingrese distancia sensor {i + 1}: "))
    sensores_distancia.append(distancia)

promedio_proximidad = sum(sensores_distancia) / len(sensores_distancia)

# Determinamos el estado basado en el promedio
estado = "Seguro" if promedio_proximidad >= 2.0 else "Aviso: Reduciendo velocidad global"
print(f"Promedio de proximidad: {promedio_proximidad:.1f}m. Estado: {estado}.")



print("\n--- MÓDULO DE VISIÓN (MATRICES) ---")
print("Llenando matriz de cámara 3x3:")

# Inicializamos la matriz 3x3
camara_ia = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for fila in range(3):
    for col in range(3):
        brillo = int(input(f"Fila {fila}, Col {col} (Brillo 0-255): "))
        
      
        if brillo > 255:
            brillo = 255
        elif brillo < 0:
            brillo = 0
            
        camara_ia[fila][col] = brillo


print("\nVisualización de la imagen capturada:")
for fila in camara_ia:
  
    contenido = "  ".join(f"{pixel:<3}" for pixel in fila)
    print(f"[ {contenido} ]")


puntos_brillantes = 0

for fila in range(3):
    for col in range(3):
        if camara_ia[fila][col] > 200:
            puntos_brillantes += 1

print("\nResultado de Análisis IA:")
print(f"Se detectaron {puntos_brillantes} píxeles de alta intensidad.")