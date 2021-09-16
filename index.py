import dash
from logging import error
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import app, server

import traceback
from apps import home, eda, model

import warnings
warnings.filterwarnings("ignore")

##################################################################################
# desiging navigation bar
##################################################################################

navbar = html.Div(
    id="banner",
    className="banner",
    children=[
        html.Div(
            id="banner_text",
            children=[
                html.H5("Data Science Dashboard"),
            ],
        ),
        html.Div(
            id="banner_nav",
            children=[
                html.A(
                    html.Button(children="Home"),
                    href="/home",
                ),
                html.A(
                    html.Button(children="Exploratory Analysis"),
                    href="/eda",
                ),
                html.A(
                    html.Button(children="Model Building"),
                    href="/model",
                ),
                # html.Button(
                #     id="learn-more-button", children="LEARN MORE", n_clicks=0
                # ),
            ],
        ),
    ],
)

##################################################################################
# Overall app layout
##################################################################################

app.layout = dbc.Container(
    [
        dcc.Location(id = 'url', refresh = False),
        navbar,
        html.Div(id = 'page_content')
    ],
    fluid=True
)

##################################################################################
# Function to switch between pages
##################################################################################

@app.callback(
    Output('page_content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    try:
        if pathname == '/home':
            return home.home_body
        elif pathname == '/eda':
            return eda.eda_body
        elif pathname == '/model':
            return model.model_body
        else:
            return home.home_body
    except Exception as e:
        print(traceback.format_exc())

##################################################################################
# Calling app
##################################################################################

if __name__ == '__main__':
    app.run_server(debug=True)