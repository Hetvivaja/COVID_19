import pandas as pd
import plotly.graph_objects as go

def create_country():

    df = pd.read_csv('D:/My_first/data/country.csv', usecols=['Country/Region', 'Deaths', 'Recovered', 'Active'])

    grouped = df.groupby('Country/Region')[['Deaths', 'Recovered', 'Active']].sum()
    grouped = grouped.sort_values(by='Deaths', ascending=False)  # Top 10 countries

# Extract data
    countries = grouped.index.tolist()
    deaths = grouped['Deaths'].tolist()
    recovered = grouped['Recovered'].tolist()
    active = grouped['Active'].tolist()

#  chart using Plotly
    fig = go.Figure(data=[
    go.Bar(name='Deaths', x=countries, y=deaths, marker_color='black'),
    go.Bar(name='Recovered', x=countries, y=recovered, marker_color='orange'),
    go.Bar(name='Active', x=countries, y=active, marker_color='blue')
    ])

    fig.update_layout(
    barmode='group',
    title='Country-wise Deaths, Recovered, and Active Cases',
    xaxis_title='Country',
    yaxis_title='Total Cases',
    xaxis_tickangle=-45
    )
    return fig
# fig.show()
