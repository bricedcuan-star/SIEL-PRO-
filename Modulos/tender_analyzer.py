import google.generativeai as genai
import os

class TenderModule:
    def __init__(self):
        # 1. PEGA TU NUEVA LLAVE AQUÍ
        raw_key = "AIzaSyARZgTTSfCuH-hHtEPAns062tC3Nzn-QoQ"
        
        # 2. LIMPIEZA Y CONFIGURACIÓN
        api_key = raw_key.strip()
        genai.configure(api_key=api_key)
        
        # Usamos el modelo más estable para evitar el error 404
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analizar_proceso_completo(self, texto_pdf):
        prompt = f"""
        Actúa como un experto en licitaciones. Analiza los 13 puntos SIEL:
        1. Liquidez, 2. Endeudamiento, 3. Capital de Trabajo, 4. Experiencia General, 
        5. Experiencia Específica, 6. Capacidad Residual, 7. Personal Técnico, 
        8. Visita Técnica, 9. Certificación Alturas, 10. Anticipo, 11. Forma de Pago, 
        12. SST/Ambiental, 13. Riesgos.
        
        Texto: {texto_pdf[:25000]}
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error en la IA: {str(e)}"
