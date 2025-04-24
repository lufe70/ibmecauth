"""
Modelos de domínio para tokens de autenticação
"""
from typing import Optional
from pydantic import BaseModel

class Token(BaseModel):
    """Modelo para token de acesso"""
    access_token: str
    token_type: str = "bearer"
    
    class Config:
        schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer"
            }
        }

class TokenPayload(BaseModel):
    """Modelo para o payload do token JWT"""
    sub: Optional[str] = None  # Username do usuário
    exp: int                   # Timestamp de expiração
