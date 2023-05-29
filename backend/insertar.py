from dash import dcc, html
import dash_bootstrap_components as dbc

form = dbc.Container([
    html.H2('Por favor, ingrese los datos coherentemente'),
    html.Br(),
    dbc.Input(id='nit', type='text', placeholder='NIT'),
    html.Br(),
    dbc.Input(id='nombre', type='text', placeholder='Nombre'),
    html.Br(),
    dbc.Input(id='direccion', type='text', placeholder='Dirección'),
    html.Br(),
    dbc.Input(id='telefono', type='text', placeholder='Teléfono'),
    html.Hr(),
    dbc.Button("Crear", id='submit',  color="primary", className="mr-1"),

])

