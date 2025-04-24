"""
Funções relacionadas à segurança da aplicação
"""
from datetime import datetime, timedelta
from typing import Any, Dict, Optional, Union

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError

from app.core.config import get_settings
from app.models.domain.token import TokenPayload
from app.models.domain.user import User

settings = get_settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/token")

def create_access_token(subject: Union[str, Any], expires_delta: Optional[timedelta] = None, **extra_data) -> str:
    """
    Cria um token JWT com os dados do usuário
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expire, "sub": str(subject)}
    # Incluir dados extras no token
    to_encode.update(extra_data)
    
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """
    Valida o token JWT e retorna o usuário atual
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        
        # Verificar se o token já expirou
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expirado",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Extrair dados do usuário do token
    user_data = {
        "username": token_data.sub,
        "email": payload.get("email"),
        "name": payload.get("name"),
        "role": payload.get("role"),
    }
    
    return User(**user_data)
