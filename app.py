from flask import Flask, request, render_template
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Obtener la ruta absoluta del directorio actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construir las rutas completas
MODEL_PATH = os.path.join(BASE_DIR, "modelo_bmw_pipeline.joblib")
CSV_PATH = os.path.join(BASE_DIR, "bmw.csv")

model = joblib.load(MODEL_PATH)
df_bmw = pd.read_csv(CSV_PATH)

print("Cargando modelo y datos...")
model = joblib.load(MODEL_PATH)

# Cargar el CSV una sola vez para obtener los modelos únicos
df_bmw = pd.read_csv(CSV_PATH)
# Obtenemos la lista de modelos ordenada alfabéticamente
unique_models = sorted(df_bmw["model"].unique())


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    # Valores por defecto para rellenar el formulario si hay un POST
    form_data = {}

    if request.method == "POST":
        try:
            # Guardamos los datos del formulario para volver a mostrarlos
            form_data = request.form

            # Recibir los datos
            val_model = request.form["model"]
            val_year = int(request.form["year"])
            val_transmission = request.form["transmission"]
            val_mileage = int(request.form["mileage"])
            val_fuelType = request.form["fuelType"]
            val_tax = int(request.form["tax"])
            val_mpg = float(request.form["mpg"])
            val_engineSize = float(request.form["engineSize"])

            # Crear DataFrame
            input_data = pd.DataFrame(
                [
                    [
                        val_model,
                        val_year,
                        val_transmission,
                        val_mileage,
                        val_fuelType,
                        val_tax,
                        val_mpg,
                        val_engineSize,
                    ]
                ],
                columns=[
                    "model",
                    "year",
                    "transmission",
                    "mileage",
                    "fuelType",
                    "tax",
                    "mpg",
                    "engineSize",
                ],
            )

            # Predecir
            prediction_value = model.predict(input_data)[0]
            prediction = f"{prediction_value:,.2f} €"

        except Exception as e:
            error = f"Error en el cálculo: {str(e)}"

    # Pasamos 'unique_models' al template para rellenar el select
    return render_template(
        "index.html",
        prediction=prediction,
        error=error,
        models=unique_models,
        form=form_data,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
