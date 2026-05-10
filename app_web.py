import streamlit as st
from Modulos.tender_analyzer import TenderModule
from PyPDF2 import PdfReader
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="SIEL-PRO Dashboard", page_icon="🛡️", layout="wide")

# 2. ESTILOS PERSONALIZADOS (Azul, Dorado y Blanco)
st.markdown("""
    <style>
    .main { background-color: #f4f7f9; }
    [data-testid="stSidebar"] { background-color: #1E3A8A; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Títulos y Subtítulos */
    h1, h2, h3 { color: #1E3A8A !important; font-family: 'Segoe UI', sans-serif; }
    
    /* Botones de Buscadores */
    .stButton>button {
        border: 2px solid #D4AF37;
        color: #1E3A8A;
        background-color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #D4AF37;
        color: white;
    }
    
    /* Botón de Acción Principal */
    .btn-analizar>div>button {
        background-color: #1E3A8A !important;
        color: white !important;
        border: none !important;
        font-size: 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CARGA DEL MOTOR
try:
    ia = TenderModule()
    motor_listo = True
except Exception as e:
    st.error(f"Error al conectar con el cerebro de IA: {e}")
    motor_listo = False

# 4. INTERFAZ LATERAL
with st.sidebar:
    st.title("🛡️ SIEL-PRO")
    st.write("Sistema Inteligente de Evaluación de Licitaciones")
    st.divider()
    clave = st.text_input("Clave de Acceso", type="password")

# 5. CUERPO PRINCIPAL
if clave == "1234":
    st.title("Módulo de Análisis — Fase 1")
    
    # --- SECCIÓN: BUSCADORES CON LINKS REALES ---
    st.subheader("🌐 Buscadores de Oportunidades")
    col_b1, col_b2, col_b3 = st.columns(3)
    
    with col_b1:
        st.link_button("Ir a SECOP II", "https://community.secop.gov.co/Public/Tendering/ContractNoticeManagement/Index")
    with col_b2:
        st.link_button("Ir a BOGOTÁ COMPRA", "https://zonatransaccional.bogotacompra.gov.co/sitio/destacados/secop-ii/")
    with col_b3:
        st.link_button("Ir a REVISTA PH", "https://revistaph.com.co/licitaciones/")

    st.divider()

    # --- SECCIÓN: CARGA Y ANÁLISIS ---
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("1. Configuración del Proceso")
        archivo_pdf = st.file_uploader("Subir pliego (PDF)", type="pdf")
        
    with col_right:
        st.subheader("2. Puntos de Control SIEL")
        st.info("La IA evaluará automáticamente los 13 indicadores de viabilidad financiera, técnica y legal.")

    if archivo_pdf and motor_listo:
        st.divider()
        if st.button("🚀 INICIAR ANÁLISIS DE IA", key="btn_main"):
            with st.spinner("Analizando los 13 puntos SIEL... Esto puede tardar un minuto."):
                try:
                    # Leer PDF
                    reader = PdfReader(archivo_pdf)
                    texto = ""
                    for page in reader.pages:
                        texto += page.extract_text()
                    
                    # Enviar a la IA
                    resultado = ia.analizar_proceso_completo(texto)
                    
                    # Mostrar resultados en un cuadro elegante
                    st.success("### ✅ Resultado del Análisis")
                    st.markdown(f"""
                    <div style="background-color: white; padding: 20px; border-radius: 10px; border-left: 10px solid #D4AF37; color: #333;">
                        {resultado}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Opción de descargar (Texto simple por ahora para evitar errores)
                    st.download_button("Descargar Informe (TXT)", resultado, file_name="Informe_SIEL.txt")
                    
                except Exception as e:
                    st.error(f"Ocurrió un error durante el escaneo: {e}")
else:
    st.warning("🔒 Ingrese la clave en el menú lateral para acceder al sistema.")
