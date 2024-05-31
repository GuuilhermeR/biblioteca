
import os, pyodbc

from database.database import DB

# https://www.bosontreinamentos.com.br/programacao-em-python/como-acessar-bancos-de-dados-sql-server-usando-python/

if __name__ == "__main__":
        
    # Criar um objeto cursor    
    conn = DB().get_connection()
    cursor = conn.cursor()

    # Comando SQL a executar
    cursor.execute('SELECT name, city FROM Person')
        
    for row in cursor:
        print(f'{row.name} - {row.city}')

    conn.close()