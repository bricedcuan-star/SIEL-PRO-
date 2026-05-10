import streamlit as st
from Modulos.tender_analyzer import TenderModule
from PyPDF2 import PdfReader

st.set_page_config(page_title="SIEL-PRO Dashboard", layout="wide")

# ESTILOS AZUL Y DORADO
st.markdown("""
    <style>
    .main { background-color: #f4f7f9; }
    [data-testid="stSidebar"] { background-color: #1E3A8A; }
    [data-testid="stSidebar"] * { color: white !important; }
    h1, h2, h3 { color: #1E3A8A !important; }
    .stButton>button { border: 2px solid #D4AF37; color: #1E3A8A; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

try:
    ia = TenderModule()
    motor_listo = True
except Exception as e:
    st.error(f"Error: {e}")
    motor_listo = False

with st.sidebar:
    st.title("🛡️ SIEL-PRO")
    clave = st.text_input("Clave", type="password")

if clave == "1234":
    st.title("Módulo de Análisis — Fase 1")
    
    # BUSCADORES ACTUALIZADOS
    st.subheader("🌐 Buscadores de Oportunidades")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.link_button("SECOP II", "https://community.secop.gov.co/Public/Tendering/ContractNoticeManagement/Index")
    with c2:
        st.link_button("CONTRATOS BOGOTÁ", "https://bogota.gov.co/asi-vamos/contratos-y-obras/participa")
    with c3:
        st.link_button("REVISTA PH", "https://convocatorias.revistaphcolombia.com/")
    with c4:
        st.link_button("LEY PROPIEDAD H.", "https://leydepropiedadhorizontal.org/category/convocatorias/")

    st.divider()

    # CARGA Y ANÁLISIS
    archivo = st.file_uploader("Subir pliego (PDF)", type="pdf")

    if archivo and motor_listo:
        if st.button("🚀 INICIAR ANÁLISIS DE IA"):
            with st.spinner("Analizando pliego..."):
                reader = PdfReader(archivo)
                texto = "".join([p.extract_text() for p in reader.pages])
                resultado = ia.analizar_proceso_completo(texto)
                
                st.success("### Resultado del Análisis")
                st.markdown(f'<div style="border-left: 10px solid #D4AF37; padding:20px; background:white;">{resultado}</div>', unsafe_allow_html=True)
                st.download_button("Descargar Informe (TXT)", resultado, file_name="Informe_SIEL.txt")
else:
    st.info("🔒 Ingrese la clave.")
