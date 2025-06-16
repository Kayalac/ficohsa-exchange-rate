import requests
from bs4 import BeautifulSoup
import json
import sys

try:
    url = 'https://www.ficohsa.hn/'
    res = requests.get(url, timeout=10)

    if res.status_code != 200:
        raise Exception(f"No se pudo acceder a Ficohsa. Código de estado: {res.status_code}")

    soup = BeautifulSoup(res.text, 'html.parser')

    # Buscar el tipo de cambio
    span = soup.select_one('.gff-indicadores-divisas-v1__sale-value.value-one')
    if not span:
        raise Exception("No se encontró el selector CSS. La estructura de la página pudo haber cambiado.")

    # Procesar el valor
    rate = span.text.replace('L', '').strip().replace(',', '.')
    data = {
        "exchangeRate": float(rate)
    }

    # Guardar archivo
    with open("cambio-ficohsa.json", "w") as f:
        json.dump(data, f)

    print("✅ Tipo de cambio actualizado correctamente:", data)

except Exception as e:
    print("❌ Error:", e)
    sys.exit(1)
