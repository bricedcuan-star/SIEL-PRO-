import streamlit as st
from Modulos.tender_analyzer import TenderModule

# Configuración con layout ancho para que se parezca al dashboard
st.set_page_config(page_title="SIEL-PRO Dashboard", page_icon="🛡️", layout="wide")

# --- ESTILOS CSS PARA AZUL Y DORADO ---
st.markdown("""
    <style>
    /* Fondo general */
    .main { background-color: #f0f2f6; }
    
    /* Títulos en Azul Profundo */
    h1, h2, h3 { color: #1E3A8A !important; font-family: 'Helvetica', sans-serif; }
    
    /* Tarjetas de métricas */
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border-left: 5px solid #D4AF37; /* Borde Dorado */
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    
    /* Color de los textos de métricas */
    div[data-testid="stMetricValue"] { color: #1E3A8A !important; }
    
    /* Estilo para el Sidebar */
    [data-testid="stSidebar"] { background-color: #1E3A8A; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Botones en dorado */
    .stButton>button {
        background-color: #D4AF37;
        color: white;
        border-radius: 20px;
        border: none;
        width: 100%;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZAR MOTOR ---
ia = TenderModule()

# --- MENÚ LATERAL (SIDEBAR) ---
with st.sidebar:
    st.title("🛡️ SIEL-PRO")
    st.divider()
    opcion = st.radio("Navegación", ["📊 Resumen de Evaluación", "📄 Documentos", "🔍 Análisis de Riesgos", "📜 Historial"])
    st.divider()
    clave = st.text_input("Clave de Acceso", type="password")

# --- CUERPO PRINCIPAL ---
if clave == "1234":
    st.title("Resumen de Evaluación")
    
    # Fila de métricas (Puntuación, Clasificación, Probabilidad)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="PUNTUACIÓN TOTAL", value="92.4 / 100")
    with col2:
        st.metric(label="CLASIFICACIÓN", value="A", delta="Muy Competitiva")
    with col3:
        st.metric(label="PROBABILIDAD DE ÉXITO", value="92%", delta="Muy Alta")

    st.divider()

    # Sección de Gráficos y Detalles
    c1, c2 = st.columns([2, 1])

    with c1:
        st.subheader("📊 Evaluación por Criterio")
        # Simulando las barras de la imagen
        st.write("Experiencia del Oferente (95%)")
        st.progress(0.95)
        st.write("Capacidad Técnica (90%)")
        st.progress(0.90)
        st.write("Metodología y Plan de Trabajo (93%)")
        st.progress(0.93)
        st.write("Sostenibilidad y ESG (90%)")
        st.progress(0.90)

    with c2:
        st.subheader("⚠️ Análisis de Riesgos")
        st.info("**MEDIO:** Se recomienda fortalecer evidencia técnica.")
        st.success("**BAJO:** Garantías y seguros cumplen.")
        st.success("**BAJO:** Plazo de ejecución óptimo.")
        
        st.divider()
        st.subheader("📂 Cargar Nuevo Pliego")
        archivo = st.file_uploader("Subir PDF", type="pdf", label_visibility="collapsed")
        if st.button("🚀 ANALIZAR AHORA"):
            st.balloons()
else:
    st.warning("🔒 Ingrese la clave en el menú lateral para ver el Dashboard.")
