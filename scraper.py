import requests
from bs4 import BeautifulSoup
import json
import sys

try:
    url = 'https://www.ficohsa.hn/'
    res = requests.get(url, timeout=10)
    soup = BeautifulSoup(res.text, 'html.parser')
    span = soup.select_one('.gff-indicadores-divisas-v1__sale-value.value-one')

    if not span:
        raise Exception("No se encontró el selector. Puede haber cambiado la estructura de la página.")

    rate = span.text.replace('L', '').strip().replace(',', '.')
    data = {"exchangeRate": float(rate)}

    with open("cambio-ficohsa.json", "w") as f:
        json.dump(data, f)

    print("Cambio generado correctamente:", data)

except Exception as e:
    print("Error:", e)
    sys.exit(1)
