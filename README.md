# Anonimización y Preservación de Privacidad de Datos para la Toma de Decisiones

Proyecto académico de Ingeniería de Datos correspondiente a la **Unidad 2** de la materia **Software para la Toma de Decisiones** en el **Instituto Tecnológico de Oaxaca (ITO)**.

El objetivo central es transformar y desasociar un conjunto de datos transaccionales hospitalarios y farmacéuticos protegiendo la privacidad de los pacientes conforme a la **Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP)** de México, manteniendo la integridad matemática para el análisis y soporte a la toma de decisiones empresariales (*Business Intelligence*).

---

## 📁 Estructura del Repositorio

```text
anonimizacion_datos/
│
├── generate_names.py        # Clase Persona y generador sintético con nombres/apellidos mexicanos
├── utils.py                 # Funciones de privacidad: masking, hash SHA-256, generalización y truncamiento
├── script.py                # Pipeline principal: ingesta, combinación, anonimización y exportación
├── evaluacion.py            # Análisis gráfico y resolución de preguntas clave para la toma de decisiones
│
├── datos_hospital_originales.csv # Dataset clínico original
├── copia.csv                # Dataset base de trabajo transaccional
├── data_anonima.csv         # Dataset resultante disociado y anonimizado
│
├── n_hombres.csv            # Catálogo de nombres masculinos
├── n_mujeres.csv            # Catálogo de nombres femeninos
├── apellidos.csv            # Catálogo de apellidos de distribución nacional
│
├── evaluacion_resultados.png # Tablero gráfico con las respuestas a las 5 preguntas del negocio
├── reporte_tecnico.tex      # Reporte técnico formal listo para compilar en LaTeX
├── requirements.txt         # Dependencias exactas del proyecto
└── README.md                # Guía de instalación y ejecución
```

---

## 🛠️ Requisitos Previos

- **Python:** Versión `3.12.x` recomendada.
- **Git:** Para clonar y versionar el proyecto.
- **Sistema Operativo:** Compatible con Windows, Linux y macOS.

---

## 🚀 Guía de Instalación y Ejecución Paso a Paso

### 1. Clonar el repositorio
Abre una terminal y clona el proyecto:
```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd anonimizacion_datos
```

### 2. Crear y activar el entorno virtual

- **En Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  & ".\.venv\Scripts\Activate.ps1"
  ```

- **En Linux / macOS (Bash/Zsh):**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Instalar las dependencias
Instala todas las librerías necesarias fijadas en `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Flujo de Ejecución del Pipeline

### Paso 1: Ejecutar la anonimización de datos
Ejecuta el script orquestador para leer `copia.csv`, agregar 40 registros sintéticos balanceados, aplicar las funciones de privacidad y generar el archivo disociado `data_anonima.csv`:

```bash
python script.py
```

*Salida esperada:* Se crea el archivo `data_anonima.csv` con los identificadores protegidos:
- **Nombre:** Enmascarado (`J*** C***** P****`).
- **RFC:** Seudonimizado con hash SHA-256 irreversible de 64 caracteres.
- **Fecha de Nacimiento:** Generalizada a rangos de edad (`18-29`, `30-39`, `40-49`, `50+`).
- **Código Postal:** Truncado a 3 dígitos con máscara ($k$-Anonymity espacial: `310***`, `640***`).

---

### Paso 2: Ejecutar el análisis y toma de decisiones
Ejecuta el módulo de evaluación para resolver las 5 preguntas del negocio y desplegar el tablero visual interactivo:

```bash
python evaluacion.py
```

*Resultado:* 
- Se abre una ventana interactiva de `matplotlib` con un tablero de 5 gráficas (barras y sectores).
- Se guarda automáticamente la imagen de alta resolución en `evaluacion_resultados.png`.

---

## 📊 Preguntas de Negocio Respondidas

| # | Pregunta de Decisión | Hallazgo Analítico |
|---|---|---|
| **P1** | ¿Qué rango de edad compra más en **Farmacia**? | Cohorte **`50+`** (\$18,243.70). |
| **P2** | ¿Qué género compra más en **Cuidado Personal**? | Género **Masculino** (\$25,727.63). |
| **P3** | ¿En qué CP gastan más en **Equipamiento**? | Zona macro **`310***`** (\$16,315.70). |
| **P4** | ¿Cuál es el rango de edad con mayor volumen de ventas totales? | Cohorte **`50+`** (\$55,795.13 en 19 transacciones). |
| **P5** | ¿Qué categoría de producto genera más facturación global? | **`Equipamiento`** (\$51,281.43). |

---

## 📄 Compilación del Reporte Técnico en LaTeX

El archivo `reporte_tecnico.tex` cuenta con la portada oficial del **Instituto Tecnológico de Oaxaca (ITO)** y toda la fundamentación teórica y legal (LFPDPPP).

Para compilarlo a PDF:
- **En Overleaf:** Sube `reporte_tecnico.tex` y `evaluacion_resultados.png` y presiona **Recompile**.
- **En local con TeX Live / MiKTeX:**
  ```bash
  pdflatex reporte_tecnico.tex
  ```

---

## 👤 Información Académica

- **Institución:** Instituto Tecnológico de Oaxaca (ITO)
- **División:** Estudios Profesionales – Ingeniería en Sistemas Computacionales
- **Materia:** Software Para la Toma de Decisiones (08:00 – 09:00 / 7SA)
- **Alumno:** Ángel Raymundo Pablo Zenón
- **Docente:** NOMBRE
