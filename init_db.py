import os
from database import Base, engine
from seed.seed_users import seed_users
from seed.seed_equipment import seed_equipment
from urllib.parse import urlparse

# Define e analisa o caminho do banco
raw_path = os.getenv("DB_PATH", "sqlite:///./academia.db")
parsed = urlparse(raw_path)
db_path = parsed.path  # Isso retorna /data/academia.db no Render

# Cria a pasta do banco, se necessário e permitido
dir_path = os.path.dirname(db_path)
if dir_path and not os.path.exists(dir_path):
    try:
        os.makedirs(dir_path, exist_ok=True)
    except PermissionError:
        print(
            f"⚠️ Sem permissão para criar o diretório '{dir_path}'. Certifique-se de que ele exista."
        )

# Cria o banco e popula se ainda não existir
if not os.path.exists(db_path):
    print("🔧 Criando o banco de dados e aplicando seeds...")
    Base.metadata.create_all(bind=engine)
    seed_users()
    seed_equipment()
else:
    print("✅ Banco de dados já existe. Pulando seed.")
