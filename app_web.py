import streamlit as st
import google.generativeai as genai
import os
from PyPDF2 import PdfReader

# 1. Recuperamos tu Diseño Original (Azul y Dorado)
st.set_page_config(page_title="SIEL Pro - Sistema Inteligente", layout="wide")

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

# 2. Motor de IA Corregido (Sin Error 404)
class SIELBrain:
    def __init__(self):
        api_key = st.secrets.get("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key.strip())
            # Usamos el modelo flash que es el que soporta archivos grandes
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            st.error("🔑 Falta la API Key en Secrets")

    def consultar(self, prompt, texto):
        try:
            # Enviamos un fragmento grande pero seguro (60k caracteres)
            contenido = f"{prompt}\n\nTEXTO DEL PLIEGO:\n{texto[:60000]}"
            response = self.model.generate_content(contenido)
            return response.text
        except Exception as e:
            return f"❌ Error de conexión: {str(e)}"

# Inicialización
try:
    siel_ia = SIELBrain()
    motor_listo = True
except:
    motor_listo = False

# 3. Tu Menú Estratégico Original
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
        if clave_acceso: st.error("Clave incorrecta")
        modulo = None
    
    st.markdown("---")
    st.info("Versión 1.0 - Desarrollado por Jenny")

# 4. Ejecución con tu Estética Original
if modulo:
    st.title(f"Monitor de Licitaciones — {modulo}")
    archivo = st.file_uploader("Sube el pliego de condiciones (PDF)", type="pdf")

    if archivo and motor_listo:
        if st.button("🚀 INICIAR ANÁLISIS ESTRATÉGICO"):
            with st.spinner("Analizando con SIEL Pro..."):
                reader = PdfReader(archivo)
                texto_pdf = "".join([p.extract_text() for p in reader.pages if p.extract_text()])
                
                # Definimos el prompt según tu Menú
                prompts = {
                    "🔍 Lectura de Pliegos": "Resume: Objeto, Presupuesto y Fechas.",
                    "📊 Viabilidad del Proceso": "Analiza solvencia financiera y técnica requerida.",
                    "⚠️ Evaluación de Riesgos": "Busca cláusulas de multas o pliegos sastre.",
                    "🏆 Simulador de Puntuación": "Extrae criterios de asignación de puntos.",
                    "✅ Checklist Documental": "Lista todos los documentos obligatorios.",
                    "🤖 Asistente IA": "Dame consejos para ganar esta licitación."
                }
                
                resultado = siel_ia.consultar(prompts.get(modulo), texto_pdf)
                
                st.subheader("Dictamen de la IA")
                st.markdown(f'<div class="resaltado">{resultado}</div>', unsafe_allow_html=True)
                st.download_button("Descargar Reporte", resultado, file_name=f"SIEL_{modulo}.txt")
else:
    st.title("Bienvenido a SIEL Pro")
    st.warning("🔒 Ingrese la clave de acceso para desbloquear.")
