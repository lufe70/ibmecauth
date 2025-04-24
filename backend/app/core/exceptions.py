"""
Exceções personalizadas da aplicação
"""
from fastapi import HTTPException, status

class AuthError(HTTPException):
    """Erro de autenticação"""
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"}
        )

class ForbiddenError(HTTPException):
    """Erro de autorização"""
    def __init__(self, detail: str = "Acesso negado"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail
        )

class NotFoundError(HTTPException):
    """Erro de recurso não encontrado"""
    def __init__(self, detail: str = "Recurso não encontrado"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )

class BadRequestError(HTTPException):
    """Erro de requisição inválida"""
    def __init__(self, detail: str = "Requisição inválida"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )
