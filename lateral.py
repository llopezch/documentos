import dash 
import pandas as pd 
import dash_bootstrap_components as dbc
from dash import dcc,html,dash_table
from df import df
from app import app
from dash.dependencies import Input, Output,State
df_temp=df.copy()

layout=dbc.Container([
        dbc.Row([
            dbc.Col([
                html.I(className="fas fa-th"),
            ],md=2,xs=2,sm=2),
            dbc.Col([
                html.H2('Ventas Totales',style={"font-size":"16px"}),
            ],md=10,xs=8,sm=8,className="lateral-header")    
        ]),
        html.Hr(style={"background-color":"white","height": "2px"}),
        dbc.Row([
            dbc.Nav([
                dbc.NavLink([html.I(className="fas fa-home me-2"), html.Span("Dashboard")], href="/grafico1", active="exact"),
                dbc.NavLink([html.I(className="fas fa-calendar-alt me-2"), html.Span("Projects")], href="/grafico2", active="exact"),
               
            ],vertical=True,pills=True,id="nav-link",)
        ],style={"margin-top":"30px"}),
        dbc.Row([
            html.H2("Data Filter",style={"font-size":"16px"})
        ],style={"margin-top":"30px"}),
        html.Hr(style={"background-color":"white","height": "2px"}),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.I(className="fas fa-envelope-open-text me-2")
                    ],md=2,xs=2,sm=2),
                    dbc.Col([
                        html.H2("Productos",style={"font-size":"13px"}),
                        dcc.Dropdown(
                            id='lista1',
                            clearable=False,
                            multi=True,                                             
                        )
                    ],md=10,xs=10,sm=10),
                ]),
                dbc.Row([
                    dbc.Col([
                        html.I(className="fas fa-bars")
                    ],md=2,xs=2,sm=2),
                    dbc.Col([
                        html.H2("Empaque",style={"font-size":"13px"}),
                        dcc.Dropdown(
                            id='lista2',
                            clearable=False,
                            multi=True,                                   
                        )
                    ],md=10,xs=10,sm=10),
                ],style={"margin-top":"10px"}),
                dbc.Row([
                    dbc.Col([
                        html.I(className="fas fa-calendar-alt me-2")
                    ],md=2,xs=2,sm=2),
                    dbc.Col([
                        html.H2("Pais",style={"font-size":"13px"}),
                        dcc.Dropdown(
                            id='lista3',
                            clearable=False,
                            multi=True, 
                                                        
                        )
                    ],md=10,xs=10,sm=10),    
                ],style={"margin-top":"10px"}),
            ])
        ],style={"margin-top":"10px"})               
],id="lateral",className="lateral")

@app.callback( Output('lista1', 'options'),
                [Input('lista2', 'value'),
                Input('lista3', 'value')]          
)

def selcecionar_lista1(value_b,value_c):  
    df_temp=df.copy()

    if value_b :
        df_temp=df_temp[df_temp['Empaque'].isin(value_b)]

    if value_c :
        df_temp=df_temp[df_temp['Region'].isin(value_c)]

    return [{"label": x, "value": x} for x in sorted(df_temp['Subcategoria'].unique())]

@app.callback(  Output('lista2', 'options'),
                [Input('lista1', 'value'),
                Input('lista3', 'value')]            
)

def selcecionar_lista1(value_a,value_c):  
    df_temp=df.copy()

    if value_a :
        df_temp=df_temp[df_temp['Subcategoria'].isin(value_a)]

    if value_c :
        df_temp=df_temp[df_temp['Region'].isin(value_c)]

    return [{"label": x, "value": x} for x in sorted(df_temp['Empaque'].unique())]


@app.callback(Output('lista3', 'options'),
               [Input('lista1', 'value'),
                Input('lista2', 'value')]            
)

def selcecionar_lista1(value_a,value_b):  
    df_temp=df.copy()

    if value_a :
        df_temp=df_temp[df_temp['Subcategoria'].isin(value_a)]

    if value_b :
        df_temp=df_temp[df_temp['Empaque'].isin(value_b)]


    return [{"label": x, "value": x} for x in sorted(df_temp['Region'].unique())]

