import pyodbc
from database.database import DB

def exibir_retorno_select(cursor):
    sql_select = 'SELECT name, city FROM Person'
    cursor.execute(sql_select)
    for row in cursor:
        print(f'{row.name} - {row.city}')

def inserir_registro(cursor):
    sql_insert = "INSERT INTO Person (name, bihDate, address, city, cellphone) VALUES (?, ?, ?, ?, ?)"
    pessoa = {
        "name": "Daniele",
        "birthDate": "1999-03-14",
        "address": "Rua Comandante Abdon Senna, 42.",
        "city": "Joinville, SC",
        "cellphone": "47999999999"
    }
    cursor.execute(sql_insert, pessoa['name'], pessoa['birthDate'], pessoa['address'], pessoa['city'], pessoa['cellphone'])
    conn.commit()

if __name__ == "__main__":
    try:
        with DB().get_connection() as conn:
            with conn.cursor() as cursor:
                exibir_retorno_select(cursor)
                inserir_registro(cursor)
                exibir_retorno_select(cursor)
    except pyodbc.Error as e:
        print(f"Erro de SQL: {e}")
    except Exception as e:
        print(f"Erro: {e}")