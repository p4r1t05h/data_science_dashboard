from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app
from apps import missingTab, outliersTab, collinearTab, bivariateTab
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
                                    label='Missing Value Analysis',
                                    value='missing',
                                    className="custom-tab",
                                    selected_className="custom-tab--selected",
                                ),
                                dcc.Tab(
                                    id = 'oulier_tab',
                                    label='Outliers Analysis',
                                    value='outlier',
                                    className="custom-tab",
                                    selected_className="custom-tab--selected",
                                ),
                                dcc.Tab(
                                    id = 'collinear_tab',
                                    label='Collinearity Analysis',
                                    value='collinear',
                                    className="custom-tab",
                                    selected_className="custom-tab--selected",
                                ),
                                dcc.Tab(
                                    id = 'bivariate_tab',
                                    label='Bivariate Analysis',
                                    value='bivariate',
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
        elif at == 'outlier':
            return outliersTab.outliersTabBody
        elif at == 'collinear':
            return collinearTab.collinearTabBody
        elif at == 'bivariate':
            return bivariateTab.bivariateTabBody
    except Exception as e:
        print(traceback.format_exc())