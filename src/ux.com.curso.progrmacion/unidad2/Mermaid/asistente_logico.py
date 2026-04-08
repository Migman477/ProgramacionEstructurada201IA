"""Asistente lógico en Python
Este programa simula un asistente lógico que responde a diferentes solicitudes del usuario.
El asistente puede saludar, proporcionar información sobre el clima, la hora y despedirse.
"""

import datetime

globalnombre_asistente = "Lin"

def obtener_solicitud():
  

    print(f"Hola, soy {globalnombre_asistente}, tu asistente lógico")

    solicitud = input("¿En qué puedo ayudarte hoy? : ").lower()
 
    return solicitud

def detectar_intencion(solicitud):

    if "hola" in solicitud or "buenos dias" in solicitud or "buenas tardes" in solicitud or "buenas noches" in solicitud:
        return "¡Hola! Soy tu asistente. Es un gusto saludarte"
    
    elif "clima"in solicitud or "temperatura" in solicitud:
        return "Consultando el servicio meteorológico... Hoy en Xalapa tendremos un día nublado."
    
    elif "hora" in solicitud or "tiempo" in solicitud:
        return "La hora actual del sistema es: " + datetime.datetime.now().strftime("%H:%M:%S")
    
    else:
        return "Lo siento, todavía no entiendo ese comando. ¿Podrías intentar con otra palabra?"
    
    









