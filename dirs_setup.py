from pathlib import Path

# Construindo o caminho completo para o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent

# Construindo o caminho completo para o resto da estrutura do projeto
BACKUPS_DIR = BASE_DIR / "backups"
DATA_DIR = BASE_DIR / "data"
EXPORTS_DIR = BASE_DIR / "exports"

LIBRARY_DB = BASE_DIR / DATA_DIR / "library.db"


# Definindo a função encarregada de criar toda a estrutura do projeto caso já não exista
def project_config():
    BACKUPS_DIR.mkdir(exist_ok=True)
    EXPORTS_DIR.mkdir(exist_ok=True)
    DATA_DIR.mkdir(exist_ok=True)

    LIBRARY_DB.touch(exist_ok=True)
