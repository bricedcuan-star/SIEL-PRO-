import google.generativeai as genai
import os

class TenderModule:
    def __init__(self):
        # Asegúrate de pegar tu clave aquí sin espacios
        api_key = "TU_NUEVA_LLAVE_AQUI".strip()
        genai.configure(api_key=api_key)
        
        # Intentamos definir el modelo de la forma más compatible posible
        self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            generation_config={"fallback_to_none": False}
        )

    def analizar_proceso_completo(self, texto_pdf):
        # Prompt simplificado para asegurar respuesta rápida
        prompt = f"Analiza los puntos clave de este pliego de licitación: {texto_pdf[:15000]}"
        
        try:
            # Si el modelo estándar falla, este bloque lo captura
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            # Si sigue dando error 404, intentamos la ruta técnica larga
            try:
                model_alt = genai.GenerativeModel('models/gemini-1.5-flash')
                return model_alt.generate_content(prompt).text
            except:
                return f"❌ Error de configuración en Google: {str(e)}. Verifica que la API Key sea de tipo 'Generative AI' en AI Studio."
