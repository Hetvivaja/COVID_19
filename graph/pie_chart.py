from pathlib import Path

import pandas as pd
import plotly.graph_objects as go

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def create_data(country):
    df = pd.read_csv(DATA_DIR / "country.csv", usecols=['Country/Region', 'Deaths', 'Recovered', 'Active'])

    countrydata = df[df['Country/Region'] == country]

    summ = countrydata.groupby('Country/Region')[['Deaths', 'Recovered', 'Active']].sum()
    if summ.empty:
        raise ValueError(f"No data found for country: {country}")

    #piechart
    pie_label = ['Deaths', 'Recovered', 'Active']
    pie_value = summ.values[0]
    colors = ['#b42318', '#0f766e', '#2563eb']
    pie_chart = go.Figure(data=[go.Pie(labels=pie_label, values=pie_value, hole=0.42, marker=dict(colors=colors))])
    pie_chart.update_layout(
        title_text=f"Case Distribution - {country}",
        template='plotly_white',
        height=460,
        margin=dict(l=20, r=20, t=70, b=40)
    )

    #Barchart
    bar_chart = go.Figure(data=[
        go.Bar(x=['Deaths'], y=[summ['Deaths'].values[0]], name='Deaths', marker_color='#b42318', width=0.7),
        go.Bar(x=['Recovered'], y=[summ['Recovered'].values[0]], name='Recovered', marker_color='#0f766e'),
        go.Bar(x=['Active'], y=[summ['Active'].values[0]], name='Active', marker_color='#2563eb'),
    ])
    bar_chart.update_layout(    
        title=f"Case Breakdown - {country}",
        xaxis_title="Case Type",
        yaxis_title="Total Count",
        barmode='group',
        template='plotly_white',
        height=460,
        margin=dict(l=70, r=20, t=70, b=70)
    )
    return pie_chart,bar_chart
                            
