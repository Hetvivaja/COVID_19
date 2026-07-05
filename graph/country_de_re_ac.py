from pathlib import Path

import pandas as pd
import plotly.graph_objects as go

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def create_country():

    df = pd.read_csv(DATA_DIR / "country.csv", usecols=['Country/Region', 'Deaths', 'Recovered', 'Active'])

    grouped = df.groupby('Country/Region')[['Deaths', 'Recovered', 'Active']].sum()
    grouped = grouped.sort_values(by='Deaths', ascending=False).head(20)

# Extract data
    countries = grouped.index.tolist()
    deaths = grouped['Deaths'].tolist()
    recovered = grouped['Recovered'].tolist()
    active = grouped['Active'].tolist()

    fig = go.Figure(data=[
    go.Bar(name='Deaths', x=countries, y=deaths, marker_color='#b42318'),
    go.Bar(name='Recovered', x=countries, y=recovered, marker_color='#0f766e'),
    go.Bar(name='Active', x=countries, y=active, marker_color='#2563eb')
    ])

    fig.update_layout(
    barmode='group',
    title='Top 20 Countries by Deaths',
    xaxis_title='Country',
    yaxis_title='Total Cases',
    xaxis_tickangle=-45,
    template='plotly_white',
    height=680,
    margin=dict(l=70, r=30, t=70, b=150)
    )
    return fig
