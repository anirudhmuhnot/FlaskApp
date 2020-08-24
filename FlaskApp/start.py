import dash

external_css = [
    'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css',
    'https://fonts.googleapis.com/icon?family=Material+Icons',
    'https://codepen.io/muhnot/pen/bKzaZr.css', 
    'https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css'
]

external_js = [
     'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/js/materialize.min.js',
     'https://code.jquery.com/jquery-3.3.1.min.js',
     'https://codepen.io/muhnot/pen/bKzaZr.js'
]

app = dash.Dash(external_scripts=external_js,
                external_stylesheets=external_css,
                suppress_callback_exceptions=True
                )
app.title = 'Embracing Machine Learning'
server = app.server