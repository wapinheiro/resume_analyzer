
import React, { useState } from 'react';
import './ResumeAnalyzer.css';

function ResumeAnalyzer() {
  const [resumeText, setResumeText] = useState('');
  const [resumeFile, setResumeFile] = useState(null);
  const [jobDescription, setJobDescription] = useState('');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);


  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResults(null);

    // Prepare form data for file upload or text
    const formData = new FormData();
    if (resumeFile) {
      formData.append('resume_file', resumeFile);
    } else {
      formData.append('resume_text', resumeText);
    }
    formData.append('job_description', jobDescription);

    try {
      const response = await fetch('http://localhost:8000/v1/analyze', {
        method: 'POST',
        body: formData
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


  // No longer needed: all file parsing is handled by the backend

  return (
    <div className="analyzer-container">
      <h2>Resume Analyzer</h2>
      <p className="analyzer-instructions">Paste your resume and (optionally) a job description below. Click Analyze to see agent results.</p>
      <form onSubmit={handleSubmit} className="analyzer-form">
        <label>Resume File (PDF, TXT, DOCX):</label>
        <input
          type="file"
          accept=".pdf,.txt,.doc,.docx"
          onChange={e => setResumeFile(e.target.files[0])}
        />
        <label>Or Paste Resume Text:</label>
        <textarea
          value={resumeText}
          onChange={e => setResumeText(e.target.value)}
          rows={6}
          disabled={!!resumeFile}
          required={!resumeFile}
        />
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
          {/* Overall Score/Feedback Card */}
          {results.overall && (
            <div className="agent-card overall-card">
              <div className="agent-header">
                <span className="agent-title">OVERALL</span>
              </div>
              <ul className="agent-details">
                {typeof results.overall.score !== 'undefined' && (
                  <li>
                    <strong>Score:</strong> {results.overall.score}/10 {' '}
                    <em>({(() => {
                      const s = results.overall.score;
                      if (s <= 2) return 'Poor/Missing';
                      if (s <= 5) return 'Needs Improvement';
                      if (s <= 7) return 'Good';
                      if (s <= 9) return 'Excellent';
                      return 'Outstanding';
                    })()})</em>
                  </li>
                )}
                {results.overall.feedback && (
                  <li>
                    <strong>Feedback:</strong>
                    <div>{results.overall.feedback}</div>
                  </li>
                )}
              </ul>
            </div>
          )}
          <div className="agent-cards">
            {Object.entries(results)
              .filter(([agent]) => agent !== 'overall')
              .map(([agent, status]) => (
                <div className={`agent-card agent-card-${agent}`} key={agent}>
                  <div className="agent-header">
                    <span className="agent-title">{agent.replace(/_/g, ' ').toUpperCase()}</span>
                  </div>
                  {status && typeof status === 'object' ? (
                    <ul className="agent-details">
                      {typeof status.score !== 'undefined' && (
                        <li>
                          <strong>Score:</strong> {status.score}/10 {' '}
                          <em>({(() => {
                            const s = status.score;
                            if (s <= 2) return 'Poor/Missing';
                            if (s <= 5) return 'Needs Improvement';
                            if (s <= 7) return 'Good';
                            if (s <= 9) return 'Excellent';
                            return 'Outstanding';
                          })()})</em>
                        </li>
                      )}
                      {typeof status.confidence !== 'undefined' && (
                        <li>
                          <strong>Confidence:</strong> {Math.round(status.confidence * 100)}% {' '}
                          <em>({(() => {
                            const c = status.confidence;
                            if (c <= 0.5) return 'Low Confidence';
                            if (c <= 0.8) return 'Moderate Confidence';
                            return 'High Confidence';
                          })()})</em>
                        </li>
                      )}
                      {status.feedback && (
                        <li>
                          <strong>Feedback:</strong>
                          {Array.isArray(status.feedback)
                            ? status.feedback.map((f, i) => <div key={i}>{f}</div>)
                            : <div>{status.feedback}</div>}
                        </li>
                      )}
                      {status.suggestions && (
                        <li>
                          <strong>Suggestions:</strong>
                          {Array.isArray(status.suggestions)
                            ? status.suggestions.map((s, i) => <div key={i}>{s}</div>)
                            : <div>{status.suggestions}</div>}
                        </li>
                      )}
                    </ul>
                  ) : (
                    <div className="agent-status">{String(status)}</div>
                  )}
                </div>
              ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default ResumeAnalyzer;
