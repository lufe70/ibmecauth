"""
Serviço de autenticação
"""
from datetime import timedelta
from typing import Dict, Any

from app.core.config import get_settings
from app.core.security import create_access_token, get_current_user
from app.models.domain.token import Token
from app.models.domain.user import User
from app.services.microsoft_service import MicrosoftService

settings = get_settings()

class AuthService:
    """Serviço para lógica de autenticação"""
    
    @staticmethod
    async def login_with_microsoft(code: str) -> Dict[str, Any]:
        """
        Realiza login com Microsoft e retorna token e informações do usuário
        """
        # Trocar o código por token Microsoft
        microsoft_token = await MicrosoftService.exchange_code_for_token(code)
        
        # Obter informações do usuário
        user_info = await MicrosoftService.get_user_info(microsoft_token.access_token)
        
        # Extrair dados do usuário
        email = user_info.userPrincipalName
        username = email.split("@")[0] if "@" in email else email
        name = user_info.displayName
        
        # Determinar o perfil do usuário
        role = MicrosoftService.determine_user_role(email)
        
        # Criar token de acesso JWT
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        token = create_access_token(
            subject=username,
            expires_delta=access_token_expires,
            email=email,
            name=name,
            role=role
        )
        
        # Criar usuário
        user = User(
            username=username,
            email=email,
            name=name,
            role=role
        )
        
        return {
            "token": Token(access_token=token, token_type="bearer"),
            "user": user
        }
        
    # Expor a função get_current_user para fácil acesso
    get_current_user = get_current_user
