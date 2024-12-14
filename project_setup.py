from constants import *
from db_tools import db_connection
import csv

@db_connection
def mk_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price REAL NOT NULL,   
            pub_year INTEGER NOT NULL,
            UNIQUE(title, author, pub_year)
        )
    """)


# Definindo a função encarregada de criar toda a estrutura do projeto caso já não exista
def project_setup():
    # Criando os diretórios necessários
    for needed_dir in NEEDED_DIRS:
        needed_dir.mkdir(exist_ok=True)

    # Criando (caso não exista) o arquivo do banco de dados
    LIBRARY_DB.touch(exist_ok=True)

    if not IMPORT_TESTFILE.exists() or IMPORT_TESTFILE.stat().st_size == 0:
        IMPORT_TESTFILE.touch()

        with open(IMPORT_TESTFILE, "w", encoding="utf-8", newline="") as test_file:
            csv.writer(test_file, delimiter=",").writerows([
                ("Title", "Author", "Price", "Pub Year"),
                ("Perigoso! Este livro contém coelhos!", "Tim Warnes", 24.90, 2024),
                ("Democracia: O Deus que falhou", "Hans-Hermann Hoppe", 86.90, 2014),
                ("É Assim que Acaba: 1", "Colleen Hoover", 38.94, 2018),
                ( "Nexus: Uma breve história das redes de informação, "
                  "da Idade da Pedra à inteligência artificial", "Yuval Noah Harari", 83.56, 2024,),
                ("A psicologia financeira: lições atemporais sobre fortuna, "
                 "ganância e felicidade", "Morgan Housel", 34.93, 2021)
            ])

    # Criando a tabela de livros caso já não existente
    mk_table()
