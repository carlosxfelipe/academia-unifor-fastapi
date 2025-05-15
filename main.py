from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import user, workout, equipment, mood
from database import Base, engine
from routers import user, workout, auth, equipment, gemini, mood

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Academia Unifor API",
    description="Backend para gerenciar usuários e treinos da Academia Unifor.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Troque por ["http://localhost:3000"] se quiser limitar
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(workout.router)
app.include_router(equipment.router)
app.include_router(gemini.router)
app.include_router(mood.router)


@app.get("/")
def root():
    return {"status": "online"}
