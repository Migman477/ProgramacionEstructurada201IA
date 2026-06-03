"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte II)
Alumno: Miguel German Cruz Maillard
"""
import random
import statistics  # Librería estándar añadida para cálculos estadísticos

# =====================================================================
# RETO 1: Formateador de Nombres de Usuario para Discord
# Sentido: Asegurar que los nombres en la base de datos no tengan espacios
#          extras y que inicien con mayúscula (Formato Limpio).
# =====================================================================
def limpiar_nombre_usuario(nombre_sucio):
    nombre_sin_espacios = ""
    inicio = 0
    fin = len(nombre_sucio) - 1
    
    while inicio <= fin and nombre_sucio[inicio] == " ":
        inicio += 1
    while fin >= inicio and nombre_sucio[fin] == " ":
        fin -= 1
        
    for i in range(inicio, fin + 1):
        nombre_sin_espacios += nombre_sucio[i]
        
    if len(nombre_sin_espacios) > 0:
        primera_letra = nombre_sin_espacios[0]
        if 'a' <= primera_letra <= 'z':
            primera_letra = chr(ord(primera_letra) - 32)
            
        resto_cadena = ""
        for i in range(1, len(nombre_sin_espacios)):
            caracter = nombre_sin_espacios[i]
            if 'A' <= caracter <= 'Z':
                caracter = chr(ord(caracter) + 32)
            resto_cadena += caracter
            
        return primera_letra + resto_cadena
    return ""

def limpiar_nombre_usuario_factorizado(nombre_sucio):
    # Uso de métodos nativos de cadenas (strings) integrados en Python
    return nombre_sucio.strip().capitalize()

# =====================================================================
# RETO 2: Buscador de Palabras Prohibidas (Filtro contra Groserías)
# Sentido: Banear o censurar mensajes inapropiados en el chat del servidor.
# =====================================================================
def contiene_palabra_bloqueada(mensaje_chat, palabra_prohibida):
    largo_mensaje = len(mensaje_chat)
    largo_palabra = len(palabra_prohibida)
    
    for i in range(largo_mensaje - largo_palabra + 1):
        coincidencia = True
        for j in range(largo_palabra):
            if mensaje_chat[i + j] != palabra_prohibida[j]:
                coincidencia = False
                break
        if coincidencia:
            return True
            
    return False

def contiene_palabra_bloqueada_factorizado(mensaje_chat, palabra_prohibida):
    # El operador 'in' evalúa la existencia de subcadenas de forma directa y optimizada en C
    return palabra_prohibida in mensaje_chat

# =====================================================================
# RETO 3: Generador de Contraseñas Temporales para Nuevos Usuarios
# Sentido: Asignar una clave alfanumérica segura al registrar un agente.
# =====================================================================
def generar_clave_temporal():
    caracteres_validos = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
    clave_generada = ""
    
    for i in range(8):
        indice_aleatorio = random.randint(0, len(caracteres_validos) - 1)
        caracter_elegido = caracteres_validos[indice_aleatorio]
        clave_generada = clave_generada + caracter_elegido 
        
    return clave_generada

def generar_clave_temporal_factorizado():
    caracteres_validos = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
    # random.choices extrae 'k' elementos al azar. "".join() los concatena sin ciclos ineficientes.
    return "".join(random.choices(caracteres_validos, k=8))

# =====================================================================
# RETO 4: Buscador del Valor Central (Mediana de Latencia de Red)
# Sentido: Encontrar el punto medio de ping (ms) para evaluar lag.
# =====================================================================
def calcular_mediana_latencia(lista_pings):
    pings_ordenados = list(lista_pings)
    n = len(pings_ordenados)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if pings_ordenados[j] > pings_ordenados[j + 1]:
                temporal = pings_ordenados[j]
                pings_ordenados[j] = pings_ordenados[j + 1]
                pings_ordenados[j + 1] = temporal
                
    if n % 2 == 1:
        return pings_ordenados[n // 2]
    else:
        mitad1 = pings_ordenados[(n // 2) - 1]
        mitad2 = pings_ordenados[n // 2]
        return (mitad1 + mitad2) / 2.0

def calcular_mediana_latencia_factorizado(lista_pings):
    # La librería statistics tiene la función median ya implementada de manera robusta
    return statistics.median(lista_pings)

# Si no quieres importar statistics, esta es una alternativa usando built-ins:
def calcular_mediana_latencia_factorizado_b(lista_pings):
    # sorted() usa un algoritmo de ordenamiento interno (Timsort) altamente optimizado
    ordenados = sorted(lista_pings)
    n = len(ordenados)
    mitad = n // 2
    return ordenados[mitad] if n % 2 != 0 else (ordenados[mitad - 1] + ordenados[mitad]) / 2.0


# === PROGRAMA PRINCIPAL (Punto de entrada para probar) ===
if __name__ == "__main__":
    print("--- Probando Código Inicial y Factorizado (Parte II) ---")
    
    print("\n[RETO 1]")
    print("Manual:", [limpiar_nombre_usuario("   luNA_eDUaRDo  ")])
    print("Factorizado:", [limpiar_nombre_usuario_factorizado("   luNA_eDUaRDo  ")])
    
    print("\n[RETO 2]")
    msg = "No digas malas palabras en este servidor"
    print("Manual:", contiene_palabra_bloqueada(msg, "malas"))
    print("Factorizado:", contiene_palabra_bloqueada_factorizado(msg, "malas"))
    
    print("\n[RETO 3]")
    print("Manual:", generar_clave_temporal())
    print("Factorizado:", generar_clave_temporal_factorizado())
    
    print("\n[RETO 4]")
    pings_servidor = [120, 45, 80, 23, 150, 62]
    print("Manual:", calcular_mediana_latencia(pings_servidor))
    print("Factorizado (Statistics):", calcular_mediana_latencia_factorizado(pings_servidor))
    print("Factorizado (Sorted Nativo):", calcular_mediana_latencia_factorizado_b(pings_servidor))