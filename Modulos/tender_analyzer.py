import google.generativeai as genai
import os

class TenderModule:
    def __init__(self):
        # Configuramos la IA (usará la clave que pusiste en Secrets)
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('models/gemini-1.5-flash')

    def analizar_proceso_completo(self, texto_pdf):
        """
        Este es el Prompt Maestro que contiene tus 13 puntos SIEL.
        """
        prompt = f"""
        Actúa como un Consultor Experto SIEL. Analiza el siguiente texto de un pliego de condiciones 
        y extrae/evalúa los 13 puntos de control SIEL:
        1. Liquidez, 2. Endeudamiento, 3. Capital de Trabajo, 4. Experiencia General, 
        5. Experiencia Específica, 6. Capacidad Residual (K/R), 7. Personal Técnico, 
        8. Visita Técnica, 9. Certificación en Alturas, 10. Anticipo, 11. Forma de Pago, 
        12. SST y Ambiental, 13. Riesgos Contractuales.

        Para cada punto, indica si se encontró información y un breve resumen.
        Al final, da un veredicto de VIABILIDAD (VIABLE, NO VIABLE o REQUIERE REVISIÓN).

        Texto del pliego:
        {texto_pdf}
        """
        
        response = self.model.generate_content(prompt)
        return response.text
