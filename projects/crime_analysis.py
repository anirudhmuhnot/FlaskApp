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
#most committed crimes most committed crimes
s = df.sum(axis=0)
s.drop(['STATE/UT','DISTRICT','YEAR','TOTAL IPC CRIMES','OTHER IPC CRIMES'],inplace=True)
temp1 = pd.DataFrame(s)
temp1.columns=['SUM']
temp1 = temp1.sort_values(by='SUM',ascending=False)
temp1=temp1.reset_index()
temp1.columns=['Crime','Total']
colorscale = [[0, '#FAEE1C'], [0.33, '#F3558E'], [0.66, '#9C1DE7'], [1, '#581B98']]
top5 = temp1['Crime'][:5]
temp2 = df.groupby(['STATE/UT','YEAR']).sum()
temp2 = temp2.reset_index()
temp2.drop('YEAR',axis=1,inplace=True)
k=[]
#top5 total crime committed by state
for i in top5:
    temp2 = temp2.sort_values(by=i,ascending=False)
    k.append(dcc.Graph(id=i,figure = {
        'data':[go.Bar(
            x=temp2['STATE/UT'],
            y=temp2[i]
        )],
        'layout' : {
        'title': i,
        'titlefont':dict(size=24,family='Courier New, monospace'),
        'height':600,
        'margin':go.Margin(b=200),
        'xaxis':dict(title='STATE',tickfont=dict(size=10)),
        'yaxis':dict(title='NUMBER OF CRIMES COMMITTED'),
        'font':dict(size=12, color='#7f7f7f')
    }
    }))
layout = html.Div(children=[
    html.H2('IPC Crime Visualisation(2000-2012)'),
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
    ),
    dcc.Graph(
    	id='two',
    	figure={
	    	'data':[go.Scatter(
	    		x = temp1['Crime'],
			    y = temp1['Total'],
			    mode='markers',
			    marker=dict(
			        size='15',
			        color = np.random.randn(500),
			        colorscale=colorscale,
			        showscale=True
			    )
	   		 )],
	    	'layout' : {
		        'title':'NUMBER AND TYPES OF CRIME COMMITTED',
		        'titlefont':dict(size=24,family='Courier New, monospace'),
		        'height':600,
		        'margin':go.Margin(b=200),
		        'xaxis':dict(title='CRIME',tickfont=dict(size=10)),
		        'yaxis':dict(title='NUMBER OF CRIMES COMMITTED BY TYPE'),
		        'font':dict(size=12, color='#7f7f7f')
	    	}
		}	
	),
    k[i] for k in range(len(k))
])