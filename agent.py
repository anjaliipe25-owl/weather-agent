import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=32.98&longitude=-96.73&current_weather=true"

response = requests.get(url)
data = response.json()

current_temp = data["current_weather"]["temperature"]

file = open("memory.txt", "r")
previous_temp = float(file.read())
file.close()

if current_temp > previous_temp:
    print("Temperature increased")
elif current_temp < previous_temp:
    print("Temperature decreased")
else:
    print("No change")

file = open("memory.txt", "w")
file.write(str(current_temp))
file.close()
