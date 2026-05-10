import google.generativeai as genai
import os

class TenderModule:
    def __init__(self):
        # PEGA AQUÍ TU NUEVA LLAVE ENTRE LAS COMILLAS
        api_key = "AIzaSyARZgTTSfCuH-hHtEPAns062tC3Nzn-QoQ"
        
        genai.configure(api_key=api_key)
        # Usamos el nombre limpio del modelo
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analizar_proceso_completo(self, texto_pdf):
        prompt = f"Analiza los 13 puntos SIEL de este texto: {texto_pdf[:30000]}"
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error: {str(e)}"
