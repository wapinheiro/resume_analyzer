import React, { useState } from 'react';

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
    <div style={{ maxWidth: 600, margin: '2rem auto', padding: '2rem', border: '1px solid #ddd', borderRadius: 8 }}>
      <h2>Resume Analyzer</h2>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '1rem' }}>
          <label>Resume Text:</label><br />
          <textarea value={resumeText} onChange={e => setResumeText(e.target.value)} rows={6} style={{ width: '100%' }} required />
        </div>
        <div style={{ marginBottom: '1rem' }}>
          <label>Job Description (optional):</label><br />
          <textarea value={jobDescription} onChange={e => setJobDescription(e.target.value)} rows={4} style={{ width: '100%' }} />
        </div>
        <button type="submit" disabled={loading} style={{ padding: '0.5rem 1.5rem' }}>
          {loading ? 'Analyzing...' : 'Analyze'}
        </button>
      </form>
      {error && <div style={{ color: 'red', marginTop: '1rem' }}>{error}</div>}
      {results && (
        <div style={{ marginTop: '2rem' }}>
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
