import React from 'react';
import './About.css';

/**
 * About Page Component
 * Displays information about the Green Code A.I project
 */
function About() {
  return (
    <div className="about-page">
      <div className="page-content">
        <h2>About Green Code A.I</h2>
        
        <section className="about-section">
          <h3>🌍 Our Mission</h3>
          <p>
            We are committed to helping developers understand and reduce the environmental impact 
            of their software. Green Code A.I is a tool designed to analyze source code 
            and estimate energy consumption and carbon footprint.
          </p>
        </section>

        <section className="about-section">
          <h3>🔍 How It Works</h3>
          <p>
            Our tool analyzes your code to:
          </p>
          <ul className="about-list">
            <li>📊 Calculate code complexity metrics</li>
            <li>⚡ Estimate energy consumption in Joules</li>
            <li>💨 Convert energy to CO₂ equivalent emissions</li>
            <li>📈 Identify optimization opportunities</li>
          </ul>
        </section>

        <section className="about-section">
          <h3>🎯 Key Features</h3>
          <ul className="about-list">
            <li>Multi-language support (Python, C, C++, Java)</li>
            <li>Real-time code analysis</li>
            <li>Detailed metrics and insights</li>
            <li>Optimization recommendations</li>
            <li>Responsive, user-friendly interface</li>
          </ul>
        </section>

        <section className="about-section">
          <h3>👥 Who Can Benefit?</h3>
          <ul className="about-list">
            <li>Software developers and engineers</li>
            <li>Data scientists and researchers</li>
            <li>DevOps and cloud engineers</li>
            <li>Environmental sustainability teams</li>
            <li>Organizations committed to green computing</li>
          </ul>
        </section>
      </div>
    </div>
  );
}

export default About;