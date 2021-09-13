# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from logging import error
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
# from app import app, server
import traceback
from apps import home, eda, model, errorPage, errorLogger

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

server = app.server

app.layout = dbc.Container(
    [
        dcc.Store('uploaded_data'),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Tabs(
                            [
                                dcc.Tab(
                                    id = 'home_tab',
                                    label='Home',
                                    value='home',
                                    className="custom-tab",
                                    selected_className="custom-tab--selected",
                                ),
                                dcc.Tab(
                                    id = 'eda_tab',
                                    label='Exploratory Analysis',
                                    value='eda',
                                    className="custom-tab",
                                    selected_className="custom-tab--selected",
                                ),
                                dcc.Tab(
                                    id = 'model_tab',
                                    label='Building Models',
                                    value='model',
                                    className="custom-tab",
                                    selected_className="custom-tab--selected",
                                )
                            ],
                            id = 'tabs',
                            value = 'home',
                            className='custom-tabs'
                        ),
                        html.Div(id = 'content')
                    ],
                )
            ]
        )
    ],
    fluid=True
)

####################################################################################
## Switiching between tabs
####################################################################################

@app.callback(
    Output('content', 'children'),
    Input('tabs', 'value')
)
def switch_tab(at):
    try:
        if at == 'home':
            return home.home_body
        elif at == 'eda':
            return eda.eda_body
        elif at=='model':
            return model.model_body
        else:
            return errorPage.error_page_body
    except Exception as e:
        errorLogger.insert_error('app', 'switch_tab', str(e), traceback.format_exc())


if __name__ == '__main__':
    app.run_server(debug=True)