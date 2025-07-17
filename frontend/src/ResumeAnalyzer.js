import React, { useState } from 'react';
import './ResumeAnalyzer.css';

function ResumeAnalyzer() {
  const [resumeText, setResumeText] = useState('');
  const [jobDescription, setJobDescription] = useState('');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResults(null);
    try {
      const response = await fetch('http://localhost:8000/v1/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ resume_text: resumeText, job_description: jobDescription })
      });
      if (!response.ok) throw new Error('API error');
      const data = await response.json();
      setResults(data);
    } catch (err) {
      setError('Failed to analyze resume.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="analyzer-container">
      <h2>Resume Analyzer</h2>
      <p className="analyzer-instructions">Paste your resume and (optionally) a job description below. Click Analyze to see agent results.</p>
      <form onSubmit={handleSubmit} className="analyzer-form">
        <label>Resume Text:</label>
        <textarea value={resumeText} onChange={e => setResumeText(e.target.value)} rows={6} required />
        <label>Job Description (optional):</label>
        <textarea value={jobDescription} onChange={e => setJobDescription(e.target.value)} rows={4} />
        <button type="submit" disabled={loading}>
          {loading ? 'Analyzing...' : 'Analyze'}
        </button>
      </form>
      {error && <div className="analyzer-error">{error}</div>}
      {results && (
        <div className="analyzer-results">
          <h3>Agent Results</h3>
          <ul>
            {Object.entries(results).map(([agent, status]) => (
              <li key={agent}><strong>{agent}:</strong> {status}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default ResumeAnalyzer;
