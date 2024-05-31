import pyodbc

class DB:
    
    def __init__(self):
        pass
    
    def get_connection(self):
        return pyodbc.connect('Driver={SQL Server};'
                              'Server=GUILHERME\\SQLEXPRESS;'
                              'Database=BibliotecaDB;'
                              'UID=sa;'
                              'PWD=sa@123')