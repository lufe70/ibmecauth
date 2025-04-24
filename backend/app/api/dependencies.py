"""
Dependências compartilhadas para as rotas da API
"""
from fastapi import Depends, Query, Path

from app.core.security import get_current_user
from app.models.domain.user import User
from app.utils.constants import UserRoles

async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """
    Verifica se o usuário está ativo
    """
    return current_user

async def get_current_professor(current_user: User = Depends(get_current_user)) -> User:
    """
    Verifica se o usuário é um professor
    """
    if current_user.role != UserRoles.PROFESSOR:
        from app.core.exceptions import ForbiddenError
        raise ForbiddenError("Acesso permitido apenas para professores")
    return current_user

async def get_current_aluno(current_user: User = Depends(get_current_user)) -> User:
    """
    Verifica se o usuário é um aluno
    """
    if current_user.role != UserRoles.ALUNO:
        from app.core.exceptions import ForbiddenError
        raise ForbiddenError("Acesso permitido apenas para alunos")
    return current_user
