import pandas as pd
import plotly.graph_objs as go

def create_day():
 
    df = pd.read_csv('D:/My_first/data/day.csv',usecols=['Date','Deaths','Recovered'])

    grouped = df.groupby('Date')[['Deaths', 'Recovered']].sum().reset_index()

# Create scatter plots
    fig = go.Figure()

# Deaths
    fig.add_trace(go.Scatter(
    x=grouped['Date'],
    y=grouped['Deaths'],
    mode='markers',
    marker=dict(color='red', symbol='x', size=10),
    name='Deaths',
    hovertemplate='Date: %{x}<br>Deaths: %{y}<extra></extra>'
    ))

# Recovered
    fig.add_trace(go.Scatter(
    x=grouped['Date'],
    y=grouped['Recovered'],
    mode='markers',
    marker=dict(color='blue', symbol='star', size=10),
    name='Recovered',
    hovertemplate='Date: %{x}<br>Recovered: %{y}<extra></extra>'
    ))

# Layout
    fig.update_layout(
    title='Date-wise Deaths and Recovered',
    xaxis_title='Date',
    yaxis_title='Number of Cases',
    xaxis_tickangle=-45,
    legend_title='Case Type',
    template='plotly_white'
    )
    return fig



# fig.show()
