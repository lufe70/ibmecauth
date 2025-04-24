// src/pages/AuthCallback.js
import React, { useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import '../styles/components.css';

const AuthCallback = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { login } = useAuth();
  
  useEffect(() => {
    const processAuth = async () => {
      const urlParams = new URLSearchParams(location.search);
      const token = urlParams.get('token');
      
      if (token) {
        try {
          await login(token);
          navigate('/dashboard');
        } catch (error) {
          console.error('Authentication error:', error);
          navigate('/login');
        }
      } else {
        navigate('/login');
      }
    };
    
    processAuth();
  }, [location, navigate, login]);
  
  return (
    <div className="auth-callback">
      <div className="loading-indicator"></div>
      <p>Processando autenticação...</p>
    </div>
  );
};

export default AuthCallback;
