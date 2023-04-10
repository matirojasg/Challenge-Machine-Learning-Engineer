import requests
import json

# Datos del vuelo a predecir.
input_data = {'OPERA': 'Aeromexico', 'SIGLADES': 'MIAMI', 'MES': 7, 'DIANOM': 'Viernes', 'temporada_alta': 1, 'periodo_dia': 'mañana', 'hora': 8, 'vuelos_paralelos': 5}

# Hacer una solicitud POST a la ruta '/predict'.
url = 'http://localhost:8000/predict'
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=json.dumps(input_data), headers=headers)

# Imprimir la respuesta
print(response.json())