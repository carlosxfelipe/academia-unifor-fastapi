from fastapi import APIRouter, Request, HTTPException
import os
import httpx

router = APIRouter(prefix="/gemini", tags=["Gemini"])

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


@router.post("/chat")
async def chat_with_gemini(request: Request):
    body = await request.json()
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}",
                json=body,
                headers={"Content-Type": "application/json"},
                timeout=10,
            )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao conectar com o Gemini: {e}"
        )
