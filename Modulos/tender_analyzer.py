import google.generativeai as genai
import os

class TenderModule:
    def __init__(self):
        # 1. PEGA TU NUEVA LLAVE AQUÍ (Asegúrate de que no tenga espacios)
        raw_key = "AIzaSyARZgTTSfCuH-hHtEPAns062tC3Nzn-QoQ"
        api_key = raw_key.strip()
        
        genai.configure(api_key=api_key)
        
        # 2. Intentamos cargar el modelo con el nombre más compatible
        try:
            self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
        except:
            self.model = genai.GenerativeModel('gemini-pro')

    def analizar_proceso_completo(self, texto_pdf):
        # Reducimos un poco el texto para evitar errores de saturación
        prompt = f"Analiza los 13 puntos SIEL de este pliego: {texto_pdf[:20000]}"
        
        try:
            # Intentamos la generación
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            # Si falla el nombre 'flash-latest', intentamos con el nombre corto
            try:
                alternativo = genai.GenerativeModel('gemini-1.5-flash')
                response = alternativo.generate_content(prompt)
                return response.text
            except:
                return f"❌ Error final de conexión: {str(e)}. Verifica que la API Key esté activa en Google AI Studio."
