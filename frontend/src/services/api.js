// src/services/api.js
import { API_URL } from '../utils/constants';

export const initiateLogin = () => {
  window.location.href = `${API_URL}/auth/login`;
};

export const fetchUserData = async (token) => {
  try {
    const response = await fetch(`${API_URL}/auth/me`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    
    if (!response.ok) {
      throw new Error('Failed to fetch user data');
    }
    
    return await response.json();
  } catch (error) {
    console.error('API error:', error);
    throw error;
  }
};
