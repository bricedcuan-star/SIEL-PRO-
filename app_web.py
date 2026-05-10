import streamlit as st
import os

# 1. Configuración de página (esto siempre debe ir primero)
st.set_page_config(page_title="SIEL-PRO", layout="wide")

st.title("🛡️ SIEL-PRO: Modo Recuperación")

# 2. Diagnóstico de archivos
st.subheader("Diagnóstico de Sistema")
if os.path.exists("Modulos/tender_analyzer.py"):
    st.success("✅ Archivo 'tender_analyzer.py' encontrado.")
else:
    st.error("❌ No se encuentra la carpeta 'Modulos' o el archivo 'tender_analyzer.py'. Revisa el nombre en GitHub.")

# 3. Intento de importación controlada
try:
    from Modulos.tender_analyzer import TenderModule
    st.success("✅ Motor de IA cargado correctamente.")
    ia_lista = True
except Exception as e:
    st.error(f"❌ Error al cargar el motor: {e}")
    ia_lista = False

# 4. Interfaz mínima para probar
st.divider()
clave = st.text_input("Introduce la clave para desbloquear", type="password")

if clave == "1234":
    st.write("### ¡Bienvenido al Dashboard!")
    uploaded_file = st.file_uploader("Prueba subir un PDF", type="pdf")
    if uploaded_file and ia_lista:
        st.info("Archivo recibido. El sistema está listo para procesar.")
