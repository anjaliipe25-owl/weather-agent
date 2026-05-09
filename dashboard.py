import streamlit as st
import plotly.graph_objects as go
import json
import pandas as pd

with open("agent_state.json", "r") as f:
    history = json.load(f)

df = pd.DataFrame(history)
df["time"] = pd.to_datetime(df["time"], utc=True)
df["time"] = df["time"].dt.tz_convert("America/Chicago")
st.title("🏕️ Camping Temperature Dashboard")
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["time"], y=df["temp"], mode="lines+markers", name="Temperature (°C)"))
st.plotly_chart(fig)
