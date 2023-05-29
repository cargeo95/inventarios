import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

#importamos backend
from backend.mostradatos import table 
from backend.insertar import *
from backend.delete import *
from backend.update import *


#importamos conexión
from python_to_postgres import *

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container([
    html.H1('TIENDA '),
    dbc.Tabs([
        dcc.Tab(
            label='READ',
            children=[
                html.H1('Mostrar datos'),
                table
            ]
    
            
        ),
        dcc.Tab(
            label='CREATE',
            children=[
                html.H1('Insertar datos'),
                form,
                html.H2(id='mensaje')
            ]
        ),
        
        dcc.Tab(
            label='UPDATE',
            children=[
                html.H1('Actualizar datos'),
                update,
                html.H2(id='mensaje_actualizar')
            ]
        ),
        dcc.Tab(
            label='DELETE',
            children=[
                html.H1('Eliminar datos'),
                borrar,
                html.H2(id='mensaje_borrar')
            ]
        )
    ]),       
])

@app.callback(
    Output('mensaje', 'children'),
    [Input('nit', 'value'),
     Input('nombre', 'value'),
     Input('direccion', 'value'),
     Input('telefono', 'value'),
     Input('submit', 'n_clicks')]
)

def insertar(nit,nombre, direccion, telefono, n_clicks):
    if n_clicks:
        insert_proveedores(nit, nombre, direccion, telefono)
        return "se agregaron los valores correctamente"
    
    

@app.callback(
    Output('mensaje_borrar', 'children'),
    [Input('id_borrar', 'value'),
     Input('delete', 'n_clicks')]
)
def eliminar(id_borrar, n_clicks):
    if n_clicks:
        deleteById(id_borrar)
        return "se eliminaron los valores correctamente"



@app.callback(
    Output('result', 'children'),
    [Input('id_actualizar', 'value')]
     
)
def show_by_id(selected_id):

    if selected_id is None:
        select = select_proveedores_by_id(1)
        
    else:
        select = select_proveedores_by_id(selected_id)
        
    return dbc.Table([
        html.Thead([
            html.Tr([
                html.Th("ID"),
                html.Th("NIT"),
                html.Th("Nombre"),
                html.Th("Dirección"),
                html.Th("Teléfono")
            ])
        ]),
        html.Tbody([
            html.Tr([
                html.Td(select[0][0]),
                html.Td(dbc.Input(id='nit_update', type='text', value=select[0][1])),
                html.Td(dbc.Input(id='nombre_update', type='text', value=select[0][2])),
                html.Td(dbc.Input(id='direccion_update', type='text', value=select[0][3])),
                html.Td(dbc.Input(id='telefono_update', type='text', value=select[0][4]))
            ])   
        ])
    ])
    
    
if 'nit_update' in app.layout:
    @app.callback(
        Output('mensaje_actualizar', 'children'),
        [Input('id_actualizar', 'value'),
        Input('nit_update', 'value'),
        Input('nombre_update', 'value'),
        Input('direccion_update', 'value'),
        Input('telefono_update', 'value'),
        Input('update', 'n_clicks')]
    )
    def update_by_id(id_actualizar, nit_update, nombre_update, direccion_update, telefono_update, n_clicks):
            
        if n_clicks:
            update_proveedores(id_actualizar, nit_update, nombre_update, direccion_update, telefono_update)
            return "se actualizaron los valores correctamente"


if __name__ == '__main__':
    app.run_server(debug=True)

