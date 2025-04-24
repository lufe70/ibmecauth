// src/components/common/AuthSuccess.js
import React from 'react';
import { useAuth } from '../../hooks/useAuth';
import { ROLES } from '../../utils/constants';
import '../../styles/components.css';

const AuthSuccess = () => {
  const { user } = useAuth();
  
  if (!user) return null;
  
  const isProfessor = user.role === ROLES.PROFESSOR;
  
  return (
    <div className="auth-success">
      <h3>Autenticação Microsoft bem-sucedida!</h3>
      <p>Você está conectado com sua conta IBMEC como {isProfessor ? 'Professor' : 'Aluno'}.</p>
    </div>
  );
};

export default AuthSuccess;
