from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

a = []
# database to be .. content
content = {
    'About Me': [
        "I'm a Freelancer with Bachelors in Computer Science from Techno India NJR, Udaipur, India. Discovered my"
        "passion early on in my life and haven't stopped ever since. I had trouble finding good code explainations and"
        " implementations to recent ML techniques. So this website is a result of that! Hope You enjoy it.",
        'perm_identity'],
    'Applications': [
        'This website consists of Analysis and Dashboards made from various datasets publicly avaliable or scraped'
        ' online. All the Machine Learning models are trained and presented as an API. Dash by plotly is used for'
        ' creating the Dashboards.',
        'view_carousel'],
    'Collaborate': [
        "Email me at anirudhmuhnot@icloud.com to work on any interesting project or implementing a research paper"
        " to competing in Kaggle competetions.",
        'settings']
}
for key, values in content.items():
    a.append(
        html.Div(className='col s12 m4', children=[
            html.Div(className='icon-block', children=[
                html.H2(className='center light-blue-text', children=[
                    html.I(className='material-icons medium', children=[
                        values[1]
                    ])
                ]),
                html.H5(className='center', children=[
                    key
                ]),
                html.P(className='light', children=[
                    values[0]
                ])
            ])
        ])
    )

layout = html.Div(id='content', className='animated zoomIn', children=[
    html.Div(className='section no-pad-bot', children=[
        html.Div(className='container', children=[
            html.Br(),
            html.H1(className='header center blue-text', children=['Hi.']),
            html.Div(className='row center', children=[
                html.H5(className='header col s12 light', children=[
                    'Here you can find Dashboards deployed with Machine Learning models in the backend and '
                    'visualisation of various datasets.'
                ])
            ]), html.Br(),
            html.Div(className='row center', children=[
                dcc.Link(html.A(className='btn-large waves-effect waves-light orange', children=['Catalog']),
                         href='/apps/allProjects')
            ])
        ])
    ]),
    # start of second section
    html.Div(className='container', children=[
        html.Div(className='section', children=[
            html.Div(className='row', children=[
                a[i] for i in range(len(a))
            ])
        ])
    ]),
    html.Footer(className='page-footer blue', children=[
        html.Div(className='container', children=[
            html.Div(className='row', children=[
                html.Div(className='col l6 s12', children=[
                    html.H5(className='white-text', children=[
                        'What I do'
                    ]),
                    html.P(className='grey-text text-lighten-4', children=[
                        "I'm a freelancer working on creating projects completley on my own. If you like these projects"
                        " and want to help your organisation or business to deploy them, you can contact me: "
                    ])
                ]),
                html.Div(className='col l3 s12', children=[
                    html.H5(className='white-text', children=[
                        'Social Media'
                    ]),
                    html.Ul(children=[
                        html.Li(html.A(className='white-text', children=['Linkedn'],
                                       href='https://www.linkedin.com/in/anirudhmuhnot/')),
                        html.Li(html.A(className='white-text', children=['Freelancer'],
                                       href='https://www.freelancer.com/u/anirudhmuhnot')),
                        html.Li(className='white-text', children=['Mail: anirudhmuhnot@icloud.com']),
                        html.Li(className='white-text', children=['Mobile: +91-9929303508'])
                    ])
                ])
            ])
        ]),
        html.Div(className='footer-copyright', children=[
            html.Div(className='container', children=[
                'Made by Anirudh Muhnot'
            ])
        ])
    ])
])
