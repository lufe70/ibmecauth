"""
Esquemas relacionados à autenticação
"""
from typing import Optional
from pydantic import BaseModel

class MicrosoftAuthRequest(BaseModel):
    """Esquema para parâmetros da requisição de autenticação Microsoft"""
    code: Optional[str] = None
    state: Optional[str] = None
    error: Optional[str] = None
    error_description: Optional[str] = None

class MicrosoftTokenResponse(BaseModel):
    """Esquema para resposta da API de token Microsoft"""
    access_token: str
    token_type: str
    expires_in: int
    scope: str
    refresh_token: Optional[str] = None
    id_token: Optional[str] = None

class MicrosoftUserInfo(BaseModel):
    """Esquema para informações do usuário retornadas pela Microsoft Graph API"""
    displayName: Optional[str] = None
    givenName: Optional[str] = None
    surname: Optional[str] = None
    userPrincipalName: str
    id: str
