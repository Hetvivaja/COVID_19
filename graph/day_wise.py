from pathlib import Path

import pandas as pd
import plotly.graph_objs as go

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def create_day():
 
    df = pd.read_csv(DATA_DIR / "day.csv", usecols=['Date', 'Deaths', 'Recovered'])

    grouped = df.groupby('Date')[['Deaths', 'Recovered']].sum().reset_index()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
    x=grouped['Date'],
    y=grouped['Deaths'],
    mode='lines+markers',
    line=dict(color='#b42318', width=2),
    marker=dict(color='#b42318', size=6),
    name='Deaths',
    hovertemplate='Date: %{x}<br>Deaths: %{y:,}<extra></extra>'
    ))

    fig.add_trace(go.Scatter(
    x=grouped['Date'],
    y=grouped['Recovered'],
    mode='lines+markers',
    line=dict(color='#0f766e', width=2),
    marker=dict(color='#0f766e', size=6),
    name='Recovered',
    hovertemplate='Date: %{x}<br>Recovered: %{y:,}<extra></extra>'
    ))

    fig.update_layout(
    title='Date-wise Deaths and Recovered',
    xaxis_title='Date',
    yaxis_title='Number of Cases',
    xaxis_tickangle=-45,
    legend_title='Case Type',
    template='plotly_white',
    height=620,
    hovermode='x unified',
    margin=dict(l=70, r=30, t=70, b=100)
    )
    return fig
