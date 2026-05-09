import streamlit as st
import plotly.graph_objects as go
import json
import pandas as pd

with open("agent_state.json", "r") as f:
    history = json.load(f)

df = pd.DataFrame(history)
df["time"] = pd.to_datetime(df["time"], utc=True)
df["time"] = df["time"].dt.tz_convert("America/Chicago")
df["temp_f"] = df["temp"] * 9/5 + 32
def packing_advice(temp_f):
    if temp_f < 40:
        return "🥶 Very cold night ahead — bring a heavy sleeping bag and layers."
    elif temp_f < 55:
        return "🧥 Cool night — a warm jacket and sleeping bag recommended."
    elif temp_f < 70:
        return "😊 Mild night — light jacket should be fine."
    else:
        return "☀️ Warm night — light clothes, stay hydrated."
st.title("🏕️ Camping Temperature Dashboard")
st.metric(label="Current Temperature", value=f"{df['temp_f'].iloc[-1]:.1f}°F")
st.info(packing_advice(df['temp_f'].iloc[-1]))
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["time"], y=df["temp_f"], mode="lines+markers", name="Temperature (°F)"))
st.plotly_chart(fig)

