import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="python_img"
)

def search_chemical(cas_number):
    cursor = database.cursor()
    query = "SELECT name FROM chemical WHERE cas_number = %s"
    values = (cas_number, )
    cursor.execute(query, values)
    chemical_row = cursor.fetchall()
    if chemical_row:
        chemical_name = chemical_row[0][0]
        return chemical_name
    else:
        return None