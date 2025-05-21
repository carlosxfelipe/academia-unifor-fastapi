import os
from fastapi import Header, HTTPException
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def verify_key(x_api_key: str = Header(...)):
    # print("🔐 Recebido:", x_api_key)
    # print("🔐 Esperado:", API_KEY)
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Acesso negado")
