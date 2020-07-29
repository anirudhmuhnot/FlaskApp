from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from start import app 
from apps import about, allProjects, crime_analysis, vehicle_damage, trading_dashboard, resume
from apps.blog import blog_home
# apps_database
import dash
import base64

apps = {
    'About': about,
    'allProjects': allProjects,
    'crime_analysis': crime_analysis,
    'vehicle_damage': vehicle_damage,
    'trading_dashboard': trading_dashboard,
    'blog/blog_home' : blog_home,
    'resume' : resume
}

# loaded navbar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(className='navbar-fixed', children=[
        html.Nav([
            html.Div(className='nav-wrapper white', children=[
                dcc.Link(className='brand-logo right hide-on-med-and-down grey-text',
                         children=[html.I(className='material-icons left', children=['blur_on']), 'Anirudh Muhnot ML'],
                         href='/apps/about'),
                html.Ul(className='left', children=[
                    dcc.Link(html.Li(className='grey-text', children=[html.I(className='material-icons left', children=['home']), 'About']),
                             href='/apps/about')
                ]),
                html.Ul(className='left', children=[
                    dcc.Link(
                        html.Li(className='grey-text', children=[html.I(className='material-icons left', children=['dashboard']), 'Portfolio']),
                        href='/apps/allProjects')
                ]),
                html.Ul(className='left', children=[
                    dcc.Link(
                        html.Li(className='grey-text', children=[html.I(className='material-icons left', children=['contacts']), 'Resume']),
                        href='/apps/resume')
                ])
                # html.Ul(className='left', children=[
                #     dcc.Link(
                #         html.Li(className='grey-text hoverable', children=[html.I(className='material-icons left', children=['contacts']), 'Blog']),
                #         href='/apps/blog/blog_home')
                # ])
            ])
        ])
    ]),
    # display container, layouts are returned to this container
    dcc.Loading(id="loading-1", children=[html.Div(id='output', className = "white")], type="default", fullscreen=True)
])


@app.callback(Output('output', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    for key, value in apps.items():
        matchname = '/apps/' + key
        if pathname == matchname:
            return value.layout
    return about.layout

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True)
