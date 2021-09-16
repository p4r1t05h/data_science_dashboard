import dash
import warnings
import dash_bootstrap_components as dbc
warnings.filterwarnings("ignore")

##################################################################################
# Defining style sheets
##################################################################################

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

##################################################################################
# Defining app and its server
##################################################################################

app = dash.Dash(__name__, external_stylesheets = [external_stylesheets, dbc.themes.FLATLY])

app.config.suppress_callback_exceptions = True

server = app.server

##################################################################################
# Calling app
##################################################################################

if __name__ == '__main__':
    app.run_server(debug=True)

