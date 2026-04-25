import requests

# -----------------------------
# 1. LOAD MEMORY (previous + max)
# -----------------------------
file = open("memory.txt", "r")
content = file.read()
file.close()

previous_temp, max_temp = content.split(",")
previous_temp = float(previous_temp)
max_temp = float(max_temp)

# -----------------------------
# 2. GET CURRENT TEMPERATURE (OBSERVE)
# -----------------------------
url = "https://api.open-meteo.com/v1/forecast?latitude=32.98&longitude=-96.73&current_weather=true"

response = requests.get(url)
data = response.json()

current_temp = data["current_weather"]["temperature"]

# -----------------------------
# 3. DECISION: MAX CHECK
# -----------------------------
if current_temp > max_temp:
    print("🚨 New maximum temperature recorded!")
    max_temp = current_temp

# -----------------------------
# 4. DECISION: COMPARE WITH PREVIOUS
# -----------------------------
if current_temp > previous_temp:
    print("📈 Temperature increased since last check")
else:
    print("📉 Temperature did not increase")

# -----------------------------
# 5. UPDATE MEMORY
# -----------------------------
file = open("memory.txt", "w")
file.write(f"{current_temp},{max_temp}")
file.close()

# -----------------------------
# 6. DEBUG OUTPUT (optional but useful)
# -----------------------------
print("Current:", current_temp)
print("Previous:", previous_temp)
print("Max:", max_temp)
