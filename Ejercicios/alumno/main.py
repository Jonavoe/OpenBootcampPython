import sqlite3

def main():
    crear_alumno(1, "jonathan", "voeffray")
    
def crear_alumno(identificador, usuario_nombre, usuario_apellido):
    conn = sqlite3.connect('alumno.db', isolation_level=None)
    cursor = conn.cursor()
    
    query =  '''INSERT INTO alumnos(id, nombre, apellido) VALUES(?, ?, ?)'''
    # query = '''DELETE FROM users WHERE id = 1'''
    rows = cursor.execute(query,(identificador, usuario_nombre, usuario_apellido))
    print(type(rows))
    
    # conn.commit()
    cursor.close()
    conn.close()
    
    
if __name__ == '__mian__':
    main()