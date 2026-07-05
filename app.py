from flask import Flask,render_template,request
import pandas as pd
import matplotlib.pyplot as plt
import plotly.io as pio
import os
from graph.totalCase import create_total
from graph.day_wise import create_day
from graph.country_de_re_ac import create_country
from graph.pie_chart import create_data

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/totalcase')
def total_case():
    fig = create_total()
    plot_html = pio.to_html(fig, full_html=False)
    return render_template('total_case.html', plot=plot_html)

@app.route('/daywise')
def day_wise():
    fig = create_day()
    plot_html = pio.to_html(fig, full_html=False)
    return render_template('day_wise.html', plot=plot_html)

@app.route('/countrywise')
def country_wise():
    fig = create_country()
    plot_html = pio.to_html(fig, full_html=False)
    return render_template('country_wise.html', plot=plot_html)

@app.route('/piechart')
def pie_chart():
    df = pd.read_csv('D:/My_first/data/country.csv', usecols=['Country/Region', 'Deaths', 'Recovered', 'Active'])
    countries = sorted(df["Country/Region"].unique())

    top_country=df.groupby('Country/Region')[['Deaths', 'Recovered', 'Active']].sum().reset_index().head(12)
    return render_template("pie_chart.html", countries=countries,boxes=top_country.to_dict(orient='records'))


@app.route('/countrypie', methods=['POST'])
def country_pie():
    selected_country = request.form['country']
    pie_fig, bar_fig = create_data(selected_country)
    pie_html = pio.to_html(pie_fig, full_html=False)
    bar_html = pio.to_html(bar_fig, full_html=False)
    return render_template('country_pie.html', pie_plot=pie_html, bar_plot=bar_html, country=selected_country)

if __name__ == '__main__': 
    app.run(debug = True,port=8001)
