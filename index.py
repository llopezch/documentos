import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import html,dcc,dash_table
from dash.dependencies import Input, Output,State
from app import app
import lateral,grafico1,grafico2


app.layout = html.Div([
    dbc.Button(html.I(className="fas fa-sliders-h"), id='btmenu', n_clicks=0, className="menu-button"),
    lateral.layout,
    dcc.Location(id='url', refresh=False,pathname='/grafico1'),
    html.Div(id='page-content',
    className="content"
    )
],className="contenido-total")

@app.callback(Output('page-content', 'children'),
                Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/' or pathname == '/grafico1':
        return grafico1.layout
    if pathname == '/grafico2': 
        return grafico2.layout

# Callback para mostrar/ocultar el sidebar en dispositivos móviles
@app.callback(
    Output("lateral", "className"),
    [Input("btmenu", "n_clicks")],
    [State("lateral", "className")]
)
def toggle_sidebar(n_clicks, sidebar_class):
    if n_clicks:
        if "collapsed" in sidebar_class:
             # Si el sidebar está colapsado, expandirlo
            return sidebar_class.replace(" collapsed", "")
        else:
            # Si el sidebar está expandido, colapsarlo
            return sidebar_class + " collapsed"
    return sidebar_class


if __name__ == '__main__':
    app.run_server(debug=True)

