import google.generativeai as genai
import os

class TenderModule:
    def __init__(self):
        # 1. PEGA TU LLAVE AQUÍ (sin espacios)
        api_key = "TU_LLAVE_DE_AI_STUDIO_AQUI".strip()
        genai.configure(api_key=api_key)
        
        # 2. Definimos el modelo de forma limpia
        # Usamos el nombre corto para evitar el error 404 de la v1beta
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analizar_proceso_completo(self, texto_pdf):
        # Limitamos el texto para que no se bloquee por tamaño
        prompt = f"Analiza los puntos clave de este pliego de licitación: {texto_pdf[:20000]}"
        
        try:
            # Intento de generación con el modelo actual
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            # Si falla, intentamos con el nombre técnico alternativo
            try:
                model_alt = genai.GenerativeModel('models/gemini-1.5-flash')
                response = model_alt.generate_content(prompt)
                return response.text
            except Exception as e2:
                return f"❌ Error de conexión: {str(e2)}. Verifica tu API Key en Google AI Studio."
