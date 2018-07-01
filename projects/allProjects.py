from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

layout = html.Div(id='content',className='container animate-bottom',style={'display':'none'},children=[
    html.Br(),
    html.H4("Some of the work I've done: "),
    html.Hr(),
    html.Br(),
    html.Div(className='row',children=[a[i] for i in range(len(a))
    ])
])
