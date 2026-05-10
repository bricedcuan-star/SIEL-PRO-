import streamlit as st
from Modulos.tender_analyzer import TenderModule
from PyPDF2 import PdfReader
from fpdf import FPDF
import io

# Configuración de página
st.set_page_config(page_title="SIEL-PRO Dashboard", layout="wide")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    [data-testid="stSidebar"] { background-color: #1E3A8A; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stButton>button { background-color: #D4AF37; color: white; width: 100%; border-radius: 20px; font-weight: bold; }
    .buscador-box { padding: 10px; border: 2px solid #1E3A8A; border-radius: 10px; text-align: center; color: #1E3A8A; font-weight: bold; background: white; }
    </style>
    """, unsafe_allow_html=True)

# Inicializar motor
ia = TenderModule()

def generar_pdf(resultado_ia):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "INFORME DE VIABILIDAD SIEL-PRO", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, resultado_ia)
    return pdf.output(dest="S").encode("latin-1", "replace")

# --- INTERFAZ ---
with st.sidebar:
    st.title("🛡️ SIEL-PRO")
    clave = st.text_input("Clave de Acceso", type="password")
    st.divider()
    st.write("Módulo de Análisis — Fase 1")

if clave == "1234":
    st.title("Dashboard de Evaluación de Licitaciones")
    
    # Buscadores
    st.subheader("🌐 Buscadores de Oportunidades")
    b1, b2, b3 = st.columns(3)
    with b1: st.markdown('<div class="buscador-box">SECOP II</div>', unsafe_allow_html=True)
    with b2: st.markdown('<div class="buscador-box">BOGOTÁ</div>', unsafe_allow_html=True)
    with b3: st.markdown('<div class="buscador-box">REVISTA PH</div>', unsafe_allow_html=True)
    
    st.divider()

    # Subida de archivo
    archivo_pdf = st.file_uploader("📂 Suba el pliego de condiciones (PDF)", type="pdf")

    if archivo_pdf:
        if st.button("🚀 INICIAR ESCANEO DE IA (13 PUNTOS SIEL)"):
            with st.spinner("La IA está analizando los 13 puntos de control..."):
                # Leer el PDF
                reader = PdfReader(archivo_pdf)
                texto_completo = ""
                for page in reader.pages:
                    texto_completo += page.extract_text()
                
                # Procesar con la IA
                resultado = ia.analizar_proceso_completo(texto_completo)
                st.session_state['resultado_ia'] = resultado
                
                st.subheader("🔍 Análisis de la IA")
                st.info(resultado)

        # Si ya hay un resultado, mostrar botón de descarga
        if 'resultado_ia' in st.session_state:
            pdf_data = generar_pdf(st.session_state['resultado_ia'])
            st.download_button(
                label="📄 DESCARGAR INFORME DE VIABILIDAD",
                data=pdf_data,
                file_name="Informe_Viabilidad_SIEL.pdf",
                mime="application/pdf"
            )
else:
    st.warning("🔒 Ingrese la clave para acceder.")
