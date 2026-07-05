from pathlib import Path

import pandas as pd
import plotly.graph_objs as go

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def create_total():
    df = pd.read_csv(DATA_DIR / "worldometer.csv", usecols=['Country/Region', 'TotalCases'])

    avg_case = (
        df.groupby('Country/Region')['TotalCases']
        .mean()
        .sort_values(ascending=False)
        .head(25)
        .sort_values()
    )

    fig = go.Figure()

    fig.add_trace(go.Bar(
    x=avg_case.values,
    y=avg_case.index,
    orientation='h',
    marker_color='#0f766e',
    name='Total Cases',
    hovertemplate='Country: %{y}<br>Total Cases: %{x:,}<extra></extra>'
    ))

    fig.update_layout(
    title='Top 25 Countries by Total Cases',
    xaxis_title='Total Cases',
    yaxis_title='Country',
    template='plotly_white',
    height=720,
    margin=dict(l=120, r=30, t=70, b=60)
    )
    return fig
