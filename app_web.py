import streamlit as st
import os
# Paso 1: Importar el nombre correcto de la clase
from Modulos.tender_analyzer import TenderModule

# Configuración de la página
st.set_page_config(page_title="SIEL-PRO Web", page_icon="🛡️")

st.title("🛡️ SIEL-PRO: Inteligencia en Licitaciones")

# Paso 2: Usar TenderModule en lugar de IAEngine
ia = TenderModule()

# Barra lateral para acceso
with st.sidebar:
    st.header("Acceso al Sistema")
    clave = st.text_input("Ingrese Clave de Acceso", type="password")

if clave == "1234":
    st.success("✅ Acceso Concedido")

    # Subida de archivo
    archivo_subido = st.file_uploader("Suba el pliego de condiciones (PDF)", type="pdf")

    if archivo_subido is not None:
        # Guardar archivo temporal
        with open("temp.pdf", "wb") as f:
            f.write(archivo_subido.getbuffer())

        if st.button("🚀 Iniciar Análisis de IA"):
            with st.spinner("Analizando requisitos críticos..."):
                # Nota: Asegúrate de que estos métodos existan en TenderModule
                # Si dan error, revisaremos los nombres de las funciones dentro de Modulos
                texto = ia.leer_pdf("temp.pdf")
                hallazgos = ia.analizar_requisitos_criticos(texto)

                st.subheader("🔍 Hallazgos Detectados")
                for h in hallazgos:
                    if "CRÍTICO" in h:
                        st.error(h)
                    else:
                        st.warning(h)
else:
    st.info("🔑 Por favor, ingrese su clave en la barra lateral para comenzar.")
