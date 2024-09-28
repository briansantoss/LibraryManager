from pathlib import Path
from db_tools import db_connection

# Construindo o caminho completo para o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent

# Construindo o caminho completo para o resto da estrutura do projeto
BACKUPS_DIR = BASE_DIR / "backups"
DATA_DIR = BASE_DIR / "data"
EXPORTS_DIR = BASE_DIR / "exports"
IMPORTS_DIR = BASE_DIR / "imports"

LIBRARY_DB = BASE_DIR / DATA_DIR / "library.db"


@db_connection
def mk_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price REAL NOT NULL,   
            pub_year TEXT NOT NULL
        )
    ''')


""" DESCOMENTE PARA TESTAR AS INSERÇÕES
    cursor.execute('''
       INSERT INTO books(author, title, publication_year, price)
       VALUES ('Diário de um banana 1', 'Jeff Kinney', '2008-05-19', 46)
       ''')

    cursor.execute('''
        INSERT INTO books(author, title, publication_year, price)
        VALUES ('O Menino Maluquinho', 'Ziraldo', '2023-12-20', 25.20)
    ''')
"""

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
