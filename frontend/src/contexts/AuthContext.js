// src/contexts/AuthContext.js
import React, { createContext, useState, useEffect } from 'react';
import { fetchUserData } from '../services/api';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    // Verificar se o usuário já está autenticado
    const token = localStorage.getItem('auth_token');
    if (token) {
      loadUserData(token);
    } else {
      setLoading(false);
    }
  }, []);

  const loadUserData = async (token) => {
    try {
      const userData = await fetchUserData(token);
      setUser(userData);
      setIsAuthenticated(true);
    } catch (error) {
      console.error('Error loading user data:', error);
      logout();
    } finally {
      setLoading(false);
    }
  };

  const login = async (token) => {
    localStorage.setItem('auth_token', token);
    await loadUserData(token);
    return isAuthenticated;
  };

  const logout = () => {
    localStorage.removeItem('auth_token');
    setUser(null);
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        isAuthenticated,
        login,
        logout
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};
