import plotly.graph_objs as go

from graph.common import CASE_COLORS, chart_layout, read_data

def create_day():
 
    df = read_data("day.csv", usecols=['Date', 'Deaths', 'Recovered'])

    grouped = df.groupby('Date')[['Deaths', 'Recovered']].sum().reset_index()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
    x=grouped['Date'],
    y=grouped['Deaths'],
    mode='lines+markers',
    line=dict(color=CASE_COLORS['Deaths'], width=2),
    marker=dict(color=CASE_COLORS['Deaths'], size=6),
    name='Deaths',
    hovertemplate='Date: %{x}<br>Deaths: %{y:,}<extra></extra>'
    ))

    fig.add_trace(go.Scatter(
    x=grouped['Date'],
    y=grouped['Recovered'],
    mode='lines+markers',
    line=dict(color=CASE_COLORS['Recovered'], width=2),
    marker=dict(color=CASE_COLORS['Recovered'], size=6),
    name='Recovered',
    hovertemplate='Date: %{x}<br>Recovered: %{y:,}<extra></extra>'
    ))

    fig.update_layout(**chart_layout(
    title='Date-wise Deaths and Recovered',
    xaxis_title='Date',
    yaxis_title='Number of Cases',
    xaxis_tickangle=-45,
    legend_title='Case Type',
    height=620,
    hovermode='x unified',
    margin=dict(l=70, r=30, t=70, b=100)
    ))
    return fig
