from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
import os
import httpx


router = APIRouter(prefix="/gemini", tags=["Gemini"])

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GREETINGS = ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]
ALLOWED_TOPICS = [
    "musculação",
    "treino",
    "bodybuilding",
    "alimentação",
    "nutrição",
    "exercício",
    "academia",
]


@router.post("/chat")
async def chat_with_gemini(request: Request):
    try:
        request_body = await request.json()
        original_contents = request_body.get("contents", [])
        user_input = original_contents[0]["parts"][0]["text"].lower()

        is_greeting = any(greeting in user_input for greeting in GREETINGS)
        is_allowed_topic = any(topic in user_input for topic in ALLOWED_TOPICS)

        if not is_greeting and not is_allowed_topic:
            return JSONResponse(
                content={
                    "candidates": [
                        {
                            "content": {
                                "role": "model",
                                "parts": [
                                    {
                                        "text": (
                                            "Desculpe, só posso responder perguntas relacionadas a musculação, "
                                            "treinos, alimentação e nutrição."
                                        )
                                    }
                                ],
                            },
                            "finishReason": "STOP",
                        }
                    ]
                },
                media_type="application/json; charset=utf-8",
            )

        system_instruction = {
            "role": "user",
            "parts": [
                {
                    "text": (
                        "Você é um assistente que responde sempre em português e apenas dúvidas sobre "
                        "musculação, treino, bodybuilding, alimentação e nutrição. "
                        "Se a pergunta não for relacionada a esses temas, diga que não pode responder."
                    )
                }
            ],
        }

        modified_body = {"contents": [system_instruction] + original_contents}

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}",
                json=modified_body,
                headers={"Content-Type": "application/json"},
                timeout=10,
            )

        response.raise_for_status()
        return JSONResponse(
            content=response.json(), media_type="application/json; charset=utf-8"
        )

    except httpx.HTTPStatusError as http_error:
        raise HTTPException(
            status_code=http_error.response.status_code, detail=str(http_error)
        )
    except Exception as general_error:
        raise HTTPException(
            status_code=500, detail=f"Failed to connect to Gemini: {general_error}"
        )
