import google.generativeai as genai
import os

class TenderModule:
    def __init__(self):
        # PEGA AQUÍ TU NUEVA LLAVE
        api_key = "AIzaSyARZgTTSfCuH-hHtEPAns062tC3Nzn-QoQ"
        
        genai.configure(api_key=api_key)
        
        # Cambiamos a 'gemini-pro' para máxima compatibilidad y evitar el error 404
        self.model = genai.GenerativeModel('gemini-pro')

    def analizar_proceso_completo(self, texto_pdf):
        prompt = f"""
        Analiza detalladamente los 13 puntos SIEL del siguiente pliego:
        1. Liquidez, 2. Endeudamiento, 3. Capital de Trabajo, 4. Experiencia General, 
        5. Experiencia Específica, 6. Capacidad Residual, 7. Personal Técnico, 
        8. Visita Técnica, 9. Certificación Alturas, 10. Anticipo, 11. Forma de Pago, 
        12. SST/Ambiental, 13. Riesgos.

        Texto: {texto_pdf[:30000]}
        """
        try:
            # Forzamos la generación simple
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            # Si gemini-pro también falla, intentamos con el nombre alternativo de flash
            try:
                self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
                response = self.model.generate_content(prompt)
                return response.text
            except:
                return f"❌ Error de compatibilidad: {str(e)}. Intente recargar la página."
