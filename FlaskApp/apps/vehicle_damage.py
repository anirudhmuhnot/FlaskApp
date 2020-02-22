from fastai.vision import *
import dash
from start import app
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import time
from base64 import decodestring
import numpy as np
import base64
img_name = './static/vehicle_damage.png'
encoded_image = base64.b64encode(open(img_name, 'rb').read())
layout = html.Div([
    html.Div(className='container animated zoomIn',children=[
    html.Div(className='row',children=[
        html.Div(className='col s12 m12 l12', children=[
            html.H3("Overview: "),
            html.H4(className='blue-text',children=['This application uses deep '
                                                                       'learning to '
                                                            'predict vehicle damage. Categories of Damages are: '
                                                    'Front/Rear Lights,Front/Rear Bumper, Windshield, Tire and Undamaged. Upload any car '
                                                    'image(s) to find the type of damage. '
                                                    '']),
            html.H3('Upload File(s): '),
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    'Drag and Drop or ',
                html.A('Select Files')
                ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Allow multiple files to be uploaded
            multiple=True
            ),
            html.Div(id='output-data-upload',className='row'),
            html.Div(className='row',children=[
                html.H5('Damage Categories: '),
                html.Br(),
                html.Img(className='responsive-img', src='data:image/png;base64,{}'.format(encoded_image.decode()))
                ])
        ])
    ])
])
])


def get_prediction(content):
    img = open_image(content)
    learn = load_learner('./apps/data/vehicle_damage')
    pred, idx, output = learn.predict(img)
    return pred,output,idx

def parse_contents(contents, filename, m):
    image = contents.split(',')[1]
    data = decodestring(image.encode('ascii'))
    with open("./apps/data/vehicle_damage/test/" + filename, "wb") as f:
        f.write(data)
    r,out,idx = get_prediction(str('./apps/data/vehicle_damage/test/'+filename))
    return html.Div(html.Div(className='row animated '+m,children=[
            html.Div(className='col s6 m6 l6',children=[
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Img(className='responsive-img', src=contents,height=400,width=400)]),
            html.Div(className='col s6 m6 l6', children=[
                html.Div(dcc.Graph(id=str(filename), figure={
                    'data': [go.Bar(x=np.array(out),
                                    y=['Bumper', 'Light', 'Windshield', 'Tire', 'No Damage'],
                                    orientation='h')]
                }))
            ]),
            html.H6('Predicted category of vehicle damage is: '+str(r)),
            html.Hr()
    ])
                    )

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents'),
               Input('upload-data', 'filename')
              ])
def update_output(list_of_contents, list_of_names):
    m=str(random.choice(['fadeIn', 'pulse', 'fadeInLeft', 'fadeInRight',
                        'fadeInUp', 'flipInX', 'rotateInDownLeft',
                        'rotateInUpLeft', 'zoomIn', 'rollIn'
                        ]))
    start_time = time.time()
    children=[]
    counter = 0
    if list_of_contents is not None:
        for c, n in zip(list_of_contents,list_of_names):
            if counter % 2 == 0:
                children.append(html.Div(className='row'))
            children.append(parse_contents(c,n,m))
            counter = counter + 1
        end_time = time.time()
        total =end_time-start_time
        children.append(html.Div(className='row', children=[
            html.Br(),
            html.Div(className='row', children=[
                html.Div(className='col s12 l12 m12', children=[
                    html.H4('Total Time: ' + str(round(total, 2)) + ' second(s)'),
                    html.H4('Avg. Time per prediction: ' + str(round(total / len(
                        list_of_contents), 2)) + ' second(s)')])
            ])
        ]))

    return children