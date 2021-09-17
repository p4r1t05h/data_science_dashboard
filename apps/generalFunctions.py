import base64
import datetime
import io

import pandas as pd
from apps import errorLogger
import traceback

import dash

####################################################################################
## parsing contents from uploaded file
####################################################################################

def parse_contents(contents, filename):
    # try:
        print('Hi')
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        return df
    # except Exception as e:
    #     errorLogger.insert_error('generalFunctions', 'parse_contents', str(e), traceback.format_exc())

####################################################################################
## Creating common settings for graphs
####################################################################################

common_Xaxes = dict(
    zeroline = False,
    showgrid = False,
    showticklabels = True,
    ticks = 'outside',
    tickwidth = 3,
    linewidth = 3
)

common_Yaxes = dict(
    zeroline = False,
    showgrid = False,
    showline = True,
    showticklabels = True,
    ticks = 'outside',
    tickwidth = 3,
    linewidth = 3
)

common_layout = dict(
    uniformtext_minsize = 8,
    uniformtext_mode = 'hide',
    font_family = 'time new roman',
    font_size = 16,
    autosize = False
)