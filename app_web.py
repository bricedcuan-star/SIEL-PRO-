import streamlit as st
import google.generativeai as genai
import os
from PyPDF2 import PdfReader

# 1. Configuración de la Página
st.set_page_config(page_title="SIEL Pro - Sistema Inteligente", layout="wide")

# 2. Estilos Corporativos (Azul y Dorado)
st.markdown("""
    <style>
    .main { background-color: #f4f7f9; }
    [data-testid="stSidebar"] { background-color: #1E3A8A; }
    [data-testid="stSidebar"] * { color: white !important; }
    h1, h2, h3 { color: #1E3A8A !important; }
    .stButton>button { 
        border: 2px solid #D4AF37; 
        color: #1E3A8A; 
        font-weight: bold; 
        width: 100%;
        border-radius: 10px;
    }
    .resaltado {
        border-left: 10px solid #D4AF37;
        padding: 20px;
        background: white;
        border-radius: 5px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica de la IA (Integrada para evitar errores de importación)
class SIELBrain:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY", "AIzaSyARZgTTSfCuH-hHtEPAns062tC3Nzn-QoQ")
        genai.configure(api_key=api_key.strip())
        # Intentamos con 1.5 flash, si no con pro
        try:
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        except:
            self.model = genai.GenerativeModel('gemini-pro')

    def consultar(self, prompt, texto):
        try:
            contenido = f"{prompt}\n\nTEXTO DEL PLIEGO:\n{texto[:100000]}"
            response = self.model.generate_content(contenido)
            return response.text
        except Exception as e:
            # Fallback a gemini-pro si falla flash
            try:
                alt_model = genai.GenerativeModel('gemini-pro')
                response = alt_model.generate_content(f"{prompt}\n\nTEXTO:\n{texto[:30000]}")
                return response.text
            except:
                return f"❌ Error de IA: {str(e)}. Verifica tu API Key en Google AI Studio."

try:
    siel_ia = SIELBrain()
    motor_listo = True
except Exception as e:
    st.error(f"Error al inicializar SIEL: {e}")
    motor_listo = False

# 4. Barra Lateral - Navegación y Seguridad
with st.sidebar:
    st.title("📂 SIEL Pro")
    st.markdown("---")
    clave_acceso = st.text_input("Clave de Acceso", type="password")
    
    if clave_acceso == "SIEL_2026*Pro":
        st.success("Acceso Concedido")
        modulo = st.radio("Menú de Estrategia", [
            "🔍 Lectura de Pliegos",
            "📊 Viabilidad del Proceso",
            "⚠️ Evaluación de Riesgos",
            "🏆 Simulador de Puntuación",
            "✅ Checklist Documental",
            "🤖 Asistente IA"
        ])
    else:
        if clave_acceso:
            st.error("Clave incorrecta")
        modulo = None
    
    st.markdown("---")
    st.info("Versión 1.0 - Desarrollado por Jenny")

# 5. Ejecución de Módulos
if modulo:
    st.title(f"Monitor de Licitaciones — {modulo}")
    archivo = st.file_uploader("Sube el pliego de condiciones (PDF)", type="pdf")

    if archivo and motor_listo:
        if st.button("🚀 INICIAR ANÁLISIS ESTRATÉGICO"):
            with st.spinner("Analizando el proceso con SIEL Pro..."):
                reader = PdfReader(archivo)
                texto_pdf = "".join([p.extract_text() for p in reader.pages])
                
                if modulo == "🔍 Lectura de Pliegos":
                    prompt = "Analiza este pliego y genera un resumen SIEL con: Objeto, Presupuesto, Fechas clave e Indicadores Financieros."
                elif modulo == "📊 Viabilidad del Proceso":
                    prompt = "Evalúa la VIABILIDAD de este proceso. ¿Es rentable? ¿Qué requisitos técnicos y financieros son los más difíciles?"
                elif modulo == "⚠️ Evaluación de Riesgos":
                    prompt = "Identifica RIESGOS jurídicos, financieros o técnicos en este pliego."
                elif modulo == "🏆 Simulador de Puntuación":
                    prompt = "Extrae los CRITERIOS DE PUNTUACIÓN (Industria nacional, Mipymes, etc)."
                else:
                    prompt = "Brinda consejos estratégicos para ganar esta licitación según el pliego."

                resultado = siel_ia.consultar(prompt, texto_pdf)
                
                st.subheader("Resultado del Análisis")
                st.markdown(f'<div class="resaltado">{resultado}</div>', unsafe_allow_html=True)
                st.download_button("Descargar Reporte", resultado, file_name=f"SIEL_{modulo}.txt")
    else:
        st.info("📩 Para comenzar, sube el PDF del pliego.")
else:
    st.title("Bienvenido a SIEL Pro")
    st.warning("🔒 Ingrese la clave de acceso para desbloquear las herramientas.")