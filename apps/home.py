from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

home_body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dcc.Upload(
                                    id='upload-data',
                                    children=html.Div([
                                        'Drag and Drop or ',
                                        html.A('Select Files')
                                    ]),
                                    className = 'upload_btn',
                                ),

                            ],
                            className = 'side_panel'
                        )
                    ],
                    width=2
                ),
            ]
        )
    ]
)