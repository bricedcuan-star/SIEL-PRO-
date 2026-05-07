import hashlib

class RiskModule:
    def __init__(self):
        # La huella digital de la contraseña maestra: SIEL2026
        self.__secret_key = "d74f26048d689617304f475631742468352614b745484501a3408936" 

    def validar_acceso(self, password):
        """Verifica si la clave ingresada es correcta"""
        input_hash = hashlib.sha256(password.encode()).hexdigest()
        return input_hash == self.__secret_key

    def analizar_riesgos(self, texto_del_pliego):
        """Detecta amenazas contractuales automáticamente"""
        hallazgos = {"CRITICO": [], "MODERADO": [], "FORTALEZA": []}
        
        texto = texto_del_pliego.lower()
        
        # Lógica de detección (Fase 2 - Heurística)
        if "multa" in texto:
            hallazgos["CRITICO"].append("⚠️ Cláusulas de multas/penalidades detectadas.")
        
        if "garantias_separadas" in texto or "pólizas independientes" in texto:
            hallazgos["CRITICO"].append("🔴 TRAMPA: Exigencia de pólizas separadas (Materiales/Mano de obra).")
            
        if "anticipo" in texto and "20%" in texto:
            hallazgos["FORTALEZA"].append("🟢 FLUJO DE CAJA: Anticipo favorable identificado.")

        return hallazgos
