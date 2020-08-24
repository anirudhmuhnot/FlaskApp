from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import base64

par_image = './static/par_image.png'
encoded_par = base64.b64encode(open(par_image, 'rb').read())
layout = html.Div(id='content', className='', children=[


                    html.Div(id='index-banner',className='parallax-container',children=[
                        html.Div(className='section no-pad-bot',children=[
                            html.Div(className='container',children=[
                                html.Br(),
                                html.Br(),
                                html.H2(className='header center teal-text text-lighten-2',children=['"The happiest people I know are those who lose themselves in the service of others."']),
                                html.Div(className='row center',children=[
                                    html.H5(className='header col s12 light',children=['Description of the website'])
                                    ]),
                                html.Div(className='row center',children=[
                                    dcc.Link(html.A(className='btn-large waves-effect waves-light blue',children=['View Projects']),href='/apps/'+'allProjects')
                                    ]),
                                html.Br(),
                                html.Br()
                            ])
                        ]),
                        html.Div(className='parallax',children=[
                            html.Img(src='data:image/png;base64,{}'.format(encoded_par.decode()))
                            ])
                        ]),
                    html.Div(className='container animated zoomIn flow-text', children=[
                        html.Div(className='row', children=[
                            html.Div(className='col l6 s12', children=[
                                html.H5(className='teal-text', children=[
                                    'What I do: '
                                ]),
                                html.P(className='black-text flow-text', children=[
                                    "I'm a freelancer specializing in Machine Learning and Business Analytics. If you like these projects"
                                    " and want to help your organisation deploy them, you can contact me. "
                                ])
                            ]),
                            html.Div(className='col l3 s12', children=[
                                html.H5(className='teal-text', children=[
                                    'Contact: '
                                ]),
                                html.Ul(children=[
                                    html.Li(html.A(className='blue-text', children=['LinkedIn'],
                                                   href='https://www.linkedin.com/in/anirudhmuhnot/')),
                                    html.Li(html.A(className='blue-text', children=['Freelancer'],
                                                   href='https://www.freelancer.com/u/anirudhmuhnot')),
                                    html.Li(className='grey-text', children=['Email: anirudhmuhnot@icloud.com'])
                                ])
                            ])
                        ])
                    ]),
                    html.Footer(className='page-footer white black-text flow-text', children=[
                        html.Div(className='footer-copyright', children=[
                            html.Div(className='container grey-text', children=[
                            'Made by Anirudh Muhnot'
                            ])
                        ])
                    ])
                ])
