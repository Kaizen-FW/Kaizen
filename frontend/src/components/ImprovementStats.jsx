import React, { useState, useEffect } from 'react';
import './ImprovementStats.css';

const ImprovementStats = () => {
  const [suggestions, setSuggestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch improvement suggestions from the backend
  useEffect(() => {
    const fetchSuggestions = async () => {
      try {
        const response = await fetch('/api/improvement-suggestions');
        if (!response.ok) {
          throw new Error('Failed to fetch improvement suggestions');
        }
        const data = await response.json();
        setSuggestions(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchSuggestions();
  }, []);

  if (loading) {
    return <div className="loading">Loading improvement suggestions...</div>;
  }

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  return (
    <div className="improvement-stats">
      <header className="stats-header">
        <h2>Improvement Suggestions</h2>
        <p>Analyze and track improvement suggestions with impact scores and statuses.</p>
      </header>

      <section className="suggestions-list">
        {suggestions.length === 0 ? (
          <p>No improvement suggestions available.</p>
        ) : (
          <table className="suggestions-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Description</th>
                <th>Impact Score</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {suggestions.map((suggestion) => (
                <tr key={suggestion.suggestion_id}>
                  <td>{suggestion.suggestion_id}</td>
                  <td>{suggestion.description}</td>
                  <td>{suggestion.impact_score}</td>
                  <td>
                    <span className={`status ${suggestion.status.toLowerCase()}`}>
                      {suggestion.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </div>
  );
};

export default ImprovementStats;
# Placeholder content for frontend/src/components/ImprovementStats.jsx
