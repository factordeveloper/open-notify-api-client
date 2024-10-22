import urllib.request
import json

# Hacer la solicitud a la API
req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
with urllib.request.urlopen(req) as response:
    data = response.read()

# Convertir la respuesta en JSON
obj = json.loads(data)

# Imprimir el timestamp y la posición de la ISS
print(obj['timestamp'])
print(obj['iss_position']['latitude'], obj['iss_position']['longitude'])
