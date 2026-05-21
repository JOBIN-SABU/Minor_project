import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Navigation from './components/Navigation';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';
import './App.css';

/**
 * App Component - Main application component
 * Sets up routing and renders Header, Navigation, page content, and Footer
 */
function App() {
  return (
    <Router>
      <div className="app-container">
        {/* Header with title and description */}
        <Header />
        
        {/* Navigation bar with links to different pages */}
        <Navigation />
        
        {/* Main content area - routes to different pages */}
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
          </Routes>
        </main>
        
        {/* Footer section */}
        <Footer />
      </div>
    </Router>
  );
}

export default App;