#Piloto automático para un vehículo
distancia_objeto = float(input("Ingrese la distancia al objeto mas cercano (en metros): "))
color_semaforo = input("Ingrese el color del semaforo (rojo, amarillo, verde): ").lower()
peaton_cruzando = input("¿Hay un peatón cruzando? (si/no): ").lower()

def navegacion(distancia, color, peaton):

    if distancia < 5 or peaton:
        print("¡FRENO DE EMERGENCIA ACTIVADO! Deteniendo el vehículo inmediatamente.")
        
    
    if color == "rojo":
        print("Estado: Detenido. Esperando luz verde.")
        
    elif color == "amarillo":
        print("Estado: Precaución. Reduciendo velocidad para detenerse.")
        
    
    elif color == "verde" and distancia >= 5:
        print("Estado: En movimiento. Todo despejado para avanzar.")

    if color not in ["rojo", "amarillo", "verde"]:
        print("Error de lectura en sensores: Color de semáforo no reconocido.")       
    
    print("Condiciones normales. Continuando la marcha.")
    
