import csv
import datetime
import time
import requests
from bs4 import BeautifulSoup

csv_file = open("sismos.csv", "w", newline="")
csv_writer = csv.writer(csv_file, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)

BASE_URL = 'https://www.sismologia.cl/sismicidad/sismos-por-dia.html'

date_ini = datetime.date(2008, 1, 1)  # fecha inicio del registro
date_end = datetime.date(2023, 6, 27)  # fecha final del registro
days = (date_end - date_ini).days  # días de datos a recopilar

for i in range(days):  # comienza la recopilacion de datos
    BASE_DIR = f"/{date_ini.year}/{date_ini.strftime('%m')}/{date_ini.strftime('%Y%m')}"

    try:
        response = requests.get(BASE_URL + BASE_DIR + date_ini.strftime("%d") + '.html')
        response.raise_for_status()
        page = BeautifulSoup(response.content, 'html.parser')
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(2)
    else:
        rows = page.select('tbody tr')
        for row in rows[1:-1]:
            csv_writer.writerow([cell.get_text().replace(',', '') for cell in row.select('td')])

        date_ini += datetime.timedelta(days=1)  # avanza 1 día

        time.sleep(1)  # espera 1 segundo para no saturar el servidor

csv_file.close()