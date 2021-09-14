import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash import dash_table
from dash_bootstrap_components._components.Col import Col
import pandas as pd
from app import app
import traceback
from dash.dependencies import Input, Output, State

from apps import generalFunctions, errorLogger

####################################################################################
## Reading Data data
####################################################################################

df = pd.read_csv('./data/Life Expectancy Data.csv')

####################################################################################
## Home Layout
####################################################################################


home_body = dbc.Container(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                # dcc.Upload(
                                #     id='home_upload',
                                #     children=html.Div([
                                #         'Drag and Drop or ',
                                #         html.A('Select Files')
                                #     ]),
                                #     className = 'upload_btn',
                                # ),
                                # html.Br(),
                                # html.Div(id='uploaded_filename'),
                                html.Br(),
                                dcc.Dropdown(id='home_dropdown'),
                            ],
                            className = 'side_panel'
                        )
                    ],
                    # width = {"size": 3, "order": 1}
                    width=2
                ),
                html.Br(),
                # dbc.Col(width = 1),
                dbc.Col(
                    [
                        dash_table.DataTable(
                            id='home_table',
                            data = df.to_dict('records'),
                            columns = [{"name": i, "id": i} for i in df.columns],
                            style_data = {
                                'whiteSpace': 'normal',
                                'height': 'auto',
                                'minWidth': '190px',
                                'width': '190px',
                                'maxWidth': '190px'
                            },
                            fixed_rows={
                                'headers': True
                            },
                            style_table={
                                'height': '400px',
                                'overflowY':'auto',
                                'overflowX': 'auto'
                            },
                            style_header={
                                'fontWeight': 'bold',
                                'textAlign':'center',
                                'border': '1px solid black',
                                'backgroundColor': 'rgb(239, 239, 239)',
                                'color': 'black',
                                'font-size': '16px'
                            },
                            style_cell={
                                'border': '1px solid grey',
                                'textAlign': 'center',
                            }
                        )
                    ],
                    # width = {"size": 5, "order": 2}
                    width= 5
                )
            ]
        )
    ],
    fluid= True,
    
)

# ####################################################################################
# ## uploading data
# ####################################################################################

# @app.callback(
#     Output('uploaded_data', 'data'),
#     Input('home_upload', 'contents'),
#     State('home_upload', 'filename')
# )
# def update_output(contents, filename):
#     try:
#         if contents is not None:
#             df = generalFunctions.parse_contents(contents, filename)
#             return df.to_dict('records')
#         else:
#             return dash.no_update
#     except Exception as e:
#         print(e)

# ####################################################################################
# ## updating ui table
# ####################################################################################

# @app.callback(
#     Output('home_table', 'data'),
#     Output('home_table', 'columns'),
#     Output('uploaded_filename', 'children'),
#     Input('uploaded_data', 'data'),
#     Input('home_upload', 'filename')
# )
# def update_output(data):
#     try:
#         if data is not None:
#             print('Hi')
#             df = pd.DataFrame.from_dict(data)
#             return df.to_dict('records'), [{"name": i, "id": i} for i in df.columns]
#         else:
#             return dash.no_update, dash.no_update
#     except Exception as e:
#         print(e)
