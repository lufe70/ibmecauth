// src/pages/HomePage.js
import React from 'react';
import { Link, Navigate } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import '../styles/home.css';

const HomePage = () => {
  const { isAuthenticated } = useAuth();

  // Se já estiver autenticado, redirecione para o dashboard
  if (isAuthenticated) {
    return <Navigate to="/dashboard" />;
  }

  return (
    <div className="home-page">
      <div className="home-container">
        <div className="home-content">
          <h1>Bem-vindo ao Portal IBMEC</h1>
          <p className="home-description">
            Acesse nosso sistema acadêmico para gerenciar suas atividades, 
            conferir notas, calendário acadêmico e muito mais.
          </p>
          
          <div className="features-overview">
            <div className="feature-item">
              <div className="feature-icon">📚</div>
              <h3>Material Didático</h3>
              <p>Acesso às aulas e materiais complementares</p>
            </div>
            
            <div className="feature-item">
              <div className="feature-icon">📅</div>
              <h3>Calendário</h3>
              <p>Acompanhe as datas importantes e aulas</p>
            </div>
            
            <div className="feature-item">
              <div className="feature-icon">📊</div>
              <h3>Desempenho</h3>
              <p>Visualize suas notas e frequência</p>
            </div>
          </div>
          
          <Link to="/login" className="login-link-button">
            Entrar no Portal
          </Link>
          
          <div className="home-footer">
            <p>Use seu e-mail institucional do IBMEC para acessar o sistema</p>
            <p>Suporte: <a href="mailto:suporte@ibmec.edu.br">suporte@ibmec.edu.br</a></p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
