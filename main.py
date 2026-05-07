from modules.risk_analyzer import RiskModule

# Iniciamos el motor de riesgos
siel_riesgos = RiskModule()

print("=========================================")
print("   SISTEMA SIEL PRO - FASE 2 (RIESGOS)   ")
print("=========================================")

# 1. El sistema pide la clave al usuario
mi_clave = input("🔑 Ingrese su contraseña de acceso SIEL: ")

# 2. Verificamos la clave
if siel_riesgos.validar_acceso(mi_clave):
    print("\n✅ ACCESO CONCEDIDO. Iniciando motor de búsqueda...")
    
    # Texto de ejemplo para probar (Simulando un pliego de condiciones)
    texto_ejemplo = "El contrato exige garantías separadas y tiene multas del 10%."
    
    # 3. Ejecutamos el análisis
    informe = siel_riesgos.analizar_riesgos(texto_ejemplo)
    
    print("\n--- INFORME DE HALLAZGOS ---")
    for hallazgo in informe["CRITICO"]:
        print(f"🔴 CRÍTICO: {hallazgo}")
    for hallazgo in informe["FORTALEZA"]:
        print(f"🟢 FORTALEZA: {hallazgo}")
        
else:
    print("\n❌ ACCESO DENEGADO. Por favor, adquiera su licencia.")
