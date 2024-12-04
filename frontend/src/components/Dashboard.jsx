import React, { useState, useEffect } from 'react';
import './Dashboard.css'; // Import CSS for styling

const Dashboard = () => {
  const [userEngagements, setUserEngagements] = useState([]);
  const [improvementSuggestions, setImprovementSuggestions] = useState([]);
  const [evolutionTasks, setEvolutionTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  // Fetch data from backend API
  useEffect(() => {
    const fetchData = async () => {
      try {
        const [engagementsRes, suggestionsRes, tasksRes] = await Promise.all([
          fetch('/api/user-engagements'),
          fetch('/api/improvement-suggestions'),
          fetch('/api/evolution-tasks'),
        ]);

        setUserEngagements(await engagementsRes.json());
        setImprovementSuggestions(await suggestionsRes.json());
        setEvolutionTasks(await tasksRes.json());
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <div className="loading">Loading dashboard...</div>;
  }

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1>Kaizen Agent Framework Dashboard</h1>
        <p>Track user engagement, improvement suggestions, and evolution tasks in one place.</p>
      </header>

      <section className="dashboard-section">
        <h2>User Engagements</h2>
        <ul>
          {userEngagements.map((engagement) => (
            <li key={engagement.engagement_id}>
              <strong>Activity:</strong> {engagement.activity} | <strong>User:</strong> {engagement.user_id} | <strong>Timestamp:</strong> {engagement.timestamp}
            </li>
          ))}
        </ul>
      </section>

      <section className="dashboard-section">
        <h2>Improvement Suggestions</h2>
        <ul>
          {improvementSuggestions.map((suggestion) => (
            <li key={suggestion.suggestion_id}>
              <strong>Description:</strong> {suggestion.description} | <strong>Impact:</strong> {suggestion.impact_score} | <strong>Status:</strong> {suggestion.status}
            </li>
          ))}
        </ul>
      </section>

      <section className="dashboard-section">
        <h2>Evolution Tasks</h2>
        <ul>
          {evolutionTasks.map((task) => (
            <li key={task.task_id}>
              <strong>Task:</strong> {task.description} | <strong>Status:</strong> {task.status} | <strong>Progress:</strong> {task.progress}%
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
};

export default Dashboard;
# Placeholder content for frontend/src/components/Dashboard.jsx
