// scoreCalculator.js

// Definición de áreas y sus pesos
const areas = {
    estrategia: {
      name: "Estrategia y Liderazgo Digital",
      weight: 0.20,
      questions: Array.from({length: 5}, (_, i) => i)
    },
    cultura: {
      name: "Cultura y Habilidades Digitales",
      weight: 0.20,
      questions: Array.from({length: 5}, (_, i) => i + 5)
    },
    procesos: {
      name: "Procesos y Operaciones",
      weight: 0.20,
      questions: Array.from({length: 5}, (_, i) => i + 10)
    },
    tecnologia: {
      name: "Tecnología y Datos",
      weight: 0.20,
      questions: Array.from({length: 5}, (_, i) => i + 15)
    },
    experiencia: {
      name: "Experiencia del Cliente",
      weight: 0.20,
      questions: Array.from({length: 10}, (_, i) => i + 20)
    }
  };
  
  // Calcula la puntuación para un área específica
  const calculateAreaScore = (answers, areaQuestions) => {
    const totalPossible = areaQuestions.length * 4;
    const areaScore = areaQuestions.reduce((total, questionIndex) => {
      const answer = answers[questionIndex];
      return total + (answer && !isNaN(answer) ? parseInt(answer) : 0);
    }, 0);
    
    return {
      rawScore: areaScore,
      percentage: (areaScore / totalPossible) * 100
    };
  };
  
  // Calcula todas las puntuaciones
  const calculateScores = (answers) => {
    const areaScores = {};
    let totalScore = 0;
  
    for (const [areaKey, area] of Object.entries(areas)) {
      const { percentage } = calculateAreaScore(answers, area.questions);
      const weightedScore = percentage * area.weight;
      areaScores[areaKey] = weightedScore;
      totalScore += weightedScore;
    }
  
    return {
      totalScore,
      areaScores,
      maturityLevel: getMaturityLevel(totalScore)
    };
  };
  
  // Determina el nivel de madurez
  const getMaturityLevel = (score) => {
    if (score >= 80) return "Optimizado";
    if (score >= 60) return "Gestionado";
    if (score >= 40) return "Definido";
    if (score >= 20) return "Emergente";
    return "Inicial";
  };
  
  // Prepara los datos para el gráfico de radar
  const getRadarChartData = (areaScores) => {
    return Object.entries(areas).map(([key, area]) => ({
      area: area.name,
      score: areaScores[key] || 0
    }));
  };
  
  export {
    calculateScores,
    getRadarChartData,
    areas
  };