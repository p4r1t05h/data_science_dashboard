from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app
from apps import missingTab, outliersTab
import traceback


##################################################################################
# Tab layout for Exploratory Analysis Page
##################################################################################

eda_body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Tabs(
                            [
                                dcc.Tab(
                                    id = 'missing_tab',
                                    label='Missing Value Treatment',
                                    value='missing',
                                    className="custom-tab",
                                    selected_className="custom-tab--selected",
                                ),
                                dcc.Tab(
                                    id = 'oulier_tab',
                                    label='Outliers Treatment',
                                    value='outlier',
                                    className="custom-tab",
                                    selected_className="custom-tab--selected",
                                ),
                                dcc.Tab(
                                    id = 'scaling_tab',
                                    label='Feature Scaling',
                                    value='scaling',
                                    className="custom-tab",
                                    selected_className="custom-tab--selected",
                                ),
                                dcc.Tab(
                                    id = 'encoding_tab',
                                    label='Feature Encoding',
                                    value='encoding',
                                    className="custom-tab",
                                    selected_className="custom-tab--selected",
                                ),
                                dcc.Tab(
                                    id = 'selection_tab',
                                    label='Feature Selection',
                                    value='selection',
                                    className="custom-tab",
                                    selected_className="custom-tab--selected",
                                )
                            ],
                            id = 'eda_tabs',
                            value = 'missing',
                            className='custom-tabs'
                        ),
                        html.Div(id = 'eda_content')
                    ],
                )
            ]
        )
    ],
    fluid=True
)

##################################################################################
# Switiching between tabs
##################################################################################

@app.callback(
    Output('eda_content', 'children'),
    Input('eda_tabs', 'value')
)
def eda_switch_tab(at):
    try:
        if at == 'missing':
            return missingTab.missingTabBody
        if at == 'outlier':
            return outliersTab.outliersTabBody
    except Exception as e:
        print(traceback.format_exc())