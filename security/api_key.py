from fastapi import Header, HTTPException

API_KEY = "minha-chave-secreta"


def verify_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Acesso negado")
