from pathlib import Path

# Construindo o caminho completo para o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent

# Construindo o caminho completo para o resto da estrutura do projeto
BACKUPS_DIR = BASE_DIR / "backups"
DATA_DIR = BASE_DIR / "data"
EXPORTS_DIR = BASE_DIR / "exports"
IMPORTS_DIR = BASE_DIR / "imports"

# Construindo o caminho completo para o arquivo do banco de dados
LIBRARY_DB = BASE_DIR / DATA_DIR / "library.db"

# Definindo as opções/strings de cada um dos menus
MAIN_MENU = '''
[1] - Library Options
[2] - Admin Options
[3] - Quit System
'''

LIBRARY_MENU = '''
[1] - Add book
[2] - Display book(s) information(s)
[3] - Modify book price
[4] - Remove book
[5] - Filter book(s) by author
[6] - Go back
'''

ADMIN_MENU = '''
[1] - Export CSV data
[2] - Import CSV data
[3] - System Backup
[4] - Go back
'''