class TenderModule:
    def __init__(self):
        # 1. PEGA TU NUEVA LLAVE AQUÍ
        raw_key = "AIzaSyARZgTTSfCuH-hHtEPAns062tC3Nzn-QoQ"
        
        # 2. LIMPIEZA AUTOMÁTICA (Esto quita espacios invisibles)
        api_key = raw_key.strip()
        
        # 3. CONFIGURACIÓN
        genai.configure(api_key=api_key)
        
        # Usamos este nombre que es el más compatible actualmente
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
