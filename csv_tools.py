import csv
from project_setup import EXPORTS_DIR
from db_tools import db_connection

# Definindo o nome do arquivo de exportação
EXPORT_FILENAME = "books.csv"


@db_connection
def import_data(cursor):
    with open(EXPORTS_DIR / EXPORT_FILENAME, "w", newline="") as export_file:
        # Realiza e captura os registros da tabela correspondentes a pesquisa feita (se houverem)
        cursor.execute("SELECT * FROM books")
        query_results = cursor.fetchall()

        # Cria o leitor do arquivo CSV e escreve o resultado da consulta nele
        writer = csv.writer(export_file)
        writer.writerows(query_results)


import_data()
