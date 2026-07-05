from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

CASE_COLUMNS = ['Country/Region', 'Deaths', 'Recovered', 'Active']
CASE_COLORS = {
    'Deaths': '#b42318',
    'Recovered': '#0f766e',
    'Active': '#2563eb',
    'TotalCases': '#0f766e',
}
PLOT_TEMPLATE = 'plotly_white'


def read_data(filename, usecols=None):
    return pd.read_csv(DATA_DIR / filename, usecols=usecols)


def chart_layout(**kwargs):
    layout = {
        'template': PLOT_TEMPLATE,
        'margin': dict(l=70, r=30, t=70, b=70),
    }
    layout.update(kwargs)
    return layout
