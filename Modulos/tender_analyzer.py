import google.generativeai as genai
import os

class TenderModule:
    def __init__(self):
        # Limpiamos la llave de cualquier espacio invisible
        api_key = "TU_LLAVE_DE_GOOGLE_AQUI".strip()
        genai.configure(api_key=api_key)
        # Usamos el nombre del modelo sin el prefijo 'models/'
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analizar_proceso_completo(self, texto_pdf):
        try:
            # Limitamos el texto para evitar errores de saturación
            response = self.model.generate_content(f"Analiza este pliego: {texto_pdf[:15000]}")
            return response.text
        except Exception as e:
            return f"❌ Error de IA: {str(e)}"
