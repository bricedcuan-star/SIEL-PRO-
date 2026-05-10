import google.generativeai as genai
import os

class TenderModule:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Falta la GEMINI_API_KEY en los Secrets")
        genai.configure(api_key=api_key)
        # Usamos 'gemini-1.5-flash' sin el prefijo 'models/' para evitar el error 404
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analizar_proceso_completo(self, texto_pdf):
        prompt = f"""
        Actúa como un Consultor Experto SIEL. Analiza el pliego y extrae los 13 puntos de control:
        1. Liquidez, 2. Endeudamiento, 3. Capital de Trabajo, 4. Experiencia General, 
        5. Experiencia Específica, 6. Capacidad Residual (K/R), 7. Personal Técnico, 
        8. Visita Técnica, 9. Certificación en Alturas, 10. Anticipo, 11. Forma de Pago, 
        12. SST y Ambiental, 13. Riesgos Contractuales.

        Texto del pliego:
        {texto_pdf[:30000]}
        """
        response = self.model.generate_content(prompt)
        return response.text
