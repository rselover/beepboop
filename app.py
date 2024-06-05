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

agsf=agsf_dollar_hist(df)
dollar_per_acre=dollar_per_acre_hist(df)

app.layout = dbc.Container([
    html.Div(className='row', children=[
        html.H1(children='Weston Real Estate', style={'textAlign':'center'}),

        html.Div(className='parent', children=[
            dcc.Graph(id='$/AGSF', className='plot', figure=agsf),
            html.Div(className='spacer'),
            dcc.Graph(id='plot 2', className='plot', figure=dollar_per_acre)
        ]),
    ]),
    dcc.Dropdown(df.Address.unique(), '144 SUDBURY RD', id='dropdown-selection', className='dash-bootstrap'),

    html.Div(className='parent', children=[
        html.Div([
            html.Label('Acres: ', className='textTileLabel'),
            html.Br(),
            html.P(className='textTile', id='textTile1'),
        ]),
        html.Div(className='spacer'),
        html.Div([
            html.Label('Above Ground Square Footage (AGSF): ', className='textTileLabel'),
            html.Br(),
            html.P(className='textTile', id='textTile2'),
        ]),
        html.Div(className='spacer'),
        html.Div([
            html.Label('Total Square Footage (ELA): ', className='textTileLabel'),
            html.Br(),
            html.P(className='textTile', id='textTile3'),
        ]),
        html.Div(className='spacer'),
        html.Div([
            html.Label('Below Ground Square Footage (BGSF): ', className='textTileLabel'),
            html.Br(),
            html.P(className='textTile', id='textTile4'),
        ])
    ]),

    
    html.Hr(),

    html.Div(className='row', children=[
        #html.Div(className='slider', children=
                #  [
            dcc.Slider(800000.00, 1500000.00, step=1,
                           marks={
                                800000: '$800K',
                                1000000: '$1M',
                                1250000: '$1.25M',
                                1500000: '$1.5M'
                            },
                            tooltip={"placement": "bottom", "always_visible": True,  "transform": "formatCurrency"},
                        value=800000.00, id='offer-slider', className='slider'),
            #html.Div(className='spacer'),
            dcc.Slider(0.6, 1, 0.05, value=0.8, id='basement-slider', className='slider',
                       tooltip={"placement": "bottom", "always_visible": True}),
        #
        # ],
            #style={
        #'display': 'flex',
        #'width': '50%',
        #'justify-content': 'center',
    #}
        #)
    ])
])

@callback(
    Output('textTile1', 'children'),
    Input('dropdown-selection', 'value')
)

def update_text1(value):
    dff = df[df.Address==value]
    return f"{dff['Acres'].values[0]}"

@callback(
    Output('textTile2', 'children'),
    Input('dropdown-selection', 'value')
)

def update_text2(value):
    dff = df[df.Address==value]
    return f"{dff['GLA (Above Grade)'].values[0]}"

@callback(
    Output('textTile3', 'children'),
    Input('dropdown-selection', 'value')
)

def update_text3(value):
    dff = df[df.Address==value]
    return f"{dff['ELA'].values[0]}"

@callback(
    Output('textTile4', 'children'),
    Input('dropdown-selection', 'value')
)

def update_text4(value):
    dff = df[df.Address==value]
    return f"{dff['BGSF'].values[0]}"

if __name__ == '__main__':
    app.run(debug=True)
