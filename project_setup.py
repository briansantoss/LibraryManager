from constants import *
from db_tools import db_connection


@db_connection
def mk_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year DATE NOT NULL,
            price REAL NOT NULL   
        )
    ''')


# Definindo a função encarregada de criar toda a estrutura do projeto caso já não exista
def project_setup():
    BACKUPS_DIR.mkdir(exist_ok=True)
    EXPORTS_DIR.mkdir(exist_ok=True)
    IMPORTS_DIR.mkdir(exist_ok=True)
    DATA_DIR.mkdir(exist_ok=True)

    # Criando (caso não exista) o arquivo do banco de dados
    LIBRARY_DB.touch(exist_ok=True)

    # Criando a tabela de livros caso já não existente
    mk_table()
