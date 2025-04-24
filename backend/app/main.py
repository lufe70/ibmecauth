"""
Ponto de entrada principal da aplicação FastAPI
"""
from fastapi import FastAPI

from app.api.routes.auth import router as auth_router
from app.core.config import get_settings
from app.middlewares.cors_middleware import setup_cors_middleware

settings = get_settings()

def create_application() -> FastAPI:
    """
    Cria e configura a aplicação FastAPI
    """
    application = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        description="API para autenticação com contas Microsoft do IBMEC com diferentes perfis",
        version="1.0.0"
    )

    # Configurar CORS
    setup_cors_middleware(application)

    # Incluir rotas
    application.include_router(auth_router, prefix=settings.API_V1_STR)

    @application.get("/")
    async def root():
        """
        Rota raiz para verificação de saúde da API
        """
        return {
            "message": "IBMEC Authentication API",
            "status": "online",
            "version": "1.0.0"
        }

    return application

app = create_application()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
