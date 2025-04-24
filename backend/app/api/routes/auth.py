"""
Rotas de autenticação
"""
from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from fastapi.responses import RedirectResponse, JSONResponse

from app.core.config import get_settings
from app.models.domain.token import Token
from app.models.domain.user import User, UserResponse
from app.models.schemas.auth import MicrosoftAuthRequest
from app.services.auth_service import AuthService
from app.services.microsoft_service import MicrosoftService
from app.api.dependencies import get_current_active_user

settings = get_settings()
router = APIRouter(prefix="/auth", tags=["autenticação"])

@router.get("/login")
async def login():
    """
    Inicia o fluxo de autenticação redirecionando para a página de login Microsoft
    """
    auth_info = MicrosoftService.get_authorization_url()
    return RedirectResponse(auth_info["authorization_url"])

@router.get("/callback")
async def auth_callback(
    request: Request,
    code: str = Query(None),
    state: str = Query(None),
    error: str = Query(None),
    error_description: str = Query(None)
):
    """
    Processa o retorno da autenticação Microsoft
    """
    # Criar objeto de requisição para validação
    auth_request = MicrosoftAuthRequest(
        code=code,
        state=state,
        error=error,
        error_description=error_description
    )
    
    # Verificar se houve erro na autenticação
    if auth_request.error:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error": auth_request.error,
                "error_description": auth_request.error_description or "Falha na autenticação"
            }
        )
    
    # Verificar se o código foi fornecido
    if not auth_request.code:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "Código de autorização não fornecido"}
        )
    
    try:
        # Autenticar com o código fornecido
        auth_result = await AuthService.login_with_microsoft(auth_request.code)
        
        # Redirecionar para o frontend com o token
        redirect_url = f"{settings.FRONTEND_URL}/auth?token={auth_result['token'].access_token}"
        return RedirectResponse(redirect_url)
    
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": f"Falha na autenticação: {str(e)}"}
        )

@router.get("/me", response_model=UserResponse)
async def get_current_user(user: User = Depends(get_current_active_user)):
    """
    Retorna informações do usuário autenticado
    """
    return user
