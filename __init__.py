from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash
from flask import send_from_directory
import time
import base64
app = dash.Dash(static_folder='static')
app.config.supress_callback_exceptions = True

external_css = [
    'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css',
    'https://fonts.googleapis.com/icon?family=Material+Icons',
    '/static/base1.css'
]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = [
     'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/js/materialize.min.js'
]

for my_js in external_js:
  app.scripts.append_script({"external_url": my_js})


@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)

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
from projects import home,allProjects,student_dash,crime_analysis
#apps_database
apps = {
  'home':home,
  'allProjects':allProjects,
  'student_dash':student_dash,
  'crime_analysis':crime_analysis
}

#loaded navbar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(className='navbar-fixed',children=[
        html.Nav([
            html.Div(className='nav-wrapper grey darken-4',children=[
                dcc.Link(className='brand-logo right hide-on-med-and-down',children=[html.I(className='material-icons left',children=['blur_on']),'Anirudh Muhnot'],href='/projects/home'),
                html.Ul(className='left',children=[
                    dcc.Link(html.Li(children=[html.I(className='material-icons left',children=['home']),'Home']),href='/projects/home')
                ]),
                html.Ul(className='left',children=[
                    dcc.Link(html.Li(children=[html.I(className='material-icons left',children=['dashboard']),'Catalog']),href='/projects/allProjects')
                ]),
                html.Ul(className='left',children=[
                    dcc.Link(html.Li(children=[html.I(className='material-icons left',children=['contacts']),'Resume']),href='/projects/resume')
                ])
            ])
        ])
    ]),
    #display container, layouts are returned to this container
    html.Div(id='output',style={'display':'block'})
])

#for content
@app.callback(Output('output', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    for key,value in apps.iteritems():
      matchname = '/projects/'+key
      if pathname == matchname:
        return value.layout
    return home.layout

#for animation
@app.callback(Output('content', 'style'),
              [Input('url', 'pathname')])
def display_page(pathname):
    for key,value in apps.iteritems():
      matchname = '/projects/'+key
      if pathname == matchname:
        return {'display':'block'}
    return {'display':'block'}

server = app.server
if __name__ == '__main__':
    app.run_server(debug=True)
