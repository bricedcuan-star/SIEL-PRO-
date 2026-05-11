import google.generativeai as genai
import streamlit as st

class TenderModule:
    def __init__(self):
        # Intentamos obtener la llave desde los Secrets de Streamlit
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
            genai.configure(api_key=api_key.strip())
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        except Exception as e:
            st.error(f"Error al configurar la IA: {str(e)}")

    def analizar_proceso_completo(self, texto_pdf):
        if not texto_pdf:
            return "No se pudo extraer texto del PDF."

        # Tomamos partes estratégicas para no saturar la memoria en archivos de 500 páginas
        # El inicio (objeto), el medio (requisitos) y el final (conclusiones)
        fragmento = texto_pdf[:20000] + "\n" + texto_pdf[-10000:]
        
        prompt = f"""
        Como experto en licitaciones SECOP, analiza la VIABILIDAD de este proceso.
        Extrae:
        1. Indicadores financieros exigidos.
        2. Experiencia técnica requerida.
        3. Riesgos identificados.
        
        Responde de forma ejecutiva para decidir si vale la pena leer las 500 páginas.
        
        PLIEGO:
        {fragmento}
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error en el análisis: {str(e)}"
