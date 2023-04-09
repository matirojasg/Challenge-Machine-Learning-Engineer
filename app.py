from flask import Flask, jsonify, request
import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pickle 

app = Flask(__name__)

# Cargar modelo entrenado
model = pickle.load(open('models/model.pkl', 'rb'))
original_columns = pickle.load(open('models/columns.pkl', 'rb'))

# Definir las columnas categóricas y numéricas
cat_cols = ['OPERA', 'SIGLADES', 'DIANOM', 'periodo_dia']
num_cols = ['MES', 'temporada_alta', 'hora', 'vuelos_paralelos']


# Ruta de la API REST para hacer predicciones
@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos de entrada del usuario
    input_data = request.get_json()

    # Crear un dataframe a partir de los datos de entrada
    input_df = pd.DataFrame.from_dict([input_data])
 
    # Aplicar el preprocesamiento a los datos de entrada
    X = pd.get_dummies(input_df, columns=cat_cols)

    scaler = StandardScaler() 
    X[num_cols] = scaler.fit_transform(X[num_cols])

    # Realizar la predicción utilizando el modelo
    X = X.reindex(labels = original_columns, axis = 1, fill_value = 0)
  

    prediction = model.predict(X)[0]

    # Devolver la predicción en formato JSON
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)

