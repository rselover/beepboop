from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from ingest import ingest

url='https://gist.githubusercontent.com/rselover/a82f17ec1a97538080940248880597fe/raw/69c797301be90b135eccc00d2015a28edc630b95/weston.json'

df=ingest(url)
app = Dash()

app.layout = [
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.Address.unique(), '144 SUDBURY RD', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.Address==value]
    return px.line(dff, x='ELA', y='FY24 Total Val')

if __name__ == '__main__':
    app.run(debug=True)
