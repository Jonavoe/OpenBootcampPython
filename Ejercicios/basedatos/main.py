
import sqlite3


def main():
    crear_alumnos("jonathan", "Voeffray")
    crear_alumnos("belen", "V")
    crear_alumnos("harry", "V")
    crear_alumnos("negri", "V")
    crear_alumnos("Amarrilo", "V")
    crear_alumnos("Colorado", "V")
    crear_alumnos("planta", "1")
    crear_alumnos("planta", "2")
    
def crear_alumnos(name, lastname):
    conn = sqlite3.connect('alumnos.db', isolation_level= None)
    cursor = conn.cursor()
    
    query = '''INSERT INTO alumnos(nombre, apellido) VALUES(?, ?)'''
    rows = cursor.execute(query,(name, lastname))
    print(type(rows))
    
    cursor.close()
    conn.close()  
    
if __name__ == '__main__':
    main()