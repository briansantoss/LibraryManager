import sqlite3


# Definindo a função que vai estabelecer a conexão com o banco de dados para toda e qualquer operação nele feita
def db_connection(function):
    def wrapper(*args, **kwargs):
        from project_setup import LIBRARY_DB
        with sqlite3.connect(LIBRARY_DB) as connection:
            cursor = connection.cursor()
            function(cursor, *args, **kwargs)
    return wrapper
