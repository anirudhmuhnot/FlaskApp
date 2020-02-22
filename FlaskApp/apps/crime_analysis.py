
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd  # dataframe manipulation
import plotly.graph_objs as go
import numpy as np  # numerical computations
from start import app
import dash

df = pd.read_csv(
    './apps/data/crime_data/01_District_wise'
    '_crimes_committed_IPC_2001_2012.csv')
# most committed crimes most committed crimes

# second
s = df.sum(axis=0)
s.drop(['STATE/UT', 'DISTRICT', 'YEAR', 'TOTAL IPC CRIMES', 'OTHER IPC CRIMES'], inplace=True)
g1 = pd.DataFrame(s)
g1.columns = ['SUM']
g1 = g1.sort_values(by='SUM', ascending=False)
g1 = g1.reset_index()
g1.columns = ['Crime', 'Total']
colors = [[0, '#FAEE1C'], [0.33, '#F3558E'], [0.66, '#9C1DE7'], [1, '#581B98']]

# third
top5 = g1['Crime'][:5]
g2 = df.groupby(['STATE/UT', 'YEAR']).sum()
g2 = g2.reset_index()
g2.drop('YEAR', axis=1, inplace=True)
temp = g2.sort_values(by='STATE/UT')
temp.reset_index(inplace=True)

one = go.Bar(
    x=temp['STATE/UT'], y=temp[top5[0]], name=top5[0], marker=dict(color='#ffcdd2')
)

two = go.Bar(
    x=temp['STATE/UT'], y=temp[top5[1]], name=top5[1], marker=dict(color='#A2D5F2')
)

three = go.Bar(
    x=temp['STATE/UT'], y=temp[top5[2]], name=top5[2], marker=dict(color='#59606D')
)

four = go.Bar(
    x=temp['STATE/UT'], y=temp[top5[3]], name=top5[3], marker=dict(color='#3459AD')
)

five = go.Bar(
    x=temp['STATE/UT'], y=temp[top5[4]], name=top5[4], marker=dict(color='#3459AD')
)

data3 = [one, two, three, four, five]
layout3 = {
    'title': 'Comparative study of top 5 crimes',
    'titlefont': dict(size=24, family='Courier New, monospace'),
    'margin': go.Margin(b=100),
    'xaxis': dict(title='STATE', tickfont=dict(size=10)),
    'yaxis': dict(title='NUMBER OF CRIMES COMMITTED'),
    'font': dict(size=12, color='#7f7f7f'),
    'height': 600
}
# fourth
arr = [380581, 84580777, 1383727, 31205576, 104099452, 1055450, 25545198, 343709, 243247, 16787941, 1458545, 60439692,
       25351462, 6864602, 12541302, 32988134, 61095297, 33406061, 64473, 72626809, 112374333, 2721756, 2966889, 1097206,
       1978502, 41974218, 1247953, 27743338, 68548437, 610577, 72147030, 3673917, 199812341, 10086292, 91273115]
pop = pd.DataFrame(arr)
pop.columns = ['Population']
g4 = df[df['YEAR'] == 2011]
g4 = g4.groupby('STATE/UT').sum()
g4.drop('YEAR', inplace=True, axis=1)
g4.reset_index(inplace=True)
g4['POPULATION'] = pop['Population']
pop = g4
y = (g4['TOTAL IPC CRIMES'] / g4['POPULATION']) * 100

data4 = [go.Bar(x=g4['STATE/UT'], y=y )]
layout4 = {
    'title': '% of State population committing a Crime (Census 2011)',
    'titlefont': dict(size=24, family='Courier New, monospace'),
    'margin': go.Margin(b=100),
    'xaxis': dict(title='STATE', tickfont=dict(size=10)),
    'yaxis': dict(title='% of Population'),
    'font': dict(size=12, color='#7f7f7f'),
    'height': 600
}

