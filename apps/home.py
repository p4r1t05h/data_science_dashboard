import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash import dash_table
import pandas as pd
from app import app
import traceback
from dash.dependencies import Input, Output, State

from apps import generalFunctions, errorLogger

home_body = dbc.Container(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dcc.Upload(
                                    id='home_upload',
                                    children=html.Div([
                                        'Drag and Drop or ',
                                        html.A('Select Files')
                                    ]),
                                    className = 'upload_btn',
                                ),
                                html.Br(),
                                html.Div(id='uploaded_filename'),
                                html.Br(),
                                dcc.Dropdown(id='home_dropdown'),
                            ],
                            className = 'side_panel'
                        )
                    ],
                    width=2
                ),
                dbc.Col(
                    [
                        dash_table.DataTable(
                            id='home_table',
                        )
                    ]
                )
            ]
        )
    ]
)

####################################################################################
## uploading data
####################################################################################

@app.callback(
    Output('uploaded_data', 'data'),
    Input('home_upload', 'contents'),
    State('home_upload', 'filename')
)
def update_output(contents, filename):
    try:
        ctx = dash.callback_context
        change_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if 'home_upload' in change_id:
            df = generalFunctions.parse_contents(contents, filename)
            return df.to_dict('records')
        else:
            return dash.no_update
    except Exception as e:
        errorLogger.insert_error('generalFunctions', 'parse_contents', str(e), traceback.format_exc())

####################################################################################
## updating ui table
####################################################################################

@app.callback(
    Output('home_table', 'data'),
    Output('home_table', 'columns'),
    Output('uploaded_filename', 'children'),
    Input('uploaded_data', 'data'),
    Input('home_upload', 'filename')
)
def update_output(data):
    try:
        if data is not None:
            print('Hi')
            df = pd.DataFrame.from_dict(data)
            return df.to_dict('records'), [{"name": i, "id": i} for i in df.columns]
        else:
            return dash.no_update, dash.no_update
    except Exception as e:
        errorLogger.insert_error('generalFunctions', 'parse_contents', str(e), traceback.format_exc())
