// src/utils/constants.js
export const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const ROLES = {
  PROFESSOR: 'professor',
  ALUNO: 'aluno'
};

export const COLORS = {
  PROFESSOR: {
    PRIMARY: '#2c3e50',
    SECONDARY: '#34495e',
    ACCENT: '#3498db'
  },
  ALUNO: {
    PRIMARY: '#ff9800', // Laranja (substituiu o vermelho #bd2024)
    SECONDARY: '#e65100', // Laranja escuro (substituiu #a11c1f)
    ACCENT: '#ffb74d'
  }
};
