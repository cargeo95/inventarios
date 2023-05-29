from dash import dcc, html
import dash_bootstrap_components as dbc

# Importamos conexión
from python_to_postgres import *

data = select_proveedores()
ids = [item[0] for item in data]
options = [{'label': str(item), 'value': item} for item in ids]

result = dbc.Container(id='result')


update = dbc.Container([
    dcc.Dropdown(
        id='id_actualizar',
        options=options,
        placeholder="Seleccione un ID",
    ),
    html.Hr(),
    
    result,
    
    dbc.Button("Actualizar", id="update", color="success", className="mr-1"),
    
])

