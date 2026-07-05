import plotly.graph_objs as go

from graph.common import CASE_COLORS, chart_layout, read_data


def create_total():
    df = read_data("worldometer.csv", usecols=['Country/Region', 'TotalCases'])

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
    marker_color=CASE_COLORS['TotalCases'],
    name='Total Cases',
    hovertemplate='Country: %{y}<br>Total Cases: %{x:,}<extra></extra>'
    ))

    fig.update_layout(**chart_layout(
    title='Top 25 Countries by Total Cases',
    xaxis_title='Total Cases',
    yaxis_title='Country',
    height=720,
    margin=dict(l=120, r=30, t=70, b=60)
    ))
    return fig
