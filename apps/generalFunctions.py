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