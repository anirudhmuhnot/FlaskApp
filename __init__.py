from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash
from flask import send_from_directory
import time
from projects import home,allProjects,student_dash,crime_analysis

app = dash.Dash()
app.config.supress_callback_exceptions = True

external_css = [
    'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css',
    'https://fonts.googleapis.com/icon?family=Material+Icons'
]

external_js = [
     'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/js/materialize.min.js'
]

for my_js in external_js:
  app.scripts.append_script({"external_url": my_js})


for css in external_css:
    app.css.append_css({"external_url": css})


#apps_database
apps = {
  'home':home,
  'allProjects':allProjects,
  'student_dash':student_dash,
  'crime_analysis':crime_analysis
}

#loaded navbar
app.layout = html.Div([
    html.Link(
        rel='stylesheet',
        href='/var/www/FlaskApp/FlaskApp/static/base1.css'
    ),
    html.Div('Assets loading locally'),
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

@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)

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