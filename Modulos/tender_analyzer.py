class TenderModule:
    def __init__(self):
        # Datos de referencia para alertas financieras
        self.limite_presupuesto = 500000000 # 500 Millones
        
    def analizar_proceso_completo(self, datos_licitacion):
        """Realiza el escaneo completo de la licitación"""
        informe_m1 = {
            "viabilidad": "PENDIENTE",
            "alertas": [],
            "datos_extraidos": datos_licitacion
        }
        
        # 1. Validación de Presupuesto
        presupuesto = datos_licitacion.get("presupuesto", 0)
        if presupuesto > self.limite_presupuesto:
            informe_m1["alertas"].append("⚠️ PRESUPUESTO ALTO: Requiere consorcio o mayor capacidad K.")
        
        # 2. Análisis del Objeto (Sectorización)
        objeto = datos_licitacion.get("objeto", "").upper()
        if "FACHADA" in objeto or "ALTURAS" in objeto:
            informe_m1["sector"] = "FACHADAS Y CUBIERTAS"
            informe_m1["alertas"].append("🛠 SECTOR DETECTADO: Aplicando reglas técnicas de fachadas.")
        
        # 3. Veredicto Inicial
        if presupuesto > 0 and len(objeto) > 10:
            informe_m1["viabilidad"] = "APROBADO PARA RIESGOS"
            
        return informe_m1
