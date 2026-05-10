import google.generativeai as genai
import os
import streamlit as st

class TenderModule:
    def __init__(self):
        # --- SOLUCIÓN DIRECTA ---
        # Pega tu clave de Google AI Studio entre las comillas:
        api_key = "AIzaSyDheHzT1xdTKyplmVA_kkw762gqrP2oBss"
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analizar_proceso_completo(self, texto_pdf):
        # Prompt mejorado para que el informe sea profesional
        prompt = f"""
        Actúa como un Consultor Experto en Licitaciones SIEL. 
        Analiza el siguiente pliego de condiciones y extrae detalladamente los 13 puntos de control:
        1. Liquidez, 2. Endeudamiento, 3. Capital de Trabajo, 4. Experiencia General, 
        5. Experiencia Específica, 6. Capacidad Residual (K/R), 7. Personal Técnico, 
        8. Visita Técnica, 9. Certificación en Alturas, 10. Anticipo, 11. Forma de Pago, 
        12. SST y Ambiental, 13. Riesgos Contractuales.

        Texto del pliego:
        {texto_pdf[:30000]}
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error de conexión con la IA: {str(e)}"