# fifth
# pie = html.Div(className='row', children=[
#     html.Div(className='col s12', children=[
#         html.Center(dcc.Graph(id="pie-graph", style={'height': '80vh', 'width': '80vh'}))
#     ]),
#     html.Div(className='col s12', children=[
#         html.Center(dcc.Slider(id='year-selected', min=2001, max=2012, value=2001,
#                                marks={2001: "2001", 2002: "2002", 2003: "2003", 2004: "2004", 2005:
#                                    "2005", 2006: "2006", 2007: "2007", 2008: "2008", 2009: "2009", 2010: "2010",
#                                       2011: "2011", 2012: "2012"}))
#     ])
# ])

temp2 = df.groupby(['STATE/UT', 'YEAR']).sum()
temp2 = temp2.reset_index()
temp2.drop('YEAR', axis=1, inplace=True)
k = []
# top5 total crime committed by state
for i in top5:
    temp2 = temp2.sort_values(by=i, ascending=False)
    k.append(dcc.Graph(id=i, figure={
        'data': [go.Bar(
            x=temp2['STATE/UT'],
            y=temp2[i]
        )],
        'layout': {
            'title': i,
            'titlefont': dict(size=24, family='Courier New, monospace'),
            'margin': go.Margin(b=200),
            'xaxis': dict(title='STATE', tickfont=dict(size=10)),
            'yaxis': dict(title='NUMBER OF CRIMES COMMITTED'),
            'font': dict(size=12, color='#7f7f7f')
        }
    }))

# layout_final
layout = html.Div(className='animated zoomIn flow-text',children=[
    html.H2('IPC Crime Visualisation(2001-2012)'),
    dcc.Graph(
        id='one',
        figure={
            'data': [go.Bar(
                x=df['STATE/UT'], y=df['TOTAL IPC CRIMES'], name='TOTAL IPC CRIMES', marker=dict(color='#F3558E')
            )],
            'layout': {
                'title': 'NUMBER OF CRIMES COMMITTED IN DIFFERENT STATES',
                'font': dict(size=12, color='#7f7f7f'),
                'titlefont': dict(size=24, family='Courier New, monospace'),
                'margin': go.Margin(b=130, pad=3),
                'xaxis': dict(title='State', tickfont=dict(size=10)),
                'yaxis': dict(title='Number Of Crimes Committed'),
                'height': 600
            }
        }
    ),
    dcc.Graph(
        id='two',
        figure={
            'data': [go.Scatter(
                x=g1['Crime'],
                y=g1['Total'],
                mode='markers',
                marker=dict(
                    size=15,
                    color=np.random.randn(500),
                    colorscale=colors,
                    showscale=True
                )
            )],
            'layout': {
                'title': 'NUMBER AND TYPES OF CRIME COMMITTED',
                'titlefont': dict(size=24, family='Courier New, monospace'),
                'margin': go.Margin(b=200),
                'xaxis': dict(title='CRIME', tickfont=dict(size=10)),
                'yaxis': dict(title='NUMBER OF CRIMES COMMITTED BY TYPE'),
                'font': dict(size=12, color='#7f7f7f'),
                'height': 600
            }
        }
    ),
    dcc.Graph(
        id='three',
        figure=go.Figure(data=data3, layout=layout3)
    ),
    dcc.Graph(
        id='four',
        figure=go.Figure(data=data4, layout=layout4)
    ),

    # pie,
    html.H4('Top 5 Crimes committed in States'),
    k[0], k[1], k[2], k[3], k[4]
])


# @app.callback(
#     dash.dependencies.Output("pie-graph", "figure"),
#     [dash.dependencies.Input("year-selected", "value")]
# )
# def update_graph(selected):
#     agg = df[df["YEAR"] == selected][["TOTAL IPC CRIMES", "STATE/UT"]]
#     agg.groupby('STATE/UT').sum()
#     return {
#         "data": [go.Pie(labels=agg['STATE/UT'], values=agg['TOTAL IPC CRIMES'], name='STATE', pull=.15, hole=.25,
#                         textposition='none', textinfo='text')],
#         "layout": go.Layout(title=f"Cases Reported Yearly"),
#     }
