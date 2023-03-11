from db import get_connection

try:
    connection = get_connection()
    with connection.cursor() as cursor:
       # cursor.execute('call consulta_alumnos()')
        #cursor.execute('call consulta_alumno(%s)',(4,))
        cursor.execute('call insertar_alumno(%s,%s,%s,%s)',('alexis','guapo','gvtq@haba.com','2023-03-11 18:03:00'))
       # resultset = cursor.fetchall()
       # for row in resultset:
        #    print(row)
    connection.commit()
    connection.close()

except Exception as ex: 
    print(ex)