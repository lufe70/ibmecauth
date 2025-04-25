"""
Configurações da aplicação com carregamento de variáveis de ambiente
"""
import os
from typing import Optional
#from pydantic import BaseSettings
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import List   

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,                    
)

class Settings(BaseSettings):
    """Configurações da aplicação carregadas de variáveis de ambiente"""
    
    # Configurações da aplicação
    APP_NAME: str = "IBMEC Auth API"
    API_V1_STR: str = ""#"/api/v1"
    DEBUG: bool = False
    
    # Configuração JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret-key-for-development")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    # Configuração Microsoft OAuth
    MS_TENANT_ID: str = os.getenv("MS_TENANT_ID", "common")
    MS_CLIENT_ID: str = os.getenv("MS_CLIENT_ID", "")
    MS_CLIENT_SECRET: str = os.getenv("MS_CLIENT_SECRET", "")
    MS_REDIRECT_URI: str = os.getenv("MS_REDIRECT_URI", "http://localhost:8000/auth/callback")
    MS_SCOPES: list = ["User.Read"]
    
    # Configuração de CORS
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    CORS_ORIGINS: list = [FRONTEND_URL]
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",          # ignora vars não declaradas (equiv. Extra.ignore)
    )

@lru_cache()
def get_settings() -> Settings:
    """
    Retorna as configurações da aplicação usando cache para melhorar o desempenho
    """
    return Settings()
