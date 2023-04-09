from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import uvicorn
import pandas as pd
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('models/model.pkl', 'rb'))
original_columns = pickle.load(open('models/columns.pkl', 'rb'))

# Definir las columnas categóricas y numéricas
cat_cols = ['OPERA', 'SIGLADES', 'DIANOM', 'periodo_dia']
num_cols = ['MES', 'temporada_alta', 'hora', 'vuelos_paralelos']

# Definir la clase que representa el modelo de entrada
class InputModel(BaseModel):
    MES: int
    temporada_alta: int
    hora: int
    vuelos_paralelos: int
    OPERA: str
    SIGLADES: str
    DIANOM: str
    periodo_dia: str

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Ruta de la API REST para hacer predicciones
@app.post('/predict')
def predict(input_data: InputModel):
    # Crear un dataframe a partir de los datos de entrada
    input_df = pd.DataFrame([input_data.dict()])

    # Aplicar el preprocesamiento a los datos de entrada
    X = pd.get_dummies(input_df, columns=cat_cols)

    scaler = StandardScaler() 
    X[num_cols] = scaler.fit_transform(X[num_cols])

    # Realizar la predicción utilizando el modelo
    X = X.reindex(labels = original_columns, axis = 1, fill_value = 0)
    prediction = model.predict(X)[0]
    proba = model.predict_proba(X).tolist()
    proba = list(map(lambda x: round(x,2), proba[0]))

    # Devolver la predicción en formato JSON
    return {
        'prediction': int(prediction),
        'proba': proba
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

