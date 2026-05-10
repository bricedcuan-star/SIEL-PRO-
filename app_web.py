import streamlit as st

# Configuración
st.set_page_config(page_title="SIEL-PRO Dashboard", layout="wide")

# --- ESTILOS MEJORADOS ---
st.markdown("""
    <style>
    .stButton>button { background-color: #D4AF37; color: white; font-weight: bold; }
    .buscador-box { 
        padding: 10px; border: 1px solid #1E3A8A; border-radius: 5px; 
        text-align: center; color: #1E3A8A; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ SIEL-PRO")
    clave = st.text_input("Clave de Acceso", type="password")

if clave == "1234":
    st.title("Módulo de Análisis — Fase 1")

    # --- SECCIÓN 1: BUSCADORES ---
    st.subheader("🌐 Buscadores de Oportunidades")
    b1, b2, b3 = st.columns(3)
    with b1: st.markdown('<div class="buscador-box">SECOP II</div>', unsafe_allow_html=True)
    with b2: st.markdown('<div class="buscador-box">BOGOTÁ</div>', unsafe_allow_html=True)
    with b3: st.markdown('<div class="buscador-box">REVISTA PH</div>', unsafe_allow_html=True)

    st.divider()

    # --- SECCIÓN 2: LOS 13 PUNTOS SIEL ---
    st.subheader("📋 Puntos de Control SIEL")
    
    # Creamos dos columnas para mostrar los puntos de forma organizada
    col_puntos1, col_puntos2 = st.columns(2)
    
    puntos = [
        "1. Liquidez", "2. Endeudamiento", "3. Capital de Trabajo",
        "4. Experiencia General", "5. Experiencia Específica", "6. Capacidad Residual (K/R)",
        "7. Personal Técnico", "8. Visita Técnica", "9. Certificación Alturas",
        "10. Anticipo", "11. Forma de Pago", "12. SST y Ambiental", "13. Riesgos Contractuales"
    ]

    for i, punto in enumerate(puntos):
        target_col = col_puntos1 if i < 7 else col_puntos2
        target_col.checkbox(punto, value=True) # Aparecerán marcados si la IA los detecta

    st.divider()

    # --- SECCIÓN 3: ACCIONES ---
    c_act1, c_act2 = st.columns(2)
    with c_act1:
        if st.button("🚀 INICIAR ESCANEO DE IA"):
            st.info("La IA está analizando los 13 puntos en el pliego...")
    
    with c_act2:
        # Aquí es donde pondremos la función para crear el PDF
        if st.button("📄 DESCARGAR INFORME DE VIABILIDAD"):
            st.success("Generando informe técnico basado en los 13 puntos...")

else:
    st.info("🔒 Por favor ingrese la clave para acceder al sistema.")
