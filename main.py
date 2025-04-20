from fastapi import FastAPI
from database import Base, engine
from routers import user, workout

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Academia Unifor API",
    description="Backend para gerenciar usuários e treinos da Academia Unifor.",
    version="1.0.0",
)

app.include_router(user.router)
app.include_router(workout.router)
