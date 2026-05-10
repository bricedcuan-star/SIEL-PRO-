import streamlit as st
import google.generativeai as genai
from Modulos.tender_analyzer import TenderModule
from PyPDF2 import PdfReader
import os

# Configuración básica
st.set_page_config(page_title="SIEL-PRO", layout="wide")

# Intentar cargar el motor de IA
try:
    ia = TenderModule()
    motor_listo = True
except Exception as e:
    st.error(f"Error al iniciar el motor de IA: {e}")
    motor_listo = False

st.title("🛡️ SIEL-PRO: Dashboard de Evaluación")

# Estilo rápido
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    h1 { color: #1E3A8A; }
    .stButton>button { background-color: #D4AF37; color: white; }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.header("Configuración")
    clave = st.text_input("Clave de Acceso", type="password")

if clave == "1234":
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("1. Cargar Pliego")
        archivo = st.file_uploader("Sube el PDF aquí", type="pdf")
        
    with col2:
        st.subheader("2. Puntos de Control")
        st.write("Se analizarán los 13 puntos SIEL automáticamente.")

    if archivo and motor_listo:
        if st.button("🚀 INICIAR ANÁLISIS"):
            with st.spinner("Leyendo documento..."):
                try:
                    reader = PdfReader(archivo)
                    texto = ""
                    for page in reader.pages:
                        texto += page.extract_text()
                    
                    resultado = ia.analizar_proceso_completo(texto)
                    st.success("Análisis Completado")
                    st.markdown(resultado)
                except Exception as e:
                    st.error(f"Error durante el análisis: {e}")
else:
    st.info("Ingresa la clave para comenzar.")
