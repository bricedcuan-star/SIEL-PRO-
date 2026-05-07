<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SIEL PRO - Inteligencia en Licitaciones</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <style>
        :root {
            --siel-navy: #051937;
            --siel-gold: #c29a43;
            --siel-gold-light: #d4af37;
            --siel-bg: #f8fafc;
            --siel-white: #ffffff;
            --siel-text: #1e293b;
            --siel-gray: #64748b;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--siel-bg);
            font-family: 'Poppins', sans-serif;
            color: var(--siel-text);
            padding: 40px 20px;
        }

        .dashboard {
            max-width: 1200px;
            margin: 0 auto;
            background: var(--siel-white);
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(5, 25, 55, 0.08);
            overflow: hidden;
            border-top: 6px solid var(--siel-navy);
        }

        /* Cabecera */
        header {
            background-color: var(--siel-navy);
            padding: 30px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 4px solid var(--siel-gold);
        }

        .header-titles h1 {
            color: var(--siel-white);
            font-family: 'Montserrat', sans-serif;
            font-size: 24px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .header-titles p {
            color: var(--siel-gold);
            font-size: 12px;
            font-weight: 300;
            margin-top: 4px;
            text-transform: uppercase;
        }

        .logo-box img {
            height: 60px;
            width: auto;
        }

        /* Contenido principal */
        .content {
            padding: 40px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
        }

        h2 {
            font-size: 15px;
            color: var(--siel-navy);
            border-left: 4px solid var(--siel-gold);
            padding-left: 12px;
            margin-bottom: 20px;
            text-transform: uppercase;
            font-weight: 600;
        }

        .card {
            background: var(--siel-white);
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 25px;
            transition: all 0.3s ease;
        }

        .card:hover {
            border-color: var(--siel-gold);
        }

        /* Formularios */
        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin-bottom: 15px;
        }

        .form-group {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        label {
            font-size: 10px;
            font-weight: 700;
            color: var(--siel-gray);
            text-transform: uppercase;
        }

        input, select, textarea {
            padding: 10px;
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            font-size: 12px;
            background-color: #f8fafc;
            color: var(--siel-text);
            width: 100%;
        }

        input:focus, select:focus, textarea:focus {
            outline: none;
            border-color: var(--siel-gold);
            box-shadow: 0 0 0 3px rgba(194, 154, 67, 0.15);
        }

        textarea {
            resize: vertical;
            min-height: 100px;
        }

        /* Prompt */
        .prompt-box {
            background-color: var(--siel-navy);
            color: var(--siel-white);
            border-radius: 8px;
            padding: 20px;
            margin-top: 10px;
        }

        .prompt-text {
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px dashed var(--siel-gold);
            padding: 12px;
            font-family: monospace;
            font-size: 11px;
            color: #cbd5e1;
            height: 90px;
            overflow-y: auto;
            margin: 10px 0;
            border-radius: 4px;
        }

        /* Buscadores */
        .links-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-top: 10px;
        }

        .link-tile {
            background-color: #f1f5f9;
            border: 1px solid #e2e8f0;
            padding: 10px 5px;
            border-radius: 6px;
            text-align: center;
            text-decoration: none;
            color: var(--siel-navy);
            font-size: 10px;
            font-weight: 600;
            transition: 0.2s;
            text-transform: uppercase;
        }

        .link-tile:hover {
            background-color: var(--siel-gold);
            color: var(--siel-white);
            border-color: var(--siel-gold);
        }

        /* Botones */
        .btn {
            border: none;
            border-radius: 6px;
            padding: 12px 20px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            cursor: pointer;
            transition: all 0.2s;
        }

        .btn-gold {
            background-color: var(--siel-gold);
            color: var(--siel-white);
            width: 100%;
        }

        .btn-gold:hover {
            background-color: var(--siel-gold-light);
        }

        .btn-navy {
            background-color: var(--siel-navy);
            color: var(--siel-white);
            border: 1px solid var(--siel-gold);
        }

        .btn-navy:hover {
            background-color: #082554;
        }

        .btn-choice {
            background: var(--siel-white);
            border: 1px solid var(--siel-gold);
            color: var(--siel-gold);
            flex: 1;
            padding: 10px;
        }

        .btn-choice:hover {
            background: var(--siel-gold);
            color: var(--siel-white);
        }

        footer {
            text-align: center;
            font-size: 10px;
            color: var(--siel-gray);
            padding: 20px 40px;
            background-color: #f8fafc;
            border-top: 1px solid #e2e8f0;
        }

        /* Estilos optimizados para que el PDF se vea ordenado y compacto */
        #contenedorInformePdf {
            font-family: 'Poppins', sans-serif;
            color: #051937;
            padding: 15mm;
            background: #ffffff;
            width: 100%;
            display: none;
        }
    </style>
