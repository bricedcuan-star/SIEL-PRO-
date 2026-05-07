# Importamos las herramientas de la carpeta modules
from modules.tender_analyzer import TenderModule
from modules.risk_analyzer import RiskModule

# Creamos los asistentes
asistente_licitacion = TenderModule()
asistente_riesgos = RiskModule()

print("--- BIENVENIDO A SIEL PRO ---")
password = input("🔑 Ingrese su clave de acceso: ")

if asistente_riesgos.validar_acceso(password):
    print("\n✅ ACCESO TOTAL CONCEDIDO")
    
    # Aquí el sistema usa el Módulo 1
    print("\n[EJECUTANDO MÓDULO 1: ANÁLISIS DE LICITACIÓN]")
    # asistente_licitacion.analizar(...) 
    
    # Aquí el sistema usa el Módulo 2
    print("\n[EJECUTANDO MÓDULO 2: ANÁLISIS DE RIESGOS]")
    # asistente_riesgos.analizar_riesgos(...)
    
else:
    print("❌ Clave incorrecta.")
