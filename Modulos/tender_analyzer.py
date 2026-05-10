import google.generativeai as genai
import os
import streamlit as st

class TenderModule:
    def __init__(self):
        # Intentamos obtenerla de 3 formas distintas
        api_key = os.getenv("GEMINI_API_KEY") 
        
        # Si no la encuentra, intentamos buscarla en st.secrets (forma interna de Streamlit)
        if not api_key:
            try:
                api_key = st.secrets["GEMINI_API_KEY"]
            except:
                api_key = None

        if not api_key:
            # Este mensaje aparecerá en la consola para ayudarte a debuguear
            print("⚠️ ADVERTENCIA: No se detectó la API KEY")
            return # Salimos sin dar error fatal

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analizar_proceso_completo(self, texto_pdf):
        if not hasattr(self, 'model'):
            return "❌ Error: La IA no está configurada. Revisa la API KEY en los Secrets."
        
        prompt = f"Analiza los 13 puntos SIEL del siguiente pliego: {texto_pdf[:30000]}"
        response = self.model.generate_content(prompt)
        return response.text
