import streamlit as st
from Modulos.tender_analyzer import TenderModule

st.set_page_config(page_title="SIEL-PRO Dashboard", layout="wide")

# --- ESTILOS PERSONALIZADOS (Para que se vea pro) ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- MENÚ LATERAL ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/583/583345.png", width=50) # Icono de ejemplo
    st.title("SIEL-PRO")
    st.radio("Navegación", ["Resumen", "Documentos", "Análisis", "Riesgos"])

# --- CUERPO PRINCIPAL ---
st.header("Resumen de Evaluación")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.metric(label="PUNTUACIÓN TOTAL", value="92.4 / 100", delta="Alta probabilidad")

with col2:
    st.metric(label="CLASIFICACIÓN", value="A", delta="Muy Competitiva")

with col3:
    st.metric(label="PROBABILIDAD DE ÉXITO", value="92%", delta="Muy Alta")

st.divider()

# --- SECCIÓN DE CRITERIOS ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Evaluación por Criterio")
    criterios = {
        "Experiencia del Oferente": 0.95,
        "Capacidad Técnica": 0.90,
        "Metodología": 0.93,
        "Equipo de Trabajo": 0.88
    }
    for nombre, valor in criterios.items():
        st.write(f"{nombre} ({int(valor*100)}%)")
        st.progress(valor)

with col_right:
    st.subheader("Análisis de Riesgos")
    st.warning("⚠️ MEDIO: Requisito de experiencia específica.")
    st.success("✅ BAJO: Garantías y seguros.")
    st.success("✅ BAJO: Plazo de ejecución.")

# --- BOTÓN DE ACCIÓN ---
if st.button("Exportar Informe PDF"):
    st.balloons()
