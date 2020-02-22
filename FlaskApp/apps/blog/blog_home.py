import dash_html_components as html
import dash_core_components as dcc
tds_popular = {"Title of the Post": ["Description of the post" , "PathName"]}
pop = []
for key,value in tds_popular.items():
    pop.append(html.Div(className='row', children=[
        html.Div(className='col s2 m2 l2'),
        html.Div(className='col s10 m10 l10', children=[
            html.H3(dcc.Link(children=[key], href='/apps/blog/' + value[1])),
            html.H5(str(value[0])),
            html.Br()])
        ])
    )
layout = html.Div(className='container', children=[
    html.Div(children=[
        html.H1(className='grey-text', children=['Popular Blog Posts: ']),
        pop[0]
    ]),
    html.Div(children=[
        html.H1(className='grey-text', children=['Recent Blog Posts: '])])
])
