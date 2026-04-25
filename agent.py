import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=32.98&longitude=-96.73&current_weather=true"
response = requests.get(url)
data = response.json()
print(data)
