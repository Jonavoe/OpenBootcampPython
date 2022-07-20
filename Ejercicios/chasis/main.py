import sqlite3


def main():
    crear_operarios("Juan", "Duarte")
    
def crear_operarios(name, lastname):
    conn = sqlite3.connect('chasis.db', isolation_level=None)
    cursor = conn.cursor()
    
    query = '''INSERT INTO operarios(nombre, apellido) VALUES(?, ?)'''
    rows = cursor.execute(query,(name, lastname))
    print(type(rows))
    
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()