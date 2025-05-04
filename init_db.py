import os
from database import Base, engine
from seed.seed_users import seed_users
from seed.seed_equipment import seed_equipment
from urllib.parse import urlparse

# Define e analisa o caminho do banco
raw_path = os.getenv("DB_PATH", "sqlite:///./academia.db")
parsed = urlparse(raw_path)
db_path = parsed.path  # Isso retorna /data/academia.db no Render

try:
    print("🔧 Criando o banco de dados e aplicando seeds...")
    Base.metadata.create_all(bind=engine)
    seed_users()
    seed_equipment()
except Exception as e:
    print(f"⚠️ Erro ao inicializar o banco: {e}")
