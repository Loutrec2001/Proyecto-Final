import requests
import pandas as pd


# Especifica los parámetros de la solicitud
url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
parameters = {
    'format': 'geojson',
    'starttime': '2013-06-27',  # Hace 10 años a partir de la fecha actual
    'endtime': '2023-06-27',  # Fecha actual
    'minmagnitude': 2.5,
    'latitude': 36.8,  # Latitud de California
    'longitude': -119.41,  # Longitud de California
    'maxradiuskm': 300  # Radio en kilómetros para cubrir California, ajusta según sea necesario
}

# Realiza la solicitud a la API
response = requests.get(url, params=parameters)

# Obtén los datos de respuesta en formato JSON
data = response.json()

# Crea una lista para almacenar los datos de los sismos
earthquake_data = []

# Itera sobre los eventos sísmicos y extrae todas las columnas relevantes
for feature in data['features']:
    properties = feature['properties']
    geometry = feature['geometry']
    
    earthquake = {
        'Fecha': properties['time'],
        'Magnitud': properties['mag'],
        'Profundidad': geometry['coordinates'][2],
        'Ubicación': properties['place'],
        'Latitud': geometry['coordinates'][1],
        'Longitud': geometry['coordinates'][0],
        'Tipo': properties['type'],
        'Estatus': properties['status'],
        'Tsunami': properties['tsunami'],
        'Alerta': properties['alert'],
        'Significancia': properties['sig'],
        'Tipo de Origen': properties['nst'],
        'Fuente': properties['net']
    }
    
    earthquake_data.append(earthquake)

# Crea un DataFrame con los datos obtenidos
df = pd.DataFrame(earthquake_data)

# Guarda el DataFrame en un archivo CSV
df.to_csv(f'C:\\Users\\KEVIN\\Desktop\\Proyecto 3\\California.csv', index=False)
