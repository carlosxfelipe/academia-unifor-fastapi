CREATE TABLE IF NOT EXISTS gym_equipment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    name TEXT NOT NULL,
    brand TEXT,
    model TEXT,
    quantity INTEGER,
    image TEXT,
    operational BOOLEAN DEFAULT TRUE
);
