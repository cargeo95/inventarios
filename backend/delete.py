from dash import dcc, html
import dash_bootstrap_components as dbc

# Importamos conexión
from python_to_postgres import *

data = select_proveedores()

ids = [item[0] for item in data]
options = [{'label': str(item), 'value': item} for item in ids]

borrar = dbc.Container([
    dcc.Dropdown(
        id='id_borrar',
        options=options,
        placeholder="Seleccione un ID",
    ),
    html.Br(),
    dbc.Button("Delete", id="delete", color="danger", className="mr-1")
])

