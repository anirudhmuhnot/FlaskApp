import dash_html_components as html
import base64

img_name = './static/resume.png'
encoded_image = base64.b64encode(open(img_name, 'rb').read())
layout = html.Div(className='container',children=[
	html.Div(className='row',children=[
                            html.Div(className='col s12 m12 l12 animated zoomIn', children=[
                               html.Img(className='responsive-img',src='data:image/png;base64,{}'.format(encoded_image.decode()))
                            ])
	])
])