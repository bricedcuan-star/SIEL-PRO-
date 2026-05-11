class SIELBrain:
    def __init__(self):
        api_key = st.secrets.get("GEMINI_API_KEY")
        if api_key:
            # ESTA LÍNEA ES LA CLAVE: Forzamos la versión estable v1
            os.environ["GOOGLE_API_USE_V1BETA"] = "0" 
            genai.configure(api_key=api_key.strip())
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            st.error("🔑 Error: Revisa los Secrets en Streamlit.")

    def consultar(self, prompt, texto):
        try:
            # Optimizamos el texto para que la IA no se sature
            fragmento = texto[:40000] 
            response = self.model.generate_content(f"{prompt}\n\nPLIEGO:\n{fragmento}")
            return response.text
        except Exception as e:
            return f"❌ Error: {str(e)}. Intenta reiniciar la App en 'Manage App'."
