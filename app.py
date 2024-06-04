from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

# loads the "darkly" template and sets it as the default
load_figure_template("darkly")

import pandas as pd
from ingest import ingest
from plots import agsf_dollar_hist, dollar_per_acre_hist

url='https://gist.githubusercontent.com/rselover/a82f17ec1a97538080940248880597fe/raw/69c797301be90b135eccc00d2015a28edc630b95/weston.json'

df=ingest(url)
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = dbc.Container([
    html.Div(className='row', children=[
        html.H1(children='Weston Real Estate', style={'textAlign':'center'}),

        html.Div(className='parent', children=[
            dcc.Graph(id='$/AGSF', className='plot'),
            html.Div(className='spacer'),
            dcc.Graph(id='plot 2', className='plot')
        ]),

        dcc.Dropdown(df.Address.unique(), '144 SUDBURY RD', id='dropdown-selection', className='dash-bootstrap'),
    ])
])

@callback(
    Output('$/AGSF', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_plot_1(value):
    dff = df[df.Address==value]

    p1 = agsf_dollar_hist(df)
    # This Plot is NOT filtered
    return p1

@callback(
    Output('plot 2', 'figure'),
    Input('dropdown-selection', 'value')
)

def update_plot_2(value):
    dff = df[df.Address==value]

    p2 = dollar_per_acre_hist(df)
    # This Plot is NOT filtered
    return p2

if __name__ == '__main__':
    app.run(debug=True)
