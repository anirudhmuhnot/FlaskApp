from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import base64


#future database variables
projects = {
            'Student Dashboard': ['A dashboard for tracking attendance, academic performance of students in realtime.','student_dash'], 
            'Crime Data Analysis': ['Analysis of IPSC crime committed from year 2000-2014.','crime_analysis']
           };
a = []
for key,value in projects.iteritems():
        img_name = '/static/'+value[1]+'.png'
        a.append(html.Div(className='col s6 m4 l4',children=[
                html.Div(className='card small',children=[
                    html.Div(className='card-image waves-effect waves-block waves-light',children=[
                        html.Img(className='activator',src='data:image/jpg;base64,{}'.format(base64.b64encode(open(img_name,'rb').read())))
                    ]),
                    html.Div(className='card-content',children=[
                        html.Span(className='card-title activator grey-text text-darken-4',children=[key,html.I(className='material-icons right',children=['more_vert'])]),
                        html.P(dcc.Link(html.A('View'),href='/projects/'+value[1]))
                    ]),
                    html.Div(className='card-reveal grey darken-1 white-text',children=[
                        html.Span(className='card-title grey-text text-darken-4',children=[
                        key,html.I(className='material-icons right',children=['more_vert'])
                        ]),
                        html.P(value[0])
                    ])  
                ])
            ])
        )

layout = html.Div(id='content',className='container animate-bottom',style={'display':'none'},children=[
    html.Br(),
    html.H4("Some of the work I've done: "),
    html.Hr(),
    html.Br(),
    html.Div(className='row',children=[a[i] for i in range(len(a))
    ])
])
