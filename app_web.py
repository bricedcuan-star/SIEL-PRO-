import streamlit as st
from Modulos.tender_analyzer import TenderModule
from PyPDF2 import PdfReader

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

try:
    ia = TenderModule()
    motor_listo = True
except Exception as e:
    st.error(f"Error al conectar con el cerebro de IA: {e}")
    motor_listo = False

with st.sidebar:
    st.title("📂 SIEL Pro")
    st.markdown("---")
    modulo = st.radio("Menú de Estrategia", [
        "🔍 Lectura de Pliegos",
        "📊 Viabilidad del Proceso",
        "⚠️ Evaluación de Riesgos",
        "🏆 Simulador de Puntuación",
        "✅ Checklist Documental",
        "🤖 Asistente IA"
    ])
    st.markdown("---")
    st.info("Versión 1.0 - Desarrollado por Jenny")

st.title(f"Monitor de Licitaciones — {modulo}")

archivo = st.file_uploader("Sube el pliego de condiciones (PDF)", type="pdf")

if archivo and motor_listo:
    if st.button("🚀 INICIAR ANÁLISIS ESTRATÉGICO"):
        with st.spinner("Analizando el proceso..."):
            reader = PdfReader(archivo)
            texto = "".join([p.extract_text() for p in reader.pages])
            
            if modulo == "🔍 Lectura de Pliegos":
                resultado = ia.analizar_proceso_completo(texto)
            elif modulo == "📊 Viabilidad del Proceso":
                resultado = ia.analizar_viabilidad(texto)
            elif modulo == "⚠️ Evaluación de Riesgos":
                resultado = ia.analizar_riesgos(texto)
            elif modulo == "🏆 Simulador de Puntuación":
                resultado = ia.simular_puntuacion(texto)
            else:
                resultado = "Motor de IA activado para este módulo. Generando respuesta..."

            st.subheader("resultado del Análisis")
            st.markdown(f'<div class="resaltado">{resultado}</div>', unsafe_allow_html=True)
else:
    st.info("📩 Para comenzar, sube el PDF del pliego y selecciona un módulo en la barra lateral.")