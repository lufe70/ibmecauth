"""
Middleware para configuração de CORS
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings

settings = get_settings()

def setup_cors_middleware(app: FastAPI) -> None:
    """
    Configura o middleware CORS na aplicação FastAPI
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
