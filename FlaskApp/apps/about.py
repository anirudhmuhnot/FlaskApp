from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import base64

img_name = './static/profile.jpeg'
encoded_image = base64.b64encode(open(img_name, 'rb').read())
layout = html.Div(id='content', className='', children=[
                html.Div(className='',children=[
                    html.Div(className='container',children=[
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Div(className='row',children=[
                            html.Div(className='col s12 m12 l6 animated zoomIn hide-on-med-and-down', children=[
                                    html.Div(className='row',children=[
                                        html.Div(className='col s2 m2 l2'),
                                        html.Div(className='col s8 m8 l8  valign-wrapper',style={'height':'35vh'},children=[
                                            html.Img(className='responsive-img',src='data:image/png;base64,{}'.format(encoded_image.decode()))
                                            ]),
                                        html.Div(className='col s2 m2 l2')
                                        ])
                                    ]),
                            html.Div(className='col s12 m12 l6 animated zoomIn hide-on-large-only', children=[
                                    html.Div(className='row',children=[
                                        html.Div(className='col s2 m2 l2'),
                                        html.Div(className='col s8 m8 l8  valign-wrapper',children=[
                                            html.Img(className='responsive-img',src='data:image/png;base64,{}'.format(encoded_image.decode()))
                                            ]),
                                        html.Div(className='col s2 m2 l2')
                                        ])
                                    ]),
                            html.Div(className='col s12 m12 l6 animated zoomIn hide-on-med-and-down',children=[
                                html.Div(className='row', children=[
                                    html.Div(className='col s2 m2 l2'),
                                    html.Div(className='col s8 m8 l8  valign-wrapper',style={'height':'35vh'},children=[
                                        dcc.Link(html.A(className=' hoverable btn-large waves-effect waves-light blue', children=['Portfolio']),href='/apps/allProjects')
                                        ]),
                                    html.Div(className='col s2 m2 l2')
                                    ])
                                ]),
                            html.Div(className='col s12 m12 l6 animated zoomIn hide-on-large-only',children=[
                                html.Div(className='row', children=[
                                    html.Div(className='col s2 m2 l2'),
                                    html.Center(html.Div(className='col s8 m8 l8  center',children=[
                                        dcc.Link(html.A(className=' hoverable btn-large waves-effect waves-light blue', children=['Portfolio']),href='/apps/allProjects')
                                        ])),
                                    html.Div(className='col s2 m2 l2')
                                    ])
                                ])
                            ])     
                        ])
                ]),
                # start of second section
                html.Footer(className='page-footer white black-text flow-text', children=[
                    html.Div(className='container', children=[
                        html.Div(className='row', children=[
                            html.Div(className='col l6 s12', children=[
                                html.H5(className='black-text', children=[
                                    'What I do'
                                ]),
                                html.P(className='grey-text', children=[
                                    "I'm a freelancer working on Machine Learning projects and understanding state-of-the-art research papers. If you like these projects"
                                    " and want to help your organisation deploy them, you can contact me: "
                                ])
                            ]),
                            html.Div(className='col l3 s12', children=[
                                html.H5(className='black-text', children=[
                                    'Social Media'
                                ]),
                                html.Ul(children=[
                                    html.Li(html.A(className='blue-text', children=['Linked In'],
                                                   href='https://www.linkedin.com/in/anirudhmuhnot/')),
                                    html.Li(html.A(className='blue-text', children=['Freelancer'],
                                                   href='https://www.freelancer.com/u/anirudhmuhnot')),
                                    html.Li(className='grey-text', children=['Contact: anirudhmuhnot@icloud.com'])
                                ])
                            ])
                        ])
                    ]),
                    html.Div(className='footer-copyright', children=[
                        html.Div(className='container grey-text', children=[
                        'Made by Anirudh Muhnot'
                        ])
                    ])
                ])
    ])
