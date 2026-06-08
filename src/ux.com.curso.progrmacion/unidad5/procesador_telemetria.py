# procesador_telemetria.py

# ==========================================
# IMPORTACIÓN DE BIBLIOTECAS (Biblioteca Estándar)
# ==========================================
import sys

# ==========================================
# FUNCIONES DEL SISTEMA
# ==========================================

def limpiar_lecturas(lista_datos):
    """
    Filtra las lecturas de un sensor LIDAR eliminando valores atípicos o inválidos.

    Itera sobre la lista de entrada y descarta cualquier valor que se considere un
    error de medición o un valor atípico. Los valores válidos se definen
    estrictamente en el rango cerrado de 0.0 a 100.0. Utiliza estructuras
    condicionales para garantizar el tipo correcto de los datos sin levantar
    excepciones.

    Parámetros:
    lista_datos (list): Una lista de números (flotantes o enteros) que representan
                        las distancias detectadas por el sensor.

    Retorna:
    list: Una nueva lista que contiene únicamente los valores de distancia válidos.
          Si el argumento recibido no es de tipo lista, retorna una lista vacía.
    """
    lecturas_validas = []

    if isinstance(lista_datos, list):
        for lectura in lista_datos:
            if isinstance(lectura, (int, float)):
                if lectura >= 0.0 and lectura <= 100.0:
                    lecturas_validas.append(float(lectura))
            else:
                pass
    else:
        pass 

    return lecturas_validas


def calcular_alertas(lista_filtrada, umbral_critico):
    """
    Cuenta cuántos valores en una lista de datos caen por debajo de un umbral crítico.

    La función valida los tipos de datos de entrada utilizando exclusivamente
    estructuras condicionales. Itera sobre la lista proporcionada y compara cada
    elemento numérico con el umbral. Si el elemento es estrictamente menor que
    el umbral, se contabiliza como una alerta.

    Parámetros:
    lista_filtrada (list): Una lista de números (flotantes o enteros) que representan
                           las lecturas válidas a evaluar.
    umbral_critico (float): Un número que define el límite de seguridad. Valores
                            menores a este límite desencadenan una alerta.

    Retorna:
    int: El número total de alertas detectadas. Retorna 0 si no hay alertas o si
         los parámetros proporcionados no son de los tipos correctos.
    """
    total_alertas = 0

    if isinstance(lista_filtrada, list):
        if isinstance(umbral_critico, (int, float)):
            for valor in lista_filtrada:
                if isinstance(valor, (int, float)):
                    if valor < umbral_critico:
                        total_alertas += 1
                else:
                    pass
        else:
            pass
    else:
        pass

    return total_alertas


def generar_log_sistema(total_alertas):
    """
    Genera un mensaje de registro (log) indicando el estado del sistema y la acción a tomar.

    Identifica la plataforma del sistema operativo actual mediante el módulo 'sys'.
    Evalúa el número total de alertas proporcionado: si la cantidad es mayor a 3,
    determina que la acción debe ser 'ABORTAR'; de lo contrario, es 'PERMITIDA'.
    Retorna una cadena formateada con los datos integrados.

    Parámetros:
    total_alertas (int): La cantidad de alertas críticas detectadas en el sistema.

    Retorna:
    str: Cadena con el formato '[SISTEMA OS] Alertas críticas encontradas: X. Acción: [ACCION]'.
    """
    if total_alertas > 3:
        accion = "ABORTAR"
    else:
        accion = "PERMITIDA"
        
    sistema_os = sys.platform
    
    return f"[{sistema_os}] Alertas críticas encontradas: {total_alertas}. Acción: {accion}"


