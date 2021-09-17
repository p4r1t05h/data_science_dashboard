from dash import dcc, html
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app
import traceback
import plotly.express as px
import pandas as pd
from apps import generalFunctions

####################################################################################
## Reading Data data
####################################################################################

df = pd.read_csv('./data/Life Expectancy Data.csv')
df['Year'] = df['Year'].astype(str)
colNames = df[df.dtypes[(df.dtypes=="float64")|(df.dtypes=="int64")].index.values].columns

##################################################################################
# Tab layout for Missing Tab Treatment
##################################################################################

outliersTabBody = dbc.Container(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.Label(html.B('Select Column Name')),
                                dcc.Dropdown(
                                    id='outliers_dropdown',
                                    options = [{'value': c, 'label':c} for c in colNames],
                                    className='dropdowns'
                                ),

                            ],
                            className='side_panel'
                        )

                    ],
                    width=3
                ),
                dbc.Col(
                    [
                        dcc.Graph(id = 'outliers_fig')
                    ],
                    width=8
                )
            ],
            align='start'
        )
    ],
    fluid=True
)

##################################################################################
# Function to update dropdown
##################################################################################

@app.callback(
    Output('outliers_fig', 'figure'),
    Input('outliers_dropdown', 'value')
)
def update_output(value):
    try:
        if value is not None:
            fig = px.box(df, y=value)
            fig.update_layout(
                generalFunctions.common_layout,
                width = 1000,
                height = 650
            )
            fig.update_xaxes(generalFunctions.common_Xaxes)
            fig.update_yaxes(generalFunctions.common_Yaxes)
            return fig
        else:
            return dash.no_update
    except Exception as e:
        print(traceback.format_exc())
