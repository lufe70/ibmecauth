// src/components/aluno/AlunoFeatures.js
import React from 'react';
import FeatureCard from '../common/FeatureCard';
import '../../styles/components.css';

const alunoFeatures = [
  {
    title: "Minhas Disciplinas",
    description: "Acesse suas disciplinas, materiais de aula e atividades."
  },
  {
    title: "Notas e Frequência",
    description: "Consulte seu desempenho acadêmico e presença nas aulas."
  },
  {
    title: "Horários",
    description: "Visualize sua grade horária semanal e calendário de provas."
  }
];

const AlunoFeatures = () => {
  return (
    <div className="aluno-dashboard">
      <h3>Painel de Aluno</h3>
      <div className="features-container">
        {alunoFeatures.map((feature, index) => (
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

export default AlunoFeatures;
