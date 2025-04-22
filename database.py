import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define o caminho do banco de dados
DB_PATH = os.getenv("DB_PATH", "sqlite:///./academia.db")
# Para Render: usar DB_PATH="sqlite:////data/academia.db"

engine = create_engine(DB_PATH, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
