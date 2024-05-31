
import os, pyodbc

from database.database import DB

# https://www.bosontreinamentos.com.br/programacao-em-python/como-acessar-bancos-de-dados-sql-server-usando-python/

def exibir_retorno_select(cursor):
    cursor.execute('SELECT name, city FROM Person')
        
    for row in cursor:
        print(f'{row.name} - {row.city}')
    
        
def inserir_regitro(cursor):
    pessoa = {
            "name": "Daniele",
            "birthDate": "1999-03-14",
            "address": "Rua Comandante Abdon Senna, 42.",
            "city": "Joinville, SC",
            "cellphone": "47999999999"
            }
    sql_insert = f"INSERT INTO Person (name, birthDate, address, city, cellphone) VALUES (?, ?, ?, ?, ?)"
    
    cursor.execute(sql_insert, pessoa['name'], pessoa['birthDate'], pessoa['address'], pessoa['city'], pessoa['cellphone'])
    conn.commit()
    

if __name__ == "__main__":
        
    conn = DB().get_connection()

    cursor = conn.cursor()
    exibir_retorno_select(cursor)
    inserir_regitro(cursor)
    exibir_retorno_select(cursor)
    conn.close()
    