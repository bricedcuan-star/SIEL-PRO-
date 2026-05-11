import google.generativeai as genai
import streamlit as st
import os

class TenderModule:
    def __init__(self):
        # Buscamos la clave que pusiste en los Secrets
        api_key = st.secrets.get("GEMINI_API_KEY")
        
        if api_key:
            genai.configure(api_key=api_key.strip())
            # Usamos el modelo más rápido y con mayor capacidad de memoria
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            st.error("🔑 Error: No se detecta la clave en Secrets.")

    def analizar_proceso_completo(self, texto_pdf):
        if not texto_pdf: return "PDF ilegible."

        # Para 500 páginas, tomamos el inicio, el medio y el final del texto
        # que es donde suelen estar los requisitos y las conclusiones.
        resumen_entrada = texto_pdf[:15000] + "\n[...]\n" + texto_pdf[-10000:]
        
        prompt = f"""
        Como experto en licitaciones SECOP, analiza este extracto de un pliego extenso:
        {resumen_entrada}
        
        Extrae exclusivamente:
        - Requisitos de liquidez y endeudamiento.
        - Años de experiencia mínima.
        - Conclusión: ¿Es viable o hay riesgos de pliego sastre?
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error de IA: {str(e)}"
