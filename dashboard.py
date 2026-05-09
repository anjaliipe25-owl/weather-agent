import streamlit as st
import plotly.graph_objects as go
import json
import pandas as pd

with open("agent_state.json", "r") as f:
    history = json.load(f)

df = pd.DataFrame(history)
print(df)
