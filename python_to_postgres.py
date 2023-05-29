import psycopg2

hostname = 'dpg-ch44skesi8ukt4pc73c0-a.oregon-postgres.render.com'
database = 'cigarreria_jx3v'
username = 'carlosgomez'
pwd = 'oISlMRxDOL28X5YfqJq1hDNJoDhO6CKe'
port_id = '5432'

conn = None
cur = None

try:
    conn = psycopg2.connect(
        host=hostname,
        user=username,
        password=pwd,
        dbname=database,
        port=port_id
    )
    ## mostramos proveedores
    def select_proveedores():
        data = []
        cur = conn.cursor()
        cur.execute(' SELECT * FROM proveedores ')
        for record in cur.fetchall():
            data.append(record)     
        conn.commit()
        cur.close()
        return data
    
    ## insertamos proveedores
    def insert_proveedores(nit,nombre, direccion, telefono):
        cur = conn.cursor()
        # cur.execute('INSERT INTO proveedores (nit, nombre, direccion, telefono) VALUES (%s, %s, %s, %s)', ( nombre, direccion, telefono))
        cur.execute('INSERT INTO proveedores (id, nit, nombre, direccion, telefono) VALUES (18, %s, %s, %s, %s)', ( nit, nombre, direccion, telefono))
        conn.commit()
        cur.close()
        
    
    def select_proveedores_by_id(id):
        data = []
        cur = conn.cursor()
        cur.execute('SELECT * FROM proveedores WHERE id = %s', (id,))
        for record in cur.fetchall():
            data.append(record)     
        conn.commit()
        cur.close()
        return data
        
    
    def update_proveedores(id, nit,nombre, direccion, telefono):
        cur = conn.cursor()
        cur.execute('UPDATE proveedores SET nit = %s, nombre = %s, direccion = %s, telefono = %s WHERE id = %s', (nit, nombre, direccion, telefono, id))
        conn.commit()
        cur.close()
        
    def deleteById(id):
        cur = conn.cursor()
        cur.execute('DELETE FROM proveedores WHERE id = %s', (id,))
        conn.commit()
        cur.close()
    
except Exception as e:
    print(e)
    print("No se conecto a la base de datos")

