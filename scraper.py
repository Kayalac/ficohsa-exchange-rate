import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.ficohsa.hn/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# Encuentra el span con el tipo de cambio correcto
span = soup.select_one('.gff-indicadores-divisas-v1__sale-value.value-one')

if not span:
    raise Exception("No se pudo encontrar el tipo de cambio. El selector puede haber cambiado.")

rate = span.text.replace('L', '').strip().replace(',', '.')

data = {
    "exchangeRate": float(rate)
}

with open("cambio-ficohsa.json", "w") as f:
    json.dump(data, f)
