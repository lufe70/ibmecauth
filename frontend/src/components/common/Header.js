// src/components/common/Header.js
import React from 'react';
import { useAuth } from '../../hooks/useAuth';
import { ROLES } from '../../utils/constants';
import '../../styles/components.css';

const Header = () => {
  const { user, logout } = useAuth();
  
  if (!user) return null;
  
  const isProfessor = user.role === ROLES.PROFESSOR;
  const headerClass = isProfessor ? 'header-professor' : 'header-aluno';
  
  return (
    <header className={headerClass}>
      <h1>Dashboard IBMEC - {isProfessor ? 'Professor' : 'Aluno'}</h1>
      <button className="logout-button" onClick={logout}>Sair</button>
    </header>
  );
};

export default Header;
