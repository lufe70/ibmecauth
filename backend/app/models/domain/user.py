"""
Modelos de domínio para usuários
"""
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    """Modelo base para usuários"""
    username: str
    email: Optional[EmailStr] = None
    name: Optional[str] = None

class User(UserBase):
    """Modelo de usuário completo"""
    role: Optional[str] = Field(default="aluno")
    is_authenticated: bool = True
    
    class Config:
        schema_extra = {
            "example": {
                "username": "joao.silva",
                "email": "joao.silva@ibmec.edu.br",
                "name": "João Silva",
                "role": "aluno",
                "is_authenticated": True
            }
        }

class UserResponse(UserBase):
    """Modelo para resposta de usuário com informação de perfil"""
    role: str
    
    class Config:
        schema_extra = {
            "example": {
                "username": "joao.silva",
                "email": "joao.silva@ibmec.edu.br",
                "name": "João Silva",
                "role": "aluno"
            }
        }
