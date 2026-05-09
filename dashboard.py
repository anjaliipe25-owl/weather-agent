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
st.title("🏕️ Camping Temperature Dashboard")
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["time"], y=df["temp_f"], mode="lines+markers", name="Temperature (°F)"))
st.plotly_chart(fig)

