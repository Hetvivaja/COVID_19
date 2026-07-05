from pathlib import Path

from flask import Flask, abort, render_template, request
import pandas as pd
import plotly.io as pio
from graph.totalCase import create_total
from graph.day_wise import create_day
from graph.country_de_re_ac import create_country
from graph.pie_chart import create_data

app = Flask(__name__)
DATA_DIR = Path(__file__).resolve().parent / "data"


def chart_html(fig):
    return pio.to_html(fig, full_html=False, config={"responsive": True})

@app.route('/')
def home():
    df = pd.read_csv(DATA_DIR / "country.csv", usecols=['Country/Region', 'Deaths', 'Recovered', 'Active'])
    totals = {
        "countries": df["Country/Region"].nunique(),
        "deaths": f"{int(df['Deaths'].sum()):,}",
        "recovered": f"{int(df['Recovered'].sum()):,}",
        "active": f"{int(df['Active'].sum()):,}",
    }
    return render_template('home.html', totals=totals)

@app.route('/totalcase')
def total_case():
    fig = create_total()
    plot_html = chart_html(fig)
    return render_template('total_case.html', plot=plot_html)

@app.route('/daywise')
def day_wise():
    fig = create_day()
    plot_html = chart_html(fig)
    return render_template('day_wise.html', plot=plot_html)

@app.route('/countrywise')
def country_wise():
    fig = create_country()
    plot_html = chart_html(fig)
    return render_template('country_wise.html', plot=plot_html)

@app.route('/piechart')
def pie_chart():
    df = pd.read_csv(DATA_DIR / "country.csv", usecols=['Country/Region', 'Deaths', 'Recovered', 'Active'])
    countries = sorted(df["Country/Region"].unique())

    top_country = (
        df.groupby('Country/Region')[['Deaths', 'Recovered', 'Active']]
        .sum()
        .reset_index()
        .sort_values(by='Deaths', ascending=False)
        .head(12)
    )
    return render_template("pie_chart.html", countries=countries, boxes=top_country.to_dict(orient='records'))


@app.route('/countrypie', methods=['POST'])
def country_pie():
    selected_country = request.form['country']
    try:
        pie_fig, bar_fig = create_data(selected_country)
    except ValueError:
        abort(404)
    pie_html = chart_html(pie_fig)
    bar_html = chart_html(bar_fig)
    return render_template('country_pie.html', pie_plot=pie_html, bar_plot=bar_html, country=selected_country)

if __name__ == '__main__':
    app.run(debug=False, port=8001)
