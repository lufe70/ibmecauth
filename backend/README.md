# IBMEC Auth Backend

Backend para autenticação de usuários IBMEC com Microsoft, utilizando FastAPI.

## Estrutura do Projeto

O projeto está organizado de forma modular:

- `app/`: Código principal da aplicação
  - `core/`: Configurações e funcionalidades centrais
  - `api/`: Definição das rotas da API
  - `services/`: Lógica de negócios
  - `models/`: Modelos de dados
  - `utils/`: Funções utilitárias

## Instalação

1. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scriptsctivate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:

```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

## Execução

```bash
uvicorn app.main:app --reload
```

A API estará disponível em http://localhost:8000

## Documentação

A documentação da API está disponível em:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Perfis de Usuário

O sistema determina automaticamente o perfil do usuário com base no email:

- **Professor**: Emails contendo "professor"
- **Aluno**: Todos os outros emails
