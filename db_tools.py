import sqlite3


# Definindo a função que vai estabelecer a conexão com o banco de dados para toda e qualquer operação nele feita
def db_connection(function):
    def wrapper():
        with sqlite3.connect('library.db') as connection:
            cursor = connection.cursor()
            function(cursor)
            connection.commit()
            return function(cursor)
    return wrapper
