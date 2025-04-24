// src/components/common/FeatureCard.js
import React from 'react';
import '../../styles/components.css';

const FeatureCard = ({ title, description }) => {
  return (
    <div className="feature-card">
      <h4>{title}</h4>
      <p>{description}</p>
    </div>
  );
};

export default FeatureCard;
