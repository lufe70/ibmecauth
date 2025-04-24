# IBMEC Auth Frontend

Frontend para autenticação de usuários IBMEC com Microsoft, separando perfis de professores e alunos.

## Estrutura do Projeto

O projeto está organizado em componentes modulares:

- `components/`: Componentes reutilizáveis
- `pages/`: Páginas principais
- `contexts/`: Gerenciamento de estado global
- `hooks/`: Hooks personalizados
- `services/`: Serviços para API
- `styles/`: Arquivos CSS
- `utils/`: Funções utilitárias e constantes

## Instalação

```bash
npm install
```

## Execução

```bash
npm start
```

## Build

```bash
npm run build
```

## Perfis de Usuário

- **Professor**: Emails contendo "professor"
- **Aluno**: Todos os outros emails

## Fluxo de Navegação

1. Página Inicial -> Login -> Dashboard
2. Dashboard adaptado ao perfil do usuário
