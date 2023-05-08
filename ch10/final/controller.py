from kanye import YePI
from image import ImageAPI
from dash import Dash, html, dcc
from dash_bootstrap_components.themes import MATERIA
from dash.dependencies import Input, Output, State

class Controller:
    def __init__(self):
        '''
        initializes Controller class
        args: None
        '''
        self.app = Dash(external_stylesheets=[MATERIA])
        self.layout = self.create_layout()

    def create_layout(self):
        '''
        creates html.Div for the application layout
        args: None
        returns: html.Div
        '''

        initial_quote = YePI().get_quote()

        return html.Div(id='all',
            children=[
                html.Div([
                    html.H1(initial_quote, id='quote', style={'position': 'absolute',
                                                              'text-align':'center',
                                                              'top':'30%',
                                                              'color': 'white',
                                                              "text-shadow": "3px 3px black, -3px -3px black, 3px -3px black, -3px 3px black",
                                                              "font-family": "Lucida Console"}),
                    html.Img(src=ImageAPI().get_photo(), id='photo', style={'height': 'auto'}),
                        ], style={'position': 'relative'}),
                    html.Button('Get more YeSpiration', id='button', style={'justify-content':'center',                                        
                                                                        'font-size': '24px',
                                                                        'display': 'block',
                                                                        'margin': 'auto',
                                                                        'padding': '10px 20px'
                                                                    }),
            ],
            style={'position': 'relative',
                   'justify-content': 'center',
                   'display':'table', 
                   'width':'100%', 
                   'padding':'20px',
                   'align-items':'center'}
        )
    
    def site(self) -> None:
        '''
        initiallizes application using layout and a callback function that calls the application back if the specified input is changed
        args: None
        returns: None
        '''
        app = self.app
        app.title = "YePI"
        app.layout = self.layout
        @app.callback([Output('quote','children'), Output('photo','src')],
                      Input('button', 'n_clicks'),
                      prevent_initial_call = True)
        def update_site(n_clicks):
                '''
                returns a new quote and image when the button is clicked
                args: n_clicks (int)
                returns: quote(str), image_url(str)
                '''
                quote = YePI().get_quote()
                image_url = ImageAPI().get_photo()
                return quote, image_url
        app.run()

        def __str__(self):
             '''
             specifies the app for the controller class
             args: None
             returns: str
             '''
             return f'app: {self.app}'
    
