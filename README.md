# Autenticação Microsoft IBMEC com Perfis

Projeto para autenticação com contas Microsoft do IBMEC com diferentes perfis (Professor e Aluno).

## Funcionalidades

- Autenticação com contas Microsoft existentes do IBMEC
- Detecção automática de perfil baseada no email:
  - Se o email contiver "professor", o usuário terá perfil de Professor
  - Caso contrário, o usuário terá perfil de Aluno
- Dashboards específicos para cada perfil de usuário
- Interface personalizada de acordo com o perfil

## Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## Configuração Microsoft (Resumo)

1. Registre seu aplicativo no [Portal Azure](https://portal.azure.com)
2. Configure o aplicativo como multilocatário
3. Adicione o URI de redirecionamento: `http://localhost:8000/auth/callback`
4. Adicione as credenciais obtidas ao arquivo `.env` no backend

*Detalhes completos na seção "Passo a Passo para Configurar o Aplicativo no Azure" abaixo*

## Como testar

Para testar a autenticação:

1. Acesse `http://localhost:3000` no navegador
2. Clique no botão "Entrar com Microsoft"
3. Você será redirecionado para a página de login da Microsoft
4. Faça login com sua conta do IBMEC (@ibmec.edu.br)
5. Na primeira vez, a Microsoft pedirá que você autorize o acesso do aplicativo
6. Após a autorização, você será redirecionado de volta para o aplicativo, já autenticado

Para testar os diferentes perfis:
* Use uma conta com "professor" no email para acessar o dashboard de Professor
* Use uma conta sem "professor" no email para acessar o dashboard de Aluno

## Arquitetura do Projeto

### Visão Geral do FrontEnd

A estrutura do projeto frontend separa as responsabilidades em componentes e módulos específicos, melhorando a organização e a manutenção do código.

#### Principais Características

1. **Separação por Responsabilidades**:
   - Componentes para UI
   - Páginas para rotas principais
   - Contextos para gerenciamento de estado
   - Serviços para comunicação com a API
   - Estilos separados por escopo

2. **Gerenciamento de Estado Centralizado**:
   - `AuthContext` gerencia todo o estado de autenticação
   - `useAuth` hook facilita o acesso ao contexto em qualquer componente

3. **Componentes Reutilizáveis**:
   - `FeatureCard` é usado por ambos painéis de Professor e Aluno
   - `Header` é compartilhado por todas as páginas autenticadas

4. **Separação por Perfil**:
   - Componentes específicos para Professor
   - Componentes específicos para Aluno
   - Lógica condicional baseada no perfil do usuário

5. **Constantes Centralizadas**:
   - `ROLES` define os tipos de perfil
   - `COLORS` define as cores para cada perfil (incluindo a mudança para laranja)
   - `API_URL` centraliza a URL da API

#### Fluxo de Autenticação Frontend

O fluxo de autenticação é gerenciado pelo `AuthContext`:

1. Usuário clica em "Entrar com Microsoft" na `LoginPage`
2. O serviço de API redireciona para Microsoft
3. Após autenticação, o callback é processado por `AuthCallback`
4. O token é armazenado e os dados do usuário são carregados
5. O usuário é redirecionado para o `Dashboard`
6. Com base no perfil, são exibidos componentes específicos de Professor ou Aluno

### Visão Geral do Backend

A arquitetura do backend segue princípios de arquitetura limpa e separação de responsabilidades, tornando o código mais modular, testável e fácil de manter.

#### Estrutura e Organização

1. **Separação de Responsabilidades**
   - Cada arquivo tem uma única função bem definida
   - Facilita a manutenção e a legibilidade do código

2. **Modularidade**
   - Módulos independentes que podem ser facilmente substituídos
   - Facilita a expansão futura da aplicação

3. **Testabilidade**
   - Componentes isolados são mais fáceis de testar
   - Facilita a criação de testes unitários e de integração

4. **Escalabilidade**
   - Estrutura preparada para adicionar novos recursos
   - Organização que facilita a divisão de trabalho em equipe

#### Fluxo de Autenticação Backend

1. **Rota de Login** (`api/routes/auth.py`)
   - Inicia o fluxo de autenticação
   - Redireciona para Microsoft Login

2. **Processamento de Callback** (`api/routes/auth.py`)
   - Recebe o código de autorização da Microsoft
   - Passa para o serviço de autenticação

3. **Serviço de Autenticação** (`services/auth_service.py`)
   - Gerencia a lógica de autenticação
   - Utiliza o serviço Microsoft para processar o código

4. **Serviço Microsoft** (`services/microsoft_service.py`)
   - Troca o código por token
   - Obtém informações do usuário
   - Determina o perfil (professor ou aluno)

5. **Geração de Token JWT** (`core/security.py`)
   - Cria um token JWT com informações do usuário
   - Inclui o perfil do usuário no token

6. **Redirecionamento para Frontend**
   - Retorna para o frontend com o token JWT

## Passo a Passo para Configurar o Aplicativo no Azure

Aqui está um guia detalhado para configurar seu aplicativo de autenticação Microsoft no Azure:

### 1. Criar uma Conta no Azure

Se você ainda não tiver uma conta no Azure:
1. Acesse [portal.azure.com](https://portal.azure.com)
2. Clique em "Criar uma conta gratuita"
3. Siga as instruções para criar sua conta (talvez precise fornecer um cartão de crédito, mas não haverá cobrança para o nível gratuito)

### 2. Registrar um Novo Aplicativo

1. Após fazer login no [Portal Azure](https://portal.azure.com), clique no menu ☰ no canto superior esquerdo
2. Busque por "Microsoft Entra ID" (antigo Azure Active Directory) e selecione-o
3. No painel lateral esquerdo, clique em "Registros de aplicativo"
4. Clique no botão "+ Novo registro" no topo da página
5. Preencha os detalhes do aplicativo:
   * **Nome**: "IBMEC Auth" ou outro nome de sua preferência
   * **Tipos de conta com suporte**: Selecione "Contas em qualquer diretório organizacional (Qualquer diretório do Microsoft Entra ID - Multilocatário)"
   * **URI de redirecionamento (opcional)**:
      * Plataforma: Web
      * URL: `http://localhost:8000/auth/callback` (para desenvolvimento)
6. Clique em "Registrar"

### 3. Anotar as Credenciais do Aplicativo

Após o registro, você estará na página de visão geral do aplicativo:

1. Anote o **ID do aplicativo (cliente)** - você precisará dele para o arquivo .env
2. Anote o **ID do diretório (locatário)** - embora usaremos "common" para multilocatário

### 4. Criar um Segredo do Cliente (Client Secret)

1. No menu lateral esquerdo da página do seu aplicativo, clique em "Certificados e segredos"
2. Na seção "Segredos do cliente", clique em "+ Novo segredo do cliente"
3. Adicione uma descrição (ex: "Chave de Desenvolvimento") e escolha um período de validade
4. Clique em "Adicionar"
5. **IMPORTANTE**: Copie o **Valor** do segredo imediatamente. Ele só será exibido uma vez e não poderá ser recuperado depois!

### 5. Configurar Permissões de API

1. No menu lateral esquerdo da página do seu aplicativo, clique em "Permissões de API"
2. Clique em "+ Adicionar uma permissão"
3. Selecione "Microsoft Graph"
4. Selecione "Permissões delegadas"
5. Procure e selecione:
   * User.Read (permite login básico e leitura do perfil do usuário)
   * User.ReadBasic.All (opcional - para obter informações básicas de outros usuários)
6. Clique em "Adicionar permissões"

### 6. Configurar o Arquivo .env no Backend

No diretório "backend" do seu projeto, edite o arquivo `.env` com as seguintes informações:

```
SECRET_KEY=sua-chave-secreta-aqui-pode-ser-qualquer-string-longa
MS_TENANT_ID=common
MS_CLIENT_ID=seu-id-do-aplicativo-que-voce-anotou
MS_CLIENT_SECRET=seu-segredo-do-cliente-que-voce-anotou
MS_REDIRECT_URI=http://localhost:8000/auth/callback
FRONTEND_URL=http://localhost:3000
```

### 7. Para Configurar em Produção

Quando estiver pronto para implantar em produção:

1. Adicione novos URIs de redirecionamento no registro do aplicativo:
   * No registro do aplicativo, vá para "Autenticação"
   * Adicione o novo URI: `https://seu-dominio.com/auth/callback`

2. Atualize o arquivo `.env` em produção:
```
MS_REDIRECT_URI=https://seu-dominio.com/auth/callback
FRONTEND_URL=https://seu-dominio.com
```

3. Configure HTTPS para ambos backend e frontend
4. Considere usar um gerenciador de segredos para armazenar as credenciais em produção