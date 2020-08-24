import dash_html_components as html
import dash_core_components as dcc
import base64
#future database variables
projects = {
            'Crime Data Analysis': ['Analysis of IPSC crime committed from year 2001-2012.','crime_analysis'],
            'Car Damage Classifier': ['Machine Learning model/API to classify Vehicle Damage(Windshield, Front/Rear'
                                          ' headlights, Tire Front/Rear Bumper) using a dataset of 1000 images '
                                          'downloaded from Google. and Fast AI library','vehicle_damage'],
             'Trading Dashboard' : ['A Real-Time* Trading dashboard to compare Open Interest and Prices of various '
                                    'stocks using Bhavcopy and data scraped from moneycontrol.com.','trading_dashboard']
           }
a = []
for key,value in projects.items():
        img_name = './static/'+value[1]+'.png'
        encoded_image = base64.b64encode(open(img_name, 'rb').read())
        a.append(html.Div(className='col s6 m6 l4 animated zoomIn',children=[
                html.Div(className='card small hoverable',children=[
                    html.Div(className='card-image waves-effect waves-block waves-light',children=[
                        html.Img(className='activator',src='data:image/png;base64,{}'.format(encoded_image.decode()))
                    ]),
                    html.Div(className='card-content',children=[
                        html.Span(className='card-title activator grey-text text-darken-4',children=
                        [key,html.I(className='material-icons right',children=['more_vert'])]),
                        html.P(dcc.Link(html.A('View'),href='/apps/'+value[1]))
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


layout = html.Div(id='content',className='container flow-text',children=[
    html.Br(),
    html.H4(className='teal-text flow-text', children=["My Most Recent Projects: "]),
    html.Hr(),
    html.Br(),
    html.Div(className='row',children=[a[i] for i in range(len(a))
    ])
])
