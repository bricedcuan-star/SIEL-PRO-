import streamlit as st
import os
from Modulos.tender_analyzer import TenderModule

# Configuración de la página
st.set_page_config(page_title="SIEL-PRO Web", page_icon="🛡️")

st.title("🛡️ SIEL-PRO: Inteligencia en Licitaciones")

# Inicializar motor
ia = TenderModule()

# Barra lateral
with st.sidebar:
    st.header("Acceso al Sistema")
    clave = st.text_input("Ingrese Clave de Acceso", type="password")

if clave == "1234":
    st.success("✅ Acceso Concedido")

    archivo_subido = st.file_uploader("Suba el pliego de condiciones (PDF)", type="pdf")

    if archivo_subido is not None:
        if st.button("🚀 Iniciar Análisis de IA"):
            with st.spinner("Analizando licitación..."):
                # Simulamos los datos para la función que ya tienes
                datos_ficticios = {"presupuesto": 600000000, "objeto": "CONSTRUCCIÓN DE FACHADAS"}
                
                # LLAMADA A TU FUNCIÓN REAL
                resultado = ia.analizar_proceso_completo(datos_ficticios)

                st.subheader("🔍 Resultado del Análisis")
                st.info(f"Estado de Viabilidad: {resultado['viabilidad']}")
                
                if resultado['alertas']:
                    st.warning("⚠️ Alertas Detectadas:")
                    for alerta in resultado['alerts']:
                        st.write(f"- {alerta}")
                else:
                    st.success("✅ No se detectaron alertas críticas.")
else:
    st.info("🔑 Por favor, ingrese su clave en la barra lateral para comenzar.")
