import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Usa a variável de ambiente DB_PATH ou um caminho local padrão
# Exemplo local: sqlite:///./academia.db
# Exemplo no Render: sqlite:////data/academia.db
DB_PATH = os.getenv("DB_PATH", "sqlite:///./academia.db")

engine = create_engine(DB_PATH, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
