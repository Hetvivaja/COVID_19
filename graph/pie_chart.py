import pandas as pd
import plotly.graph_objects as go

def create_data(country):
    df=pd.read_csv('D:/My_first/data/country.csv', usecols=['Country/Region', 'Deaths', 'Recovered', 'Active'])

    countrydata=df[df['Country/Region']==country]

    summ=countrydata.groupby('Country/Region')[['Deaths','Recovered','Active']].sum()

    #piechart
    pie_label = ['Deaths', 'Recovered', 'Active']
    pie_value = summ.values[0]
    pie_chart = go.Figure(data=[go.Pie(labels=pie_label, values=pie_value, hole=0.3)])
    pie_chart.update_layout(title_text=f"Case Distribution - {country}")

    #Barchart
    bar_chart = go.Figure(data=[
        go.Bar(x=['Deaths'], y=[summ['Deaths'].values[0]], name='Deaths', marker_color='black',width=0.88),
        go.Bar(x=['Recovered'], y=[summ['Recovered'].values[0]], name='Recovered', marker_color='orange'),
        go.Bar(x=['Active'], y=[summ['Active'].values[0]], name='Active', marker_color='blue'),
    ])
    bar_chart.update_layout(    
        title=f"Case Breakdown - {country}",
        xaxis_title="Case Type",
        yaxis_title="Total Count",
        barmode='group'
    )
    return pie_chart,bar_chart
                            