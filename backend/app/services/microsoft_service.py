"""
Serviço para interação com a API Microsoft Graph e autenticação
"""
import urllib.parse
import uuid
from typing import Dict, Optional
import httpx
from fastapi import HTTPException, status

from app.core.config import get_settings
from app.models.schemas.auth import MicrosoftTokenResponse, MicrosoftUserInfo
from app.utils.constants import MicrosoftEndpoints

settings = get_settings()

class MicrosoftService:
    """Serviço para interação com a API Microsoft Graph"""
    
    @staticmethod
    def get_authorization_url() -> Dict[str, str]:
        """
        Gera a URL para redirecionamento à página de autenticação Microsoft
        """
        state = str(uuid.uuid4())
        
        params = {
            "client_id": settings.MS_CLIENT_ID,
            "response_type": "code",
            "redirect_uri": settings.MS_REDIRECT_URI,
            "response_mode": "query",
            "scope": " ".join(settings.MS_SCOPES),
            "state": state
        }
        
        auth_url = f"{MicrosoftEndpoints.get_auth_endpoint(settings.MS_TENANT_ID)}?{urllib.parse.urlencode(params)}"
        return {"authorization_url": auth_url, "state": state}
    
    @staticmethod
    async def exchange_code_for_token(code: str) -> MicrosoftTokenResponse:
        """
        Troca o código de autorização por um token de acesso
        """
        token_data = {
            "client_id": settings.MS_CLIENT_ID,
            "client_secret": settings.MS_CLIENT_SECRET,
            "code": code,
            "redirect_uri": settings.MS_REDIRECT_URI,
            "grant_type": "authorization_code"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                MicrosoftEndpoints.get_token_endpoint(settings.MS_TENANT_ID),
                data=token_data
            )
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Falha ao trocar código por tokens: {response.text}"
                )
            
            return MicrosoftTokenResponse(**response.json())
    
    @staticmethod
    async def get_user_info(access_token: str) -> MicrosoftUserInfo:
        """
        Obtém informações do usuário usando o token de acesso
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(
                MicrosoftEndpoints.get_user_info_endpoint(),
                headers={"Authorization": f"Bearer {access_token}"}
            )
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Falha ao obter informações do usuário"
                )
            
            return MicrosoftUserInfo(**response.json())
    
    @staticmethod
    def determine_user_role(email: str) -> str:
        """
        Determina o perfil do usuário baseado no email
        """
        from app.utils.constants import UserRoles
        
        # Se o email contiver "professor", atribui o perfil de professor
        if "professor" in email.lower():
            return UserRoles.PROFESSOR
        
        # Caso contrário, atribui o perfil de aluno
        return UserRoles.ALUNO
