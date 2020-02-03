from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from app import app
from apps import home, allProjects, crime_analysis, vehicle_damage, trading_dashboard
from apps.blog import blog_home
# apps_database
apps = {
    'home': home,
    'allProjects': allProjects,
    'crime_analysis': crime_analysis,
    'vehicle_damage': vehicle_damage,
    'trading_dashboard': trading_dashboard,
    'blog/blog_home' : blog_home
}

# loaded navbar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(className='navbar-fixed', children=[
        html.Nav([
            html.Div(className='nav-wrapper white', children=[
                dcc.Link(className='brand-logo right hide-on-med-and-down grey-text',
                         children=[html.I(className='material-icons left', children=['blur_on']), 'Anirudh Muhnot'],
                         href='/apps/home'),
                html.Ul(className='left', children=[
                    dcc.Link(html.Li(className='grey-text', children=[html.I(className='material-icons left', children=['home']), 'Home']),
                             href='/apps/home')
                ]),
                html.Ul(className='left', children=[
                    dcc.Link(
                        html.Li(className='grey-text', children=[html.I(className='material-icons left', children=['dashboard']), 'Catalog']),
                        href='/apps/allProjects')
                ]),
                html.Ul(className='left', children=[
                    dcc.Link(
                        html.Li(className='grey-text', children=[html.I(className='material-icons left', children=['contacts']), 'Resume']),
                        href='/apps/resume')
                ]),
                html.Ul(className='left', children=[
                    dcc.Link(
                        html.Li(className='grey-text', children=[html.I(className='material-icons left', children=['contacts']), 'Blog']),
                        href='/apps/blog/blog_home')
                ])
            ])
        ])
    ]),
    # display container, layouts are returned to this container
    dcc.Loading(id="loading-1", children=[html.Div(id='output')], type="cube", fullscreen=True)
])


@app.callback(Output('output', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    for key, value in apps.items():
        matchname = '/apps/' + key
        if pathname == matchname:
            return value.layout
    return home.layout

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=9601, debug=True)
