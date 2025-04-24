"""
Funções auxiliares
"""
import re
from datetime import datetime, timezone

def normalize_email(email: str) -> str:
    """Normaliza um endereço de email para comparação"""
    return email.lower().strip()

def is_valid_email(email: str) -> bool:
    """Verifica se um email tem formato válido"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def get_current_timestamp() -> int:
    """Retorna o timestamp atual em UTC"""
    return int(datetime.now(timezone.utc).timestamp())
