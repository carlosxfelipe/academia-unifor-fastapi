uvicorn main:app --host 0.0.0.0 --port 10000

rm academia.db
sqlite3 academia.db < sql/users_workouts_schema.sql
sqlite3 academia.db < sql/gym_equipment_schema.sql
python -m seed.seed_users
python -m seed.seed_equipment

Key: API_KEY
Value: G...

Key: DB_PATH
Value: sqlite:///./academia.db
