import plotly.graph_objects as go

from graph.common import CASE_COLORS, CASE_COLUMNS, chart_layout, read_data

def create_data(country):
    df = read_data("country.csv", usecols=CASE_COLUMNS)

    countrydata = df[df['Country/Region'] == country]

    summ = countrydata.groupby('Country/Region')[['Deaths', 'Recovered', 'Active']].sum()
    if summ.empty:
        raise ValueError(f"No data found for country: {country}")

    pie_label = ['Deaths', 'Recovered', 'Active']
    pie_value = summ.values[0]
    colors = [CASE_COLORS[label] for label in pie_label]
    pie_chart = go.Figure(data=[go.Pie(labels=pie_label, values=pie_value, hole=0.42, marker=dict(colors=colors))])
    pie_chart.update_layout(**chart_layout(
        title_text=f"Case Distribution - {country}",
        height=460,
        margin=dict(l=20, r=20, t=70, b=40)
    ))

    bar_chart = go.Figure(data=[
        go.Bar(x=['Deaths'], y=[summ['Deaths'].values[0]], name='Deaths', marker_color=CASE_COLORS['Deaths'], width=0.7),
        go.Bar(x=['Recovered'], y=[summ['Recovered'].values[0]], name='Recovered', marker_color=CASE_COLORS['Recovered']),
        go.Bar(x=['Active'], y=[summ['Active'].values[0]], name='Active', marker_color=CASE_COLORS['Active']),
    ])
    bar_chart.update_layout(**chart_layout(    
        title=f"Case Breakdown - {country}",
        xaxis_title="Case Type",
        yaxis_title="Total Count",
        barmode='group',
        height=460,
        margin=dict(l=70, r=20, t=70, b=70)
    ))
    return pie_chart,bar_chart
                            
