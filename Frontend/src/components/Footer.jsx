import React from 'react';

/**
 * Footer Component
 * Displays footer information and copyright
 */
function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="footer">
      <div className="footer-content">
        <p>
          🌍 Green Code A.I • Measure, Analyze, and Optimize Your Code's Environmental Impact
        </p>
        <p className="footer-copyright">
          &copy; {currentYear} Green  AI. All rights reserved.
        </p>
      </div>
    </footer>
  );
}

export default Footer;