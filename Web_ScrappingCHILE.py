import requests

# URL de la API del Servicio Sismológico Nacional de Chile
url = "https://api.red.ssn.cl/fdsnws/event/1/query"

# Parámetros de la consulta
params = {
    "format": "geojson",  # Formato de respuesta en GeoJSON
    "starttime": "2008-06-28T00:00:00",  # Fecha de inicio (15 años atrás)
    "endtime": "2023-06-28T23:59:59",  # Fecha de fin (hasta la fecha actual)
    "minlatitude": "-56",  # Límite mínimo de latitud (Chile continental y marítimo)
    "maxlatitude": "-17",  # Límite máximo de latitud (Chile continental y marítimo)
    "minlongitude": "-76",  # Límite mínimo de longitud (Chile continental y marítimo)
    "maxlongitude": "-66",  # Límite máximo de longitud (Chile continental y marítimo)
}

# Realizar la solicitud GET a la API
response = requests.get(url, params=params)

# Verificar si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    # Obtener los datos de sismos en formato JSON
    data = response.json()
    # Aquí puedes procesar los datos como desees
    # Por ejemplo, imprimir la cantidad de sismos encontrados
    print("Cantidad de sismos encontrados:", len(data["features"]))
else:
    print("Error al obtener los datos de la API")