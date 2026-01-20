# 🚘 Tasación Inteligente de Vehículos BMW (Machine Learning)

Este proyecto consiste en una aplicación web completa que utiliza algoritmos de Aprendizaje Automático (Machine Learning) para predecir el precio de mercado de vehículos BMW de segunda mano. La herramienta permite a los usuarios introducir características técnicas del coche y recibir una estimación precisa en tiempo real.

## 📋 Descripción del Proyecto

El sistema ha sido desarrollado siguiendo el ciclo de vida completo de un proyecto de Ciencia de Datos:
1.  **Entrenamiento (Fase 1):** Análisis de datos, preprocesamiento con Pipelines y comparación de modelos (Regresión Lineal, Random Forest y Gradient Boosting).
2.  **Optimización:** Ajuste de hiperparámetros (Hyperparameter Tuning) y Validación Cruzada para asegurar la robustez del modelo.
3.  **Despliegue (Fase 2):** Implementación de una interfaz web amigable conectada a un backend en Flask.

## 🛠️ Tecnologías Utilizadas

El proyecto utiliza las siguientes librerías y herramientas:

* **Lenguaje:** Python 3.9+
* **Web Framework:** Flask (Backend)
* **Frontend:** HTML5, CSS3 (Diseño Responsivo)
* **Machine Learning:** Scikit-Learn (RandomForestRegressor, Pipelines, GridSearchCV)
* **Manipulación de Datos:** Pandas, NumPy
* **Persistencia:** Joblib (Carga y guardado de modelos)

## 📂 Estructura del Proyecto

Para que la aplicación funcione correctamente, los archivos están organizados de la siguiente manera:

```text
/proyecto_bmw
│
├── app.py                      # Código principal del servidor (Backend)
├── bmw.csv                     # Dataset (necesario para cargar los modelos en el formulario)
├── modelo_bmw_pipeline.joblib  # Modelo entrenado exportado
├── requirements.txt            # Lista de dependencias
├── README.md                   # Documentación del proyecto
├── BMW_FASE_1.ipynb            # Notebook de entrenamiento y análisis
│
└── templates/
    └── index.html              # Interfaz web (Frontend)

```

> **Nota:** Es importante que `index.html` esté dentro de una carpeta llamada `templates` para que Flask lo encuentre.

## 🚀 Instrucciones de Ejecución

Sigue estos pasos para desplegar la aplicación en tu entorno local:

### 1. Preparación del entorno

Abre una terminal en la carpeta del proyecto e instala las dependencias necesarias:

```bash
pip install -r requirements.txt

```

*(Si no tienes el archivo requirements.txt, las librerías principales son: flask, pandas, scikit-learn, joblib)*

### 2. Ejecución del servidor

Ejecuta el archivo principal de la aplicación:

```bash
python app.py

```

Deberías ver un mensaje indicando que el servidor está corriendo (generalmente en `http://127.0.0.1:8080` o `http://localhost:8080`).

### 3. Uso de la aplicación

1. Abre tu navegador web e ingresa la dirección local mostrada en la terminal.
2. Completa el formulario con los datos del vehículo (Modelo, Año, Kilometraje, etc.).
3. Haz clic en **"Calcular Valor Estimado"**.
4. El sistema mostrará el precio predicho en pantalla.

## 📊 Sobre el Modelo de Predicción

El modelo final seleccionado es un **Random Forest Regressor**.

* **Justificación:** Tras comparar métricas (MAE, MSE, R²) con otros algoritmos como Regresión Lineal, el Random Forest ofreció el mejor equilibrio entre precisión y generalización.
* **Entrenamiento:** Se utilizó el 80% de los datos para entrenamiento y 20% para test.
* **Validación:** Se aplicó Validación Cruzada (Cross-Validation) de 5 pliegues para evitar el sobreajuste.

---

### Extra: `requirements.txt`
Para que la instrucción `pip install -r requirements.txt` del README funcione, crea también un archivo llamado `requirements.txt` y pega esto dentro:

```text
flask
pandas
numpy
scikit-learn
joblib

