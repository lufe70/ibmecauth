"""
Constantes usadas em toda a aplicação
"""

# Roles (perfis de usuário)
class UserRoles:
    """Constantes para os perfis de usuário"""
    PROFESSOR = "professor"
    ALUNO = "aluno"

# Endpoints Microsoft
class MicrosoftEndpoints:
    """URLs de endpoints da Microsoft"""
    AUTHORITY = "https://login.microsoftonline.com"
    GRAPH_API = "https://graph.microsoft.com/v1.0"
    
    @classmethod
    def get_auth_endpoint(cls, tenant_id):
        """Retorna o endpoint de autorização para o tenant especificado"""
        return f"{cls.AUTHORITY}/{tenant_id}/oauth2/v2.0/authorize"
    
    @classmethod
    def get_token_endpoint(cls, tenant_id):
        """Retorna o endpoint de token para o tenant especificado"""
        return f"{cls.AUTHORITY}/{tenant_id}/oauth2/v2.0/token"
    
    @classmethod
    def get_user_info_endpoint(cls):
        """Retorna o endpoint para obter informações do usuário"""
        return f"{cls.GRAPH_API}/me"

# Mensagens de erro
class ErrorMessages:
    """Mensagens de erro comuns"""
    INVALID_CREDENTIALS = "Credenciais inválidas"
    TOKEN_EXPIRED = "Token expirado"
    UNAUTHORIZED = "Não autorizado"
    MICROSOFT_AUTH_FAILED = "Falha na autenticação com Microsoft"
