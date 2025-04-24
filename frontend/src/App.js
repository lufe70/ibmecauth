// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import AuthCallback from './pages/AuthCallback';
import Dashboard from './pages/Dashboard';

const RequireAuth = ({ children }) => {
  // Este componente verifica se o usuário está autenticado
  const isAuthenticated = localStorage.getItem('auth_token') !== null;
  
  if (!isAuthenticated) {
    // Redireciona para a página inicial em vez da página de login
    return <Navigate to="/" />;
  }
  
  return children;
};

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="app">
          <Routes>
            {/* Rota inicial para a HomePage */}
            <Route path="/" element={<HomePage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/auth" element={<AuthCallback />} />
            <Route 
              path="/dashboard" 
              element={
                <RequireAuth>
                  <Dashboard />
                </RequireAuth>
              } 
            />
            {/* Outras rotas redirecionam para a página inicial */}
            <Route path="*" element={<Navigate to="/" />} />
          </Routes>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
