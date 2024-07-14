import dash 
import pandas as pd 
import dash_bootstrap_components as dbc
from dash import dcc,html,dash_table
from dash.dependencies import Input, Output,State
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
from app import app
from df import df


main_config = {
    "hovermode": "x unified",
    "hoverlabel": {
        "bgcolor": "rgba(0,0,0,0.5)",
        "font": {"color": "white"}
    },
    "legend": {
        "yanchor":"top", 
        "y":0.9, 
        "xanchor":"left",
        "x":0.1,
        "title": {"text": None},
        "font" :{"color":"white"},
        "bgcolor": "rgba(0,0,0,0.5)"
    },
    "margin": {"l":30, "r":30, "t":30, "b":30}
}


layout=dbc.Container([
            dbc.Row([
                dbc.Col([
                    dcc.Markdown("""
                                    **Paginas / Graficos de Ventas**  
                                      Graficos
                                    """)
                ],md=10),
                dbc.Col([
                 
                    dbc.Button(html.I(className="fas fa-user-alt"), id='bt1', n_clicks=0,className="bton"),
                    html.Label("Sign Out",style={"font-weight": "bold"}),
                    dbc.Button(html.I(className="fas fa-cog"), id='bt2', n_clicks=0,className="bton"),
                    dbc.Button(html.I(className="fas fa-bell"), id='bt3', n_clicks=0,className="bton"),
            
                    dbc.Popover([
                        dbc.PopoverHeader("Perfil Usuario"),
                        dbc.PopoverBody([
                            dbc.Row([
                                dbc.Col([
                                    html.Label("Usuario"),
                                    html.Label("Area"),
                                    html.Label("Correo"),
                                    html.Label("Telefono"),
                                ],md=4),
                                dbc.Col([
                                    html.Label("Luis lopez chavez"),
                                    html.Label("Tesoreria"),
                                    html.Label("xxxxxxx@gmail.com"),
                                    html.Label("xxxxxxx"),
                                ],md=8)
                            ]),
                            dbc.Button("Cerrar", id='bt4',className="boton-popover"), 
                        ]),
                    ],id="popover1", target="bt1", is_open=False, placement='bottom', trigger="focus"),
                    dbc.Popover([
                        dbc.PopoverHeader("Tema"),
                        dbc.PopoverBody([
                                dbc.RadioItems(
                                    options=[
                                        {'label': 'Oscuro', 'value': 'Oscuro'},
                                        {'label': 'Claro', 'value': 'Claro'}
                                    ],
                                    value='Claro',
                                    labelStyle={"display": "block"}
                                ),
                                dbc.Button("Cerrar", id='bt5',className="boton-popover",n_clicks=0), 
                        ])             
                    ],id="popover2", target="bt2", is_open=False, placement='bottom'),
                    dbc.Popover([
                        dbc.PopoverHeader("Notificaciones"),
                        dbc.PopoverBody([
                            dbc.Button("Cerrar", id='bt6',className="boton-popover",n_clicks=0), 
                        ])
                    ],id="popover3", target="bt3", is_open=False, placement='bottom',trigger="focus"),
                    

                ],className="mb-4")
            ]),
            #tarjetas e iconos
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        html.I(className="fas fa-comments-dollar"),className="card1",
                    ),
                    dbc.Card([
                        html.Legend("Total Ventas",className="titulo1"),
                        html.H5("total",id="total_ventas",className="titulo2"),   
                    ],className="card2",)
                ],xs=12, sm=12, md=6, lg=3,className="mb-4"),
                dbc.Col([
                    dbc.Card(
                        html.I(className="fas fa-balance-scale-right"),className="card1",
                    ),
                    dbc.Card([
                        html.Legend("Total Utilidad",className="titulo1"),
                        html.H5("total",id="total_utilidad",className="titulo2"),   
                    ],className="card2")
                ],xs=12, sm=12, md=6, lg=3,className="mb-4"),
                dbc.Col([
                    dbc.Card(
                        html.I(className="fas fa-chart-pie"),className="card1",
                    ),
                    dbc.Card([
                        html.Legend("Total costo Envio",className="titulo1"),
                        html.H5("total",id="total_costo",className="titulo2"),   
                    ],className="card2")
                ],xs=12, sm=12, md=6, lg=3,className="mb-4"),
                dbc.Col([
                    dbc.Card(
                        html.I(className="fas fa-coins"),className="card1",
                    ),
                    dbc.Card([
                        html.Legend("Total Descuento",className="titulo1"),
                        html.H5("total",id="total_descuento",className="titulo2"),   
                    ],className="card2")
                ],xs=12, sm=12, md=6, lg=3,className="mb-4"),

            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                html.H5("Total Ventas"),   
                            ],className="tarjeta"),
                        ],md=10,xs=12, sm=12)
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id="grafico1",className="barra1")
                        ],md=10,xs=12, sm=12)
                    ])  
                ],xs=12, sm=12,md=4,className="mb-4"),

                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                html.H5("Total Ventas"),   
                            ],className="tarjeta"),
                        ],md=10,xs=12, sm=12)
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id="grafico2",className="barra1")
                        ],md=10,xs=12, sm=12)
                    ])  

                ],xs=12, sm=12, md=4, className="mb-4"),
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                html.H5("Total Ventas"),   
                            ],className="tarjeta"),
                        ],md=10,xs=12, sm=12)
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id="grafico3",className="barra1")
                        ],md=10,xs=12, sm=12)
                    ])  
                ],xs=12, sm=12, md=4, className="mb-4"),
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                             dash_table.DataTable(
                                id="tabla_agrupada",
                                columns=[{"name": i, "id": i} for i in ["Categoria", "Subcategoria", "Cantidad", "Ventas", "Utilidad"]],
                                data=df.to_dict('records'),
                                sort_action="native",
                                filter_action="native",
                                page_action="native",
                                page_current=0,
                                page_size=10,
                            
                                    style_cell={  
                                        'padding': '5px',  
                                        'text-align': 'center',  
                                        'minWidth': '50px',  
                                        'maxWidth': '100px',  
                                        'overflow': 'hidden',  
                                        'textOverflow': 'ellipsis',
                                        "font-size": "13px",
                                 
                                      
                                     
                                   },
                                    style_header={  
                                        'font-size': '16px',         
                                        'fontWeight': 'bold',
                                        'backgroundColor': 'black',
                                        'color': 'white',
                                        'minWidth': '20px',
                                        'maxWidth': '100px',
                                        'textAlign': 'center',
                                        'maxheight': '27px',
                                        'height': '48px'
                                 },
                             
                                style_table={  
                                    'overflowX': 'auto',  
                                    'width': '109%',  
                                    'height': '410px'
                                },      
                                
                                

                              )

                        ],xs=12, sm=12,lg=11)
                    ])
                   
                   
                
                ],lg=7,xs=12, sm=12),

                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id="grafico4")
                        ],md=12,xs=12, sm=12)
                    ])
                ],lg=5)
            ])

])

