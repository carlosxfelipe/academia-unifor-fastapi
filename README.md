# Academia Unifor API

API desenvolvida com **FastAPI** e **SQLite** para gerenciamento de usuários, treinos, exercícios e equipamentos de academia.

A API foi publicada e a documentação está disponível em: [https://academia-unifor-fastapi.onrender.com/docs](https://academia-unifor-fastapi.onrender.com/docs)

## Como executar o projeto

Siga os passos abaixo para rodar o projeto localmente:

### 1. Crie um ambiente virtual

```bash
python3 -m venv venv
```

### 2. Ative o ambiente virtual

```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Crie o banco de dados SQLite e aplique os esquemas

```bash
sqlite3 academia.db < sql/gym_equipment_schema.sql
sqlite3 academia.db < sql/users_workouts_schema.sql
```

### 5. Popule o banco de dados com os dados iniciais

```bash
python -m seed.seed_users
python -m seed.seed_equipment
```

### 6. Inicie o servidor FastAPI

```bash
uvicorn main:app --reload
```

### 7. Acesse a documentação interativa

Abra no navegador:

[http://localhost:8000/docs](http://localhost:8000/docs)
