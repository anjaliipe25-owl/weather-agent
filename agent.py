import requests
import json
import datetime

# -----------------------------
# 1. LOAD MEMORY (previous + max)
# -----------------------------
try:
    file = open("agent_state.json", "r")
    history = json.load(file)
    file.close()
except FileNotFoundError:
    history = []

if history:
    previous_temp = history[-1]["temp"]
    max_temp = max(entry["temp"] for entry in history)
else:
    previous_temp = 0
    max_temp = 0
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
history.append({"temp": current_temp, "time": datetime.datetime.now(datetime.timezone.utc).isoformat()})
file = open("agent_state.json", "w")
json.dump(history, file)
file.close()

# -----------------------------
# 6. DEBUG OUTPUT (optional but useful)
# -----------------------------
print("Current:", current_temp)
print("Previous:", previous_temp)
print("Max:", max_temp)
