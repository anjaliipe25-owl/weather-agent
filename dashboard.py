import streamlit as st
import plotly.graph_objects as go
import json
import pandas as pd

with open("agent_state.json", "r") as f:
    history = json.load(f)

df = pd.DataFrame(history)
print(df)

df["time"] = pd.to_datetime(df["time"], utc=True)
print(df.dtypes)
df["time"] = df["time"].dt.tz_convert("America/Chicago")
