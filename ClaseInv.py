# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 19:08:59 2020

@author: Lucas E. La Pietra
"""

import pandas as pd
import plotly.express as px
import dash
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

df = pd.read_csv(
    'https://raw.githubusercontent.com/cienciadedatos/datos-de-miercoles/master/datos/2019/2019-07-10/pokemon.csv')

app.layout = html.Div([
    dbc.Row(
        [
            dbc.Col(html.H1("Graficos Dash Pokemon"))
        ]
    ),
    dbc.Row(
        [
            dbc.Col(dcc.Graph(id='bar1'), md=5),
            dbc.Col(dcc.Graph(id='scatter1'), md=7)
        ]
    ),
    dbc.Row(
        [
            dbc.Col([
                html.Label('Cantidad de Pokemon a mostrar:'),
                dcc.Slider(
                    id='slider',
                    min=10,
                    max=50,
                    value=25)]),
        ]),
    dbc.Row(
        [
            dcc.RadioItems(
                id='radio',
                options=[
                    {'label': 'Ataque', 'value': 'ataque'},
                    {'label': 'Defensa', 'value': 'defensa'},
                    {'label': 'Velocidad', 'value': 'velocidad'}
                ],
                value='ataque'
            )
        ]
    )
])


@app.callback(Output('bar1', 'figure'),
              [Input('slider', 'value'), Input('radio','value')]
              )
def update_figure(cantidad, estadistica):
    fig = px.bar(df.nlargest(cantidad, columns=estadistica), x='nombre_traducido', y=estadistica, color='tipo_1')
    return fig


@app.callback(Output('scatter1', 'figure'),
              [Input('slider', 'value')]
              )
def update_figure(cantidad):
    fig = px.scatter(df.nlargest(cantidad, columns='ataque'), x='defensa', y='ataque', hover_data=['nombre_traducido'],
                     color='tipo_1')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
