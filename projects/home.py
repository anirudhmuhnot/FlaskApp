from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import os
a = []
#database to be .. content
content = {
	'About Me':["I'm a final year Computer Science student at Techno India NJR, Udaipur, India. Discovered my passion early on in my life and haven't stopped ever since. I had trouble finding good explainations to ML techniques and their practial applications from scratch, so this website is a result of that! Hope You enjoy it.",'perm_identity'],
	'Practial applications at heart':['This webiste is an implementation of the techniques described. UI is created by Dash framework introduced by plotly. All the codes are running on the website for practical demonstration.','view_carousel'],
	'Help me improve':['Feel free to comment and post any issue regarding the project for more through explaination. If you identify any bug, let me know. Your feedback matters. You can email me at anirudhmuhnot30u30@gmail.com Thank you. Cheers.','settings']
}
for key,values in content.iteritems():
	a.append(
		html.Div(className=['col s12 m4'],children=[
			html.Div(className='icon-block',children=[
				html.H2(className='center light-blue-text',children=[
					html.I(className='material-icons medium',children=[
						values[1]
					])
				]),
				html.H5(className='center',children=[
					key
				]),
				html.P(className='light',children=[
					values[0]
				])
			])
		])
		)


layout = html.Div(id='content',className='animate-bottom',style={'display':'none'},children=[
        	html.Div(className='section no-pad-bot',children=[
        		html.Div(className='container',children=[
        			html.Br(),
        			html.H1(className='header center blue-text',children=['Hi.']),
        			html.Div(className='row center',children=[
        				html.H5(className='header col s12 light',children=[
        					'Here you can find some real world Machine Leraning Projects with UI and github link for the same.'
        				])
        			]),html.Br(),
        			html.Div(className='row center',children=[
        				dcc.Link(html.A(className='btn-large waves-effect waves-light orange', children=['Catalog']),href='/projects/allProjects')
        			])
        		])
        	]),
        	#start of second section
        	html.Div(className='container',children=[
        		html.Div(className='section',children=[
        			html.Div(className='row',children=[
        				a[i] for i in range(len(a))
        			])
        		])
        	]),
		html.Footer(className='page-footer blue',children=[
			html.Div(className='container',children=[
				html.Div(className='row',children=[
					html.Div(className='col l6 s12', children=[
						html.H5(className='white-text',children=[
							'What I do'
						]),
						html.P(className='grey-text text-lighten-4',children=[
							"I'm a freelancer working on creating projects completley on my own. If you like these projects and want to help your organisation or business to deploy them, you can contact me: "
						])
					]),
					html.Div(className='col l3 s12',children=[
						html.H5(className='white-text',children=[
							'Social Media'
						]),
						html.Ul(children=[
							html.Li(html.A(className='white-text',children=['Linkedn'],href='https://www.linkedin.com/in/anirudhmuhnot/')),
							html.Li(html.A(className='white-text',children=['Freelancer'],href='https://www.freelancer.com/u/anirudhmuhnot')),
							html.Li(className='white-text',children=['Mail: anirudhmuhnot30u30@gmail.com']),
							html.Li(className='white-text',children=['Mobile: +91-9929303508'])
						])
					])
				])
			]),
			html.Div(className='footer-copyright',children=[
				html.Div(className='container',children=[
					'Made by Anirudh Muhnot'
				])
			])
		])
])