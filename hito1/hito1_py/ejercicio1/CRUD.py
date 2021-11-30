import sqlite3

from sqlite3 import Error
con = sqlite3.connect('Tienda.db')
cursorObj = con.cursor()
def conectar():
    try:
        print("Conexión establecida")
    except Error:
        print(Error)

def tabla(con):
    cursorObj.execute(
        "CREATE TABLE personas(id integer PRIMARY KEY, nombre text, edad integer, ciudad text)")
    print("Tabla creada")

def insertar(con, entities = (0, '', 0, '')):
    cursorObj.execute('INSERT INTO personas(id, nombre, edad, ciudad) VALUES(?, ?, ?, ?)',entities)
    con.commit()

def mostrar(con):
    cursorObj.execute('SELECT * FROM personas')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

def borrar(con,id):
    cursorObj.execute('DELETE FROM personas WHERE id='+ str(id))
    con.commit()
    print("Borrando")

def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')
    return num


def update(con):
    while True:
        print("1 Modificar Nombre")
        print("2 Modificar Edad")
        print("3 Modificar Ciudad")
        print("4 Salir")

        modificar = (input())
        if (modificar == '1'):
            nombre = input("Nombre : ")
            cursorObj.execute('UPDATE personas SET nombre=?  WHERE id=?;', (nombre, id))
            con.commit()

        elif (modificar == '2'):
            edad = input("Edad : ")
            cursorObj.execute('UPDATE personas SET edad=? WHERE id=? ;', (edad, id))
            con.commit()

        elif (modificar == '3'):
            ciudad = input("Ciudad : ")
            cursorObj.execute('UPDATE personas SET ciudad=? WHERE id=? ;', (ciudad, id))
            con.commit()

        elif (modificar == '4'):
            return False
#tabla(con)
conectar()
salir = False
opcion = 0

while not salir:

    print("1. Insertar")
    print("2. Seleccionar")
    print("3. Update")
    print("4. Eliminar")
    print("5. Salir")

    print("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        id=input("Dime el id : ")

        nombre = input("Dime el nombre : ")

        edad = input("Dime la edad : ")

        ciudad = input("Dime la ciudad : ")
        insertar(con, entities=(id, nombre, edad, ciudad))
    elif opcion == 2:
        mostrar(con)
    elif opcion == 3:
        id = input("¿Qué id quieres cambiar? : ")
        cursorObj.execute('SELECT * FROM personas WHERE id=' + id)
        rows = cursorObj.fetchall()
        for row in rows:
            print(row)
        update(con)

    elif opcion == 4:
        id=input("Dime el id a borrar : ")
        borrar(con, id)
    elif opcion == 5:
        salir = True
    else:
        print("Introduce un numero entre 1 y 4")

print("Fin")
con.close()
