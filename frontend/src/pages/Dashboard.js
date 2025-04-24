// src/pages/Dashboard.js
import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import { ROLES } from '../utils/constants';
import Header from '../components/common/Header';
import ProfessorFeatures from '../components/professor/ProfessorFeatures';
import AlunoFeatures from '../components/aluno/AlunoFeatures';
import AuthSuccess from '../components/common/AuthSuccess';
import '../styles/dashboard.css';

const Dashboard = () => {
  const { user, loading, isAuthenticated } = useAuth();
  
  // Se estiver carregando, mostra indicador de loading
  if (loading) {
    return <div className="loading">Carregando...</div>;
  }
  
  // Se não estiver autenticado, redireciona para login
  if (!isAuthenticated) {
    return <Navigate to="/login" />;
  }
  
  // Determina quais componentes mostrar com base no perfil (role)
  const FeaturesComponent = user.role === ROLES.PROFESSOR
    ? ProfessorFeatures
    : AlunoFeatures;
  
  return (
    <div className="dashboard">
      <Header />
      
      <div className="user-info">
        <h2>Bem-vindo, {user?.name || user?.username}</h2>
        <div className="user-details">
          <p><strong>Email:</strong> {user?.email}</p>
          <p><strong>Nome de usuário:</strong> {user?.username}</p>
          <p><strong>Perfil:</strong> {user?.role === ROLES.PROFESSOR ? 'Professor' : 'Aluno'}</p>
        </div>
      </div>
      
      <FeaturesComponent />
      
      <AuthSuccess />
    </div>
  );
};

export default Dashboard;
