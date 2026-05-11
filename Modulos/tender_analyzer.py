import google.generativeai as genai
import streamlit as st

class TenderModule:
    def __init__(self):
        # Usamos st.secrets para que no tengas que pegar la llave en el código
        # Si prefieres pegarla, cámbialo por: api_key = "TU_LLAVE".strip()
        try:
            api_key = st.secrets["GEMINI_API_KEY"].strip()
        except:
            api_key = "TU_LLAVE_AQUI".strip()
            
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analizar_proceso_completo(self, texto_pdf):
        # Si el PDF es gigante, tomamos las partes donde suelen estar los requisitos
        # Normalmente: Inicio (objeto), Medio (requisitos) y Final (anexos)
        fragmento = texto_pdf[:40000] # Aproximadamente 15-20 páginas clave
        
        prompt = f"""
        Eres un experto jurídico y financiero en contratacion pública (SECOP). 
        Analiza el siguiente extracto de pliego de condiciones y determina la VIABILIDAD.
        
        Extrae y resume estos puntos críticos:
        1. Requisitos Financieros (Liquidez, Endeudamiento, Capital de Trabajo).
        2. Experiencia Requerida (General y Específica).
        3. Puntos clave de SST y Riesgos.
        
        TEXTO DEL PLIEGO:
        {fragmento}
        
        CONCLUSIÓN: Responde claramente si el proceso parece viable o si tiene 'trampas' o requisitos muy restrictivos.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error en el motor de IA: {str(e)}"
