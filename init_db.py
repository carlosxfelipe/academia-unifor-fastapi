import os
from database import Base, engine
from seed.seed_users import seed_users
from seed.seed_equipment import seed_equipment

# Extrai o caminho do arquivo .db
db_path = os.getenv("DB_PATH", "sqlite:///./academia.db").replace("sqlite:///", "")

if not os.path.exists(db_path):
    print("🔧 Criando o banco de dados e aplicando seeds...")
    Base.metadata.create_all(bind=engine)
    seed_users()
    seed_equipment()
else:
    print("✅ Banco de dados já existe. Pulando seed.")
