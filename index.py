from logging import error
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import app, server
import traceback
from apps import home, eda, model, errorPage, errorLogger

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Tabs(
                            [
                                dcc.Tab(
                                    label='Home',
                                    value='home',
                                ),
                                dcc.Tab(
                                    label='Exploratory Analysis',
                                    value='eda',
                                ),
                                dcc.Tab(
                                    label='Building Models',
                                    value='model',
                                )
                            ],
                            id = 'tabs',
                            value = 'home'
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
        errorLogger.insert_error('index', 'switch_tab', str(e), traceback.format_exc())


if __name__ == '__main__':
    app.run_server(debug=True)