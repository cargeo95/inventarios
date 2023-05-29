from dash import dcc, html
import dash_bootstrap_components as dbc


#importamos conexión
from python_to_postgres import *

def mostrarDatos():
    data = select_proveedores()
    table_rows = []
    for item in data:
        table_row = html.Tr([
            html.Td(item[0]),
            html.Td(item[1]),
            html.Td(item[2]),
            html.Td(item[3]),
            html.Td(item[4])      
        ])
        table_rows.append(table_row)

    table = dbc.Table([
        html.Thead([
            html.Tr([
                html.Th("ID"),
                html.Th("NIT"),
                html.Th("Nombre"),
                html.Th("Dirección"),
                html.Th("Teléfono")
            ])
        ]),
        html.Tbody(table_rows)
    ])

    return table

