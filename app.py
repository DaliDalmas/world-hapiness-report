import dash
import dash_core_components as dcc 
import dash_html_components as html 
import pandas as pd
app = dash.Dash()

colors = {
    'background':'#000000',
    'text': '#FFFFFF'
}


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H3(
        children='WHAT MAKES THE WORLD HAPPY?',
        style={
            'textAlign': 'left',
            'color': colors['text']
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)