from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
#dependencies
import pandas as pd #dataframe manipulation
import plotly.plotly as py #visualisation
import plotly.figure_factory as ff
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
from plotly.grid_objs import Grid, Column
import time
import numpy as np #numerical computations
import plotly.tools as tls

df = pd.read_csv('/var/www/FlaskApp/FlaskApp/projects/crime_data/01_District_wise_crimes_committed_IPC_2001_2012.csv')

layout = html.Div(children=[
    html.H1('IPC Crime Analysis'),
    html.Div(className='container',children=[
    	dcc.Graph(
    		id='one',
			figure = {
	    		'data' : [go.Bar(
	            	x=df['STATE/UT'],y=df['TOTAL IPC CRIMES'],name='TOTAL IPC CRIMES',marker=dict(color='#F3558E')
	    		)],
	    		'layout' : {
			        'title':'NUMBER OF CRIMES COMMITTED IN DIFFERENT STATES',
			        'font':dict(size=12, color='#7f7f7f'),
			        'titlefont':dict(size=24,family='Courier New, monospace'),
			        'height':620,
			        'margin':go.Margin(b=130,pad=3),
			        'xaxis':dict(title='State',tickfont=dict(size=10)),
			        'yaxis':dict(title='Number Of Crimes Committed')
	    		}
			}
    	)
    ])
])