# ==========================================
# PROGRAMA PRINCIPAL (Orquestación Manual)
# ==========================================
if __name__ == "__main__":

    # 1. Datos simulados de telemetría (con algunos errores de sensor, tipos inválidos y valores atípicos)
    lecturas_raw = [12.5, -5.0, 88.2, 120.1, 1.2, 0.0, 45.6, 2.5, "error_de_red", 1.8]
    UMBRAL = 3.0

    print("=== SISTEMA DE TELEMETRÍA DE AGENTE AUTÓNOMO ===\n")

    # Mostrar lista original en pantalla
    print(f"Lista original:   {lecturas_raw}")

    # 2. Invocación estructurada: Filtrar las lecturas
    lecturas_procesadas = limpiar_lecturas(lecturas_raw)
    print(f"Lista filtrada:   {lecturas_procesadas}")

    # 3. Invocación estructurada: Calcular alertas usando los datos filtrados
    alertas_detectadas = calcular_alertas(lecturas_procesadas, UMBRAL)
    print(f"Total de alertas: {alertas_detectadas}")

    # 4. Invocación estructurada: Generar el log del sistema
    log_resultado = generar_log_sistema(alertas_detectadas)
    print(f"Log generado:     {log_resultado}")


"""
================================================================================
EVIDENCIAS DE CONTROL DE CALIDAD
================================================================================

1. PROMPT UTILIZADO:
"Actúa como un programador experto en Python Estructurado. Escribe el código de
tres funciones: limpiar_lecturas(lista_datos), calcular_alertas(lista_filtrada, 
umbral_critico), y generar_log_sistema(total_alertas). Restricciones estrictas: 
No utilices programación orientada a objetos (POO). No utilices manejo de 
excepciones (nada de bloques try-except). Gestiona los errores de tipo y de 
rango usando únicamente estructuras condicionales if/else. Utiliza la 
biblioteca estándar sys. Genera el código completo de las funciones y un 
bloque if __name__ == '__main__': para probarlas en secuencia."

--------------------------------------------------------------------------------

2. TABLA DE PRUEBAS DE ESCRITORIO MANUAL (TRACE TABLE):
Caso de prueba: Lista de lecturas 100% erróneas o atípicas.
Entradas: lecturas_raw = [-10.5, 105.0, "desconexion", None], UMBRAL = 2.0

Paso a paso:
- Inicio limpiar_lecturas(lista_datos):
  * iteración 1: lectura = -10.5 -> ¿Es float/int? Sí. ¿Está entre 0.0 y 100.0? No. Se ignora.
  * iteración 2: lectura = 105.0 -> ¿Es float/int? Sí. ¿Está entre 0.0 y 100.0? No. Se ignora.
  * iteración 3: lectura = "desconexion" -> ¿Es float/int? No. Se ignora (pasa al else).
  * iteración 4: lectura = None -> ¿Es float/int? No. Se ignora.
  * Resultado de limpiar_lecturas: lecturas_validas = []

- Inicio calcular_alertas(lista_filtrada, umbral_critico):
  * lista_filtrada = []
  * Condición isinstance([], list) es True.
  * Condición isinstance(2.0, (int, float)) es True.
  * Bucle for valor in []: No se ejecuta porque la lista está vacía.
  * Resultado de calcular_alertas: total_alertas = 0

- Inicio generar_log_sistema(total_alertas):
  * total_alertas = 0
  * Condición 0 > 3 es False.
  * Variable accion = "PERMITIDA"
  * Variable sistema_os toma el valor de sys.platform (ej. 'win32' o 'linux').
  * Resultado: "[win32] Alertas críticas encontradas: 0. Acción: PERMITIDA"

--------------------------------------------------------------------------------

3. AUDITORÍA DE CÓDIGO:
¿La IA intentó utilizar funciones o sintaxis avanzada?
Sí, en mis primeros intentos la IA tendía a utilizar "Comprensión de Listas" 
(List Comprehensions) para la función limpiar_lecturas, escribiendo código como:
lecturas_validas = [x for x in lista_datos if isinstance(x, (int, float)) and 0 <= x <= 100]

Además, para manejar los errores de tipos de datos al comparar con el umbral, 
la IA proponía usar bloques "try: ... except TypeError: continue".

Para obligar a la IA a mantener el diseño puramente estructurado (propio de 
nuestras clases), tuve que agregar explícitamente en el prompt las directivas: 
"No utilices manejo de excepciones (nada de bloques try-except)" y "Gestiona 
los errores usando únicamente estructuras condicionales if/else", además de 
pedir que actuara como un "programador en Python Estructurado". Esto la forzó 
a utilizar bucles 'for' tradicionales anidados con 'if isinstance(...)'.
================================================================================
"""