</head>
<body>

<div class="dashboard">
    <header>
        <div class="header-titles">
            <h1>Módulo de Análisis — Fase 1</h1>
            <p>Sistema Inteligente de Evaluación de Licitaciones</p>
        </div>
        <div class="logo-box">
            <img src="logo_siel_final.jpg" alt="Logo SIEL" onerror="this.src='https://placehold.co/150x50/051937/c29a43?text=SIEL+PRO'">
        </div>
    </header>

    <div class="content">
        <section class="card">
            <h2>1. Configuración del Proceso</h2>
            <div class="form-grid">
                <div class="form-group">
                    <label>Tipo de Proceso</label>
                    <select id="tipoProceso">
                        <option>Licitación Pública</option>
                        <option>Convocatoria Privada</option>
                        <option>Términos de Referencia Privados</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Sector</label>
                    <select id="sector">
                        <option>Fachadas y Cubiertas</option>
                        <option>Obras Civiles</option>
                        <option>Tecnología</option>
                        <option>Salud</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Modalidad</label>
                    <select id="modalidad">
                        <option>Empresa Individual</option>
                        <option>Consorcio</option>
                        <option>Unión Temporal</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Rol</label>
                    <select id="rol">
                        <option>Contratista</option>
                        <option>Interventor</option>
                        <option>Proveedor</option>
                    </select>
                </div>
            </div>

            <h2 style="margin-top: 30px;">2. Datos del Pliego</h2>
            <div class="form-grid">
                <div class="form-group" style="grid-column: span 2;">
                    <label>Número de Proceso</label>
                    <input type="text" id="numProceso" placeholder="Ej: PH-2024-001">
                </div>
                <div class="form-group" style="grid-column: span 2;">
                    <label>Entidad / Cliente</label>
                    <input type="text" id="entidad" placeholder="Razón social de la entidad">
                </div>
                <div class="form-group">
                    <label>Presupuesto ($)</label>
                    <input type="number" id="presupuesto" placeholder="0.00">
                </div>
                <div class="form-group">
                    <label>Anticipo (%)</label>
                    <input type="text" id="anticipo" placeholder="Ej: 30%">
                </div>
            </div>

            <div style="margin-top: 35px;">
                <label>Buscadores de Oportunidades</label>
                <div class="links-grid">
                    <a href="https://community.secop.gov.co/" target="_blank" class="link-tile">SECOP II</a>
                    <a href="https://bogota.gov.co/asi-vamos/contratos-y-obras/participa" target="_blank" class="link-tile">Bogotá</a>
                    <a href="https://convocatorias.revistaphcolombia.com/" target="_blank" class="link-tile">Revista PH</a>
                </div>
            </div>
        </section>

        <section class="card" style="display: flex; flex-direction: column;">
            <div class="prompt-box">
                <label style="color: var(--siel-gold);">Prompt Maestro SIEL</label>
                <div class="prompt-text" id="promptMaestro">Actúa como un Consultor Experto SIEL. Analiza el pliego adjunto y extrae los 13 puntos de control:
1. Liquidez
2. Endeudamiento
3. Capital de Trabajo
4. Experiencia General
5. Experiencia Específica
6. Capacidad Residual (K/R)
7. Personal Técnico
8. Visita Técnica
9. Certificación en Alturas
10. Anticipo
11. Forma de Pago
12. SST / Ambiental
13. Riesgos Contractuales

Entrega el dictamen de viabilidad (1 al 10) y justifica las observaciones.</div>
                <button class="btn btn-gold" onclick="copiarPrompt()"><i class="fa-regular fa-copy"></i> Copiar Prompt</button>
            </div>

            <div style="margin-top: 25px;">
                <label>Paso 1: ¿Qué tipo de PDF vas a subir a la IA?</label>
                <div style="display: flex; gap: 10px; margin-top: 8px;">
                    <button class="btn btn-choice" onclick="alert('Seleccionado Formato Texto: Adjunta tu PDF seleccionable en tu IA de preferencia y utiliza el prompt.')">Formato Texto</button>
                    <button class="btn btn-choice" onclick="alert('Seleccionado Formato Imagen: Toma capturas de los requisitos técnicos y financieros o utiliza OCR antes de usar el prompt.')">Formato Imagen</button>
                </div>
            </div>

            <div style="margin-top: 25px; flex-grow: 1; display: flex; flex-direction: column;">
                <label>Paso 2: Pega el resultado del análisis de la IA</label>
                <textarea id="iaResult" style="margin-top: 8px; flex-grow: 1;" placeholder="Pega aquí el resultado del análisis de tu IA..."></textarea>
            </div>

            <button class="btn btn-navy" style="margin-top: 20px;" onclick="descargarInformePDF()">
                <i class="fa-solid fa-file-pdf"></i> Descargar Informe de Viabilidad
            </button>
        </section>
    </div>

    <footer>
        Sistema SIEL PRO — Inteligencia en Evaluación de Licitaciones © 2026
    </footer>
</div>

<div id="contenedorInformePdf">
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 4px solid #c29a43; padding-bottom: 10px; margin-bottom: 15px;">
        <div>
            <h1 style="font-size: 16pt; text-transform: uppercase; margin: 0; color: #051937;">Informe de Viabilidad SIEL</h1>
            <p style="color: #c29a43; font-weight: bold; font-size: 8pt; margin-top: 4px;">MÓDULO 1 - ESTRATEGIA DE LICITACIONES</p>
        </div>
        <img src="logo_siel_final.jpg" style="height: 40px;" alt="Logo SIEL">
    </div>

    <h2 style="font-size: 10.5pt; color: #051937; border-left: 3px solid #c29a43; padding-left: 8px; margin-bottom: 8px; text-transform: uppercase;">1. Datos del Proceso</h2>
    <div style="background-color: #f8fafc; padding: 10px; border: 1px solid #e2e8f0; border-radius: 6px; margin-bottom: 12px; font-size: 9pt;">
        <p style="margin-bottom: 4px;"><strong>Número de proceso:</strong> <span id="pdfNumProceso">S/N</span></p>
        <p style="margin-bottom: 4px;"><strong>Entidad:</strong> <span id="pdfEntidad">No especificada</span></p>
        <p style="margin-bottom: 4px;"><strong>Tipo y Sector:</strong> <span id="pdfTipoSector">General</span></p>
        <p style="margin-bottom: 0;"><strong>Presupuesto:</strong> $<span id="pdfPresupuesto">0.00</span></p>
    </div>

    <h2 style="font-size: 10.5pt; color: #051937; border-left: 3px solid #c29a43; padding-left: 8px; margin-bottom: 8px; text-transform: uppercase;">2. Matriz de los 13 Puntos de Control SIEL</h2>
    <table style="width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 8.5pt;">
        <thead>
            <tr style="background-color: #f1f5f9;">
                <th style="border: 1px solid #cbd5e1; padding: 5px;">#</th>
                <th style="border: 1px solid #cbd5e1; padding: 5px;">Punto de Control</th>
                <th style="border: 1px solid #cbd5e1; padding: 5px;">Estado</th>
                <th style="border: 1px solid #cbd5e1; padding: 5px;">Riesgo</th>
            </tr>
        </thead>
        <tbody>
            <tr><td style="border: 1px solid #cbd5e1; padding: 4px;">1</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Liquidez</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Validación IA</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Medio</td></tr>
            <tr><td style="border: 1px solid #cbd5e1; padding: 4px;">2</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Endeudamiento</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Validación IA</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Alto</td></tr>
            <tr><td style="border: 1px solid #cbd5e1; padding: 4px;">3</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Capital de Trabajo</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Validación IA</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Medio</td></tr>
            <tr><td style="border: 1px solid #cbd5e1; padding: 4px;">4</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Experiencia General</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Validación IA</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Bajo</td></tr>
            <tr><td style="border: 1px solid #cbd5e1; padding: 4px;">5</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Experiencia Específica</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Validación IA</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Alto</td></tr>
            <tr><td style="border: 1px solid #cbd5e1; padding: 4px;">6</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Capacidad Residual</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Validación IA</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Medio</td></tr>
            <tr><td style="border: 1px solid #cbd5e1; padding: 4px;">7</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Personal Técnico</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Validación IA</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Medio</td></tr>
            <tr><td style="border: 1px solid #cbd5e1; padding: 4px;">8</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Visita Técnica</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Validación IA</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Alto</td></tr>
            <tr><td style="border: 1px solid #cbd5e1; padding: 4px;">9</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Certificación en Alturas</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Validación IA</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Alto</td></tr>
            <tr><td style="border: 1px solid #cbd5e1; padding: 4px;">10</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Anticipo</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Validación IA</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Bajo</td></tr>
            <tr><td style="border: 1px solid #cbd5e1; padding: 4px;">11</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Forma de Pago</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Validación IA</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Medio</td></tr>
            <tr><td style="border: 1px solid #cbd5e1; padding: 4px;">12</td><td style="border: 1px solid #cbd5e1; padding: 4px;">SST / Ambiental</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Validación IA</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Bajo</td></tr>
            <tr><td style="border: 1px solid #cbd5e1; padding: 4px;">13</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Riesgos Contractuales</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Validación IA</td><td style="border: 1px solid #cbd5e1; padding: 4px;">Alto</td></tr>
        </tbody>
    </table>

    <h2 style="font-size: 10.5pt; color: #051937; border-left: 3px solid #c29a43; padding-left: 8px; margin-top: 15px; margin-bottom: 8px; text-transform: uppercase;">3. Veredicto y Justificación Estratégica</h2>
    <div style="background-color: #fef9c3; border-left: 4px solid #c29a43; padding: 10px; font-size: 9pt; line-height: 1.4;">
        <span id="pdfIaResult">No se incluyó análisis.</span>
    </div>

    <div style="text-align: center; font-size: 7.5pt; color: #64748b; margin-top: 30px; border-top: 1px solid #cbd5e1; padding-top: 10px;">
        SIEL PRO © 2026 | Sistema Inteligente de Evaluación de Licitaciones.
    </div>
</div>

<script>
    function copiarPrompt() {
        const promptText = document.getElementById("promptMaestro").innerText;
        navigator.clipboard.writeText(promptText);
        alert("Prompt copiado al portapapeles.");
    }

    function descargarInformePDF() {
        // Cargar los valores actuales del formulario dentro del informe oculto
        document.getElementById("pdfNumProceso").innerText = document.getElementById("numProceso").value || "S/N";
        document.getElementById("pdfEntidad").innerText = document.getElementById("entidad").value || "No especificada";
        document.getElementById("pdfTipoSector").innerText = document.getElementById("tipoProceso").value + " / " + document.getElementById("sector").value;
        document.getElementById("pdfPresupuesto").innerText = document.getElementById("presupuesto").value || "0.00";

        const iaTexto = document.getElementById("iaResult").value || "Sin observaciones.";
        document.getElementById("pdfIaResult").innerHTML = iaTexto.replace(/\n/g, '<br>');

        const elementoInforme = document.getElementById("contenedorInformePdf");
        
        // Configuraciones de visualización para asegurar la generación correcta de PDF compacto
        elementoInforme.style.display = "block";

        const opciones = {
            margin:       10,
            filename:     `Informe_Viabilidad_${document.getElementById("numProceso").value || 'S_N'}.pdf`,
            image:        { type: 'jpeg', quality: 0.98 },
            html2canvas:  { scale: 2 },
            jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
        };

        // Generar el archivo y descargarlo
        html2pdf().set(opciones).from(elementoInforme).save().then(() => {
            // Ocultar de nuevo la plantilla oculta
            elementoInforme.style.display = "none";
        });
    }
</script>
</body>
</html>
