from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
# from app import app
import traceback
import plotly.express as px
import pandas as pd

####################################################################################
## Reading Data data
####################################################################################

df = pd.read_csv('./data/Life Expectancy Data.csv')
df['Year'] = df['Year'].astype(str)

corr = df.corr()

fig = px.imshow(corr)

##################################################################################
# Tab layout for Collinear Tab Analysis
##################################################################################

collinearTabBody = dbc.Container(
    [
        dbc.Row(
            [
                # dbc.Col(
                #     [
                #         dbc.Card(className='side_panel')

                #     ],
                #     width=3
                # ),
                dbc.Col(
                    [
                        dcc.Graph(figure=fig)
                    ],
                    width=8
                )
            ],
            align='start'
        )
    ],
    fluid=True
)
