// src/components/professor/ProfessorFeatures.js
import React from 'react';
import FeatureCard from '../common/FeatureCard';
import '../../styles/components.css';

const professorFeatures = [
  {
    title: "Gerenciamento de Turmas",
    description: "Acesse as turmas, configure avaliações e monitore o desempenho dos alunos."
  },
  {
    title: "Material Didático",
    description: "Faça upload de materiais para suas disciplinas e organize o conteúdo."
  },
  {
    title: "Calendário Acadêmico",
    description: "Visualize e gerencie datas importantes e horários de aulas."
  }
];

const ProfessorFeatures = () => {
  return (
    <div className="professor-dashboard">
      <h3>Painel de Professor</h3>
      <div className="features-container">
        {professorFeatures.map((feature, index) => (
          <FeatureCard 
            key={index}
            title={feature.title}
            description={feature.description}
          />
        ))}
      </div>
    </div>
  );
};

export default ProfessorFeatures;
