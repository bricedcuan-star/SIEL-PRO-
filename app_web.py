import streamlit as st
import google.generativeai as genai
import os
from PyPDF2 import PdfReader

# 1. Configuración de la Página
st.set_page_config(page_title="SIEL Pro - Sistema Inteligente", layout="wide")

# 2. Estilos Corporativos (Azul y Dorado)
st.markdown("""
    <style>
    .main { background-color: #f4f7f9; }
    [data-testid="stSidebar"] { background-color: #1E3A8A; }
    [data-testid="stSidebar"] * { color: white !important; }
    h1, h2, h3 { color: #1E3A8A !important; }
    .stButton>button { 
        border: 2px solid #D4AF37; 
        color: #1E3A8A; 
        font-weight: bold; 
        width: 100%;
        border-radius: 10px;
    }
    .resaltado {
        border-left: 10px solid #D4AF37;
        padding: 20px;
        background: white;
        border-radius: 5px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        white-space: pre-wrap;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica de la IA (Ahora lee los SECRETS correctamente)
class SIELBrain:
    def __init__(self):
        # Buscamos la clave en los Secrets de Streamlit
        api_key = st.secrets.get("GEMINI_API_KEY")
        
        if api_key:
            # Forzamos la configuración para evitar el error v1beta
            genai.configure(api_key=api_key.strip())
            # Usamos el nombre del modelo sin sufijos raros
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            st.error("🔑 Error: No se detecta la clave 'GEMINI_API_KEY' en los Secrets.")

    def consultar(self, prompt, texto):
        try:
            # Enviamos el contenido. Si el PDF es muy largo, Gemini 1.5 lo maneja bien.
            # Limitamos a 50k caracteres para asegurar rapidez
            contenido = f"{prompt}\n\nTEXTO DEL PLIEGO:\n{texto[:50000]}"
            
            # El truco: No especificar la versión de la API en la llamada
            response = self.model.generate_content(contenido)
            return response.text
        except Exception as e:
            # Si el error persiste, probamos con el modelo Pro automático
            try:
                model_alt = genai.GenerativeModel('gemini-pro')
                response = model_alt.generate_content(f"{prompt}\n\nTEXTO:\n{texto[:20000]}")
                return response.text
            except:
                return f"❌ Error de conexión con Google: {str(e)}. Intenta reiniciar la App."

# Inicializamos la IA
try:
    siel_ia = SIELBrain()
    motor_listo = True
except Exception as e:
    st.error(f"Error al conectar con la IA: {e}")
    motor_listo = False

# 4. Barra Lateral
with st.sidebar:
    st.title("📂 SIEL Pro")
    st.markdown("---")
    clave_acceso = st.text_input("Clave de Acceso", type="password")
    
    if clave_acceso == "SIEL_2026*Pro":
        st.success("Acceso Concedido")
        modulo = st.radio("Menú de Estrategia", [
            "🔍 Lectura de Pliegos",
            "📊 Viabilidad del Proceso",
            "⚠️ Evaluación de Riesgos",
            "🏆 Simulador de Puntuación",
            "🤖 Asistente IA"
        ])
    else:
        if clave_acceso:
            st.error("Clave incorrecta")
        modulo = None
    
    st.markdown("---")
    st.info("Versión 1.0 - Desarrollado por Jenny")

# 5. Ejecución de Módulos
if modulo:
    st.title(f"{modulo}")
    archivo = st.file_uploader("Sube el pliego de condiciones (PDF)", type="pdf")

    if archivo and motor_listo:
        if st.button("🚀 INICIAR ANÁLISIS ESTRATÉGICO"):
            with st.spinner("SIEL Pro está leyendo el pliego..."):
                try:
                    # Leemos el PDF
                    reader = PdfReader(archivo)
                    texto_pdf = ""
                    for page in reader.pages:
                        texto_pdf += page.extract_text()
                    
                    # Configuramos el prompt según el módulo elegido
                    if modulo == "🔍 Lectura de Pliegos":
                        prompt = "Extrae: Objeto, Presupuesto, Fechas clave e Indicadores Financieros (Liquidez, Endeudamiento)."
                    elif modulo == "📊 Viabilidad del Proceso":
                        prompt = "Analiza si este proceso es viable financieramente y qué tan difícil es cumplir los requisitos."
                    elif modulo == "⚠️ Evaluación de Riesgos":
                        prompt = "Busca cláusulas peligrosas, multas o requisitos que parezcan 'pliegos sastre'."
                    else:
                        prompt = "Resume los puntos más importantes para decidir si participamos o no."

                    # Llamada a la IA
                    resultado = siel_ia.consultar(prompt, texto_pdf)
                    
                    st.subheader("Dictamen de la IA")
                    st.markdown(f'<div class="resaltado">{resultado}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Hubo un problema al leer el PDF: {e}")
    else:
        st.info("📩 Sube un archivo PDF para que la IA lo analice.")
else:
    st.title("Bienvenido a SIEL Pro")
    st.warning("🔒 Ingrese la clave de acceso en la barra lateral.")
