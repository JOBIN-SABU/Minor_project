import React from 'react';

/**
 * Header Component
 * Displays the main title and description of the application
 */
function Header() {
  return (
    <header className="header">
      <div className="header-content">
        {/* Application title with emoji */}
        <h1 className="header-title">🌱 Green Code A.I</h1>
        {/* Application description */}
        <p className="header-description">
          Estimate software energy usage and carbon footprint from source code
        </p>
      </div>
    </header>
  );
}

export default Header;