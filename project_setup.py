from constants import NEEDED_DIRS
from db_tools import db_init
from csv_tools import generate_sample_csv


# Definindo a função encarregada de criar toda a estrutura do projeto caso já não exista
def project_setup():
    # Criando os diretórios necessários
    for needed_dir in NEEDED_DIRS:
        needed_dir.mkdir(exist_ok=True)

    db_init()
    # Gerando o arquivo csv de amostra caso necessário
    generate_sample_csv()