# formato numeros
def format_num(num):
    if num >=1000000000 :
        return "S/"+"{:,.0f}".format(num/1000)+ "B"
    elif num >=1000000 :
        return "S/"+"{:,.0f}".format(num/1000)+ "M"
    elif num >=1000 :
        return "S/"+"{:,.0f}".format(num)+ "K"
    else:
        return  "S/"+"{:,.2F}".format(num)



@app.callback(
    Output("popover2", "is_open"),
    [Input("bt2", "n_clicks"),
     Input("bt5", "n_clicks")],
) 
def toggle_popover(n, is_open):
    ctx=dash.callback_context
    if not ctx.triggered_id:
      raise PreventUpdate

    is_open= True if ctx.triggered_id=="bt2" else False
    return is_open

@app.callback(
    [Output("total_ventas", "children"),
    Output("total_utilidad", "children"),
    Output("total_costo", "children"),
    Output("total_descuento", "children"),
    Output("grafico1", "figure"),
    Output("grafico2", "figure"),
    Output("grafico3", "figure"),
    Output("tabla_agrupada","data")],                          
    [Input("lista1", "value"),
    Input("lista2", "value"),
    Input("lista3", "value")],
)
def update_output(n1,n2,n3):
    dfz=df.copy()
    
    if n1 :
        dfz=dfz[dfz['Subcategoria'].isin(n1)]
    if n2 :
        dfz=dfz[dfz['Empaque'].isin(n2)]
    if n3 :
        dfz=dfz[dfz['Region'].isin(n3)]

    total_ventas=format_num(dfz['Ventas'].sum())
    total_utilidad=format_num(dfz['Utilidad'].sum())
    total_costo=format_num(dfz['Costo_envio'].sum())
    total_descuento=format_num(dfz['Descuento'].sum())
     
  
    # grafico de barras
    
    df_vtas_años = dfz.groupby('Año')['Ventas'].sum().reset_index()
    # variacion porcentual devntas con respecto al año
    df_vtas_años['Variacion']=(df_vtas_años['Ventas'].pct_change()*100).round(2)
    fig_ventas=go.Figure()
    fig_ventas.add_trace(go.Bar(x=df_vtas_años['Año'], y=df_vtas_años['Ventas'], name='Ventas',marker=dict(color='#FFFFFF')))
    fig_ventas.add_trace(go.Scatter(x=df_vtas_años['Año'], y=df_vtas_años['Variacion'], name='Variacion', yaxis='y2'))
    fig_ventas.update_layout(barmode='group', yaxis2=dict(overlaying='y', side='right'))
    fig_ventas.update_layout(plot_bgcolor='#62A26E',paper_bgcolor='#62A26E',font_color='white')
    fig_ventas.update_layout(main_config,showlegend=False)
    fig_ventas.update_yaxes(showgrid=False)

     # grafico de barras

    df_utilidad_años = dfz.groupby('Año')['Utilidad'].sum().reset_index()
    # variacion porcentual de utilidad con respecto al año
    df_utilidad_años['Variacion']=(df_utilidad_años['Utilidad'].pct_change()*100).round(2)
    
    fig_utilidad=go.Figure()
    fig_utilidad.add_trace(go.Bar(x=df_utilidad_años['Año'], y=df_utilidad_años['Utilidad'], name='Utilidad',marker=dict(color='#FFFFFF')))
    fig_utilidad.add_trace(go.Scatter(x=df_utilidad_años['Año'], y=df_utilidad_años['Variacion'], name='Variacion', yaxis='y2'))
    fig_utilidad.update_layout(yaxis2=dict(overlaying='y', side='right'))
    fig_utilidad.update_layout(plot_bgcolor='#E7106F',paper_bgcolor='#E7106F',font_color='white')
    fig_utilidad.update_layout(main_config,showlegend=False)
    fig_utilidad.update_yaxes(showgrid=False)

    # grafico de circulo

    df_envio_años = dfz.groupby('Año')['Id'].count().reset_index()
    cantidad_total_envio=df_envio_años['Id'].sum()
   
    fig_costo=go.Figure()
    fig_costo.add_trace(go.Pie(labels=df_envio_años['Año'], values=df_envio_años['Id'], hole=.9))
    fig_costo.update_layout(paper_bgcolor='#0B0201',font_color='white')
    fig_costo.update_layout(main_config,showlegend=False)
    fig_costo.update_layout(
                annotations=[
                    dict(
                        text=str(cantidad_total_envio),
                        x=0.5,
                        y=0.55,
                        font_size=25,
                        showarrow=False,
                    ),
                    dict(
                        text="Cant. Envíos",
                        x=0.5,
                        y=--0.45,
                        font_size=15,
                        showarrow=False,
                    )
                ]
    )

    agrupar_tabla=dfz.groupby(["Categoria","Subcategoria"])[["Cantidad","Ventas","Utilidad"]].sum().reset_index()


    return total_ventas,total_utilidad,total_costo,total_descuento,fig_ventas,fig_utilidad,fig_costo,agrupar_tabla.to_dict('records')

    
 


   
   