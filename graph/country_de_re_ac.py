import plotly.graph_objects as go

from graph.common import CASE_COLORS, CASE_COLUMNS, chart_layout, read_data

def create_country():

    df = read_data("country.csv", usecols=CASE_COLUMNS)

    grouped = df.groupby('Country/Region')[['Deaths', 'Recovered', 'Active']].sum()
    grouped = grouped.sort_values(by='Deaths', ascending=False).head(20)

    countries = grouped.index.tolist()
    deaths = grouped['Deaths'].tolist()
    recovered = grouped['Recovered'].tolist()
    active = grouped['Active'].tolist()

    fig = go.Figure(data=[
    go.Bar(name='Deaths', x=countries, y=deaths, marker_color=CASE_COLORS['Deaths']),
    go.Bar(name='Recovered', x=countries, y=recovered, marker_color=CASE_COLORS['Recovered']),
    go.Bar(name='Active', x=countries, y=active, marker_color=CASE_COLORS['Active'])
    ])

    fig.update_layout(**chart_layout(
    barmode='group',
    title='Top 20 Countries by Deaths',
    xaxis_title='Country',
    yaxis_title='Total Cases',
    xaxis_tickangle=-45,
    height=680,
    margin=dict(l=70, r=30, t=70, b=150)
    ))
    return fig
