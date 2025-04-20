python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

sqlite3 academia.db < sql/gym_equipment_schema.sql
sqlite3 academia.db < sql/users_workouts_schema.sql

python -m seed.seed_users

uvicorn main:app --reload

http://localhost:8000/docs
