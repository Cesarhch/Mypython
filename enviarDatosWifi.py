import requests

url = "http://192.168.4.1"  # Dirección IP por defecto del ESP32 en modo AP
data = {"dato1": "valor1", "dato2": "valor2"}

response = requests.post(url, json=data)

print(response.status_code)
print(response.text)
