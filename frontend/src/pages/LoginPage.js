// src/pages/LoginPage.js
import React from 'react';
import { Navigate, Link } from 'react-router-dom';
import { initiateLogin } from '../services/api';
import { useAuth } from '../hooks/useAuth';
import '../styles/login.css';

const LoginPage = () => {
  const { isAuthenticated } = useAuth();

  // Se já estiver autenticado, redirecione para o dashboard
  if (isAuthenticated) {
    return <Navigate to="/dashboard" />;
  }

  const handleLogin = () => {
    initiateLogin();
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <h1>Login IBMEC</h1>
        <p>Faça login com sua conta institucional do IBMEC</p>
        <button className="login-button" onClick={handleLogin}>
          <svg className="ms-logo" viewBox="0 0 23 23" xmlns="http://www.w3.org/2000/svg">
            <path fill="#f25022" d="M1 1h10v10H1z" />
            <path fill="#00a4ef" d="M1 12h10v10H1z" />
            <path fill="#7fba00" d="M12 1h10v10H12z" />
            <path fill="#ffb900" d="M12 12h10v10H12z" />
          </svg>
          Entrar com Microsoft
        </button>
        
        {/* Botão para voltar à página inicial */}
        <div className="back-to-home">
          <Link to="/" className="back-link">
            ← Voltar para a página inicial
          </Link>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
