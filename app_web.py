import streamlit as st
import google.generativeai as genai
import os
from PyPDF2 import PdfReader

# Configuración inicial (Debe ser lo primero)
st.set_page_config(page_title="SIEL Pro", layout="wide")

# Lógica de conexión segura
def inicializar_ia():
    try:
        api_key = st.secrets.get("GEMINI_API_KEY", "")
        if api_key:
            genai.configure(api_key=api_key.strip())
            return genai.GenerativeModel('gemini-1.5-flash')
    except Exception:
        return None
    return None

model = inicializar_ia()

# Interfaz básica para que no se quede en blanco
st.title("📂 SIEL Pro - Análisis de Pliegos")

with st.sidebar:
    st.header("Configuración")
    clave = st.text_input("Clave de Acceso", type="password")
    if clave == "SIEL_2026*Pro":
        st.success("Acceso Concedido")
        modo = st.radio("Menú", ["Análisis de Viabilidad", "Resumen de Pliego"])
    else:
        modo = None

if modo:
    archivo = st.file_uploader("Sube el PDF de 500 páginas", type="pdf")
    if archivo and st.button("🚀 Iniciar IA"):
        with st.spinner("Leyendo y filtrando viabilidad..."):
            try:
                reader = PdfReader(archivo)
                # Solo leemos las primeras 50 páginas para no romper la memoria
                texto = ""
                for i in range(min(50, len(reader.pages))):
                    texto += reader.pages[i].extract_text()
                
                if model:
                    res = model.generate_content(f"Analiza la viabilidad financiera de este pliego: {texto[:30000]}")
                    st.write(res.text)
                else:
                    st.error("La IA no está configurada en Secrets.")
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.info("Por favor, ingresa la clave en la barra lateral para desbloquear.")
