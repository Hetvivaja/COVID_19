import pandas as pd
import plotly.graph_objs as go


def create_total():
    df = pd.read_csv('D:/My_first/data/worldometer.csv',usecols=['Country/Region','TotalCases'])

    avg_case = df.groupby('Country/Region')['TotalCases'].mean().sort_values(ascending=False)

# Create a Plotly chart
    fig = go.Figure()

    fig.add_trace(go.Scatter(
    x=avg_case.index,
    y=avg_case.values,
    mode='lines+markers',
    line=dict(color='purple'),
    name='Avg Total Cases',
    hovertemplate='Country: %{x}<br>Avg Cases: %{y}<extra></extra>'
    ))

# Update layout
    fig.update_layout(
    title='Average TotalCases by Country',
    xaxis_title='Country',
    yaxis_title='Average TotalCases',
    xaxis_tickangle=-45,
    template='plotly_white',
    height=600,
    width=1500
    )
    return fig

# fig.show()
