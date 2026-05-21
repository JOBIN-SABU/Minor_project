import React, { useState } from 'react';
import './Home.css';

/**
 * Home Page Component
 * Main page with the carbon footprint estimator form and results display
 */
function Home() {
  // State management for form inputs
  const [language, setLanguage] = useState('Python');
  const [memoryMb, setMemoryMb] = useState(100);
  const [inputSize, setInputSize] = useState(10);
  const [code, setCode] = useState('');
  
  // State for API response and loading
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [apiUrl, setApiUrl] = useState('http://127.0.0.1:8000/predict');

  // Available programming languages
  const languages = ['Python', 'C', 'C++', 'Java'];

  /**
   * Handle prediction button click
   * Validates input and makes API request to backend
   */
  const handlePredict = async () => {
    // Validate code input
    if (!code.trim()) {
      setError('Please paste your code');
      return;
    }

    // Set loading state and clear previous errors
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      // Prepare request payload
      const payload = {
        code,
        language,
        memory_mb: memoryMb,
        variables: {
          n: inputSize,
        },
      };

      // Make API request to backend
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      // Handle error response
      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Backend Error: ${errorText}`);
      }

      // Parse and store result
      const data = await response.json();
      setResult(data);
    } catch (err) {
      // Set error message
      setError(err.message || 'Could not connect to backend');
    } finally {
      // Stop loading
      setLoading(false);
    }
  };

  /**
   * Reset form to initial state
   */
  const handleReset = () => {
    setLanguage('Python');
    setMemoryMb(100);
    setInputSize(10);
    setCode('');
    setResult(null);
    setError(null);
  };

  return (
    <div className="home-page">
      <div className="estimator-container">
        {/* Left Column - Input Form */}
        <div className="input-panel">
          {/* API Configuration */}
          <div className="form-section">
            <label htmlFor="api-url" className="section-label">
              Backend API URL
            </label>
            <input
              id="api-url"
              type="text"
              value={apiUrl}
              onChange={(e) => setApiUrl(e.target.value)}
              className="input-field"
              placeholder="http://127.0.0.1:8000/predict"
            />
          </div>

          {/* Programming Language Selection */}
          <div className="form-section">
            <label className="section-label">📝 Programming Language</label>
            <div className="language-buttons">
              {languages.map((lang) => (
                <button
                  key={lang}
                  onClick={() => setLanguage(lang)}
                  className={`lang-button ${language === lang ? 'active' : ''}`}
                >
                  {lang}
                </button>
              ))}
            </div>
          </div>

          {/* Memory Usage Input */}
          <div className="form-section">
            <label htmlFor="memory" className="section-label">
              ⚡ Memory Usage (MB)
            </label>
            <input
              id="memory"
              type="number"
              min="1"
              value={memoryMb}
              onChange={(e) => setMemoryMb(parseFloat(e.target.value) || 1)}
              className="input-field"
            />
            <p className="input-hint">Current: {memoryMb.toFixed(1)} MB</p>
          </div>

          {/* Input Size */}
          <div className="form-section">
            <label htmlFor="input-size" className="section-label">
              ☁️ Input Size (n)
            </label>
            <input
              id="input-size"
              type="number"
              min="1"
              value={inputSize}
              onChange={(e) => setInputSize(parseInt(e.target.value) || 1)}
              className="input-field"
            />
            <p className="input-hint">Current: {inputSize}</p>
          </div>

          {/* Code Input Area */}
          <div className="form-section">
            <label htmlFor="code" className="section-label">
              💻 Source Code
            </label>
            <textarea
              id="code"
              value={code}
              onChange={(e) => setCode(e.target.value)}
              placeholder="Paste your code here..."
              className="code-textarea"
            />
            <p className="input-hint">{code.length} characters</p>
          </div>

          {/* Error Alert */}
          {error && (
            <div className="alert alert-error">
              <span className="alert-icon">⚠️</span>
              <p>{error}</p>
            </div>
          )}

          {/* Action Buttons */}
          <div className="button-group">
            <button
              onClick={handlePredict}
              disabled={loading}
              className={`btn btn-primary ${loading ? 'loading' : ''}`}
            >
              {loading ? '⏳ Analyzing...' : '⚡ Predict Carbon Footprint'}
            </button>
            <button onClick={handleReset} className="btn btn-secondary">
              Reset
            </button>
          </div>
        </div>

        {/* Right Column - Results Panel */}
        <aside className="results-panel">
          {result ? (
            <div className="results-content">
              {/* Success Alert */}
              <div className="alert alert-success">
                <span className="alert-icon">✅</span>
                <p>Prediction Successful</p>
              </div>

              {/* Result Metrics */}
              <div className="metrics-grid">
                {/* Energy Consumption Metric */}
                <div className="metric-card energy-card">
                  <p className="metric-label">Energy Consumption</p>
                  <p className="metric-value">
                    {result.energy_joules?.toFixed(4) || 'N/A'}
                    <span className="metric-unit"> J</span>
                  </p>
                </div>

                {/* Carbon Footprint Metric */}
                <div className="metric-card carbon-card">
                  <p className="metric-label">Carbon Footprint</p>
                  <p className="metric-value">
                    {result.carbon_kg?.toFixed(8) || 'N/A'}
                    <span className="metric-unit"> kg CO₂</span>
                  </p>
                </div>

                {/* Complexity Score Metric */}
                <div className="metric-card complexity-card">
                  <p className="metric-label">Complexity Score</p>
                  <p className="metric-value">
                    {result.complexity_score || 'N/A'}
                  </p>
                </div>

                {/* Nesting Depth Metric */}
                <div className="metric-card nesting-card">
                  <p className="metric-label">Nesting Depth</p>
                  <p className="metric-value">
                    {result.nesting_depth || 'N/A'}
                  </p>
                </div>
              </div>

              {/* Info Card with Tips */}
              <div className="info-card">
                <p className="info-title">💡 Tips for Optimization:</p>
                <ul className="info-list">
                  <li>• Reduce nesting depth for cleaner code</li>
                  <li>• Optimize memory usage</li>
                  <li>• Use efficient algorithms</li>
                  <li>• Monitor CPU usage patterns</li>
                </ul>
              </div>
            </div>
          ) : (
            <div className="empty-state">
              <p className="empty-icon">🌱</p>
              <p className="empty-title">No analysis yet</p>
              <p className="empty-text">
                Fill in your code details and click "Predict Carbon Footprint" to get started
              </p>
            </div>
          )}
        </aside>
      </div>
    </div>
  );
}

export default Home;