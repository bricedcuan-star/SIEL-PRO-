import google.generativeai as genai
import os

class TenderModule:
    def __init__(self):
        # PEGA AQUÍ TU NUEVA LLAVE
        api_key = "TU_NUEVA_LLAVE_AQUI"
        
        genai.configure(api_key=api_key)
        
        # Este es el nombre técnico más "crudo". Si este falla, el problema es la región.
        self.model = genai.GenerativeModel('gemini-1.5-flash-001')

    def analizar_proceso_completo(self, texto_pdf):
        # Reducimos el texto aún más para asegurar que no sea un error de tamaño
        prompt = f"Analiza los puntos financieros y técnicos de este pliego: {texto_pdf[:15000]}"
        
        try:
            # Intentamos la llamada más básica posible
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            # ÚLTIMO RECURSO: Intentar con el modelo que SÍ te funcionó en el chat de AI Studio
            try:
                self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
                response = self.model.generate_content(prompt)
                return response.text
            except:
                return f"Error crítico: {str(e)}. Google no reconoce el modelo en esta región."
