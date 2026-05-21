import React, { useState } from 'react';
import './Contact.css';

/**
 * Contact Page Component
 * Displays contact form for user inquiries
 */
function Contact() {
  // State management for form inputs
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: '',
  });

  const [submitted, setSubmitted] = useState(false);

  /**
   * Handle input change
   * Updates form data state as user types
   */
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  /**
   * Handle form submission
   * Validates and processes the contact form
   */
  const handleSubmit = (e) => {
    e.preventDefault();

    // Simple validation
    if (
      !formData.name ||
      !formData.email ||
      !formData.subject ||
      !formData.message
    ) {
      alert('Please fill in all fields');
      return;
    }

    // Here you would typically send the data to a backend service
    console.log('Form submitted:', formData);

    // Show success message
    setSubmitted(true);

    // Reset form
    setFormData({
      name: '',
      email: '',
      subject: '',
      message: '',
    });

    // Hide success message after 3 seconds
    setTimeout(() => {
      setSubmitted(false);
    }, 3000);
  };

  return (
    <div className="contact-page">
      <div className="page-content">
        <h2>Contact Us</h2>
        <p className="contact-intro">
          Have questions or feedback about Green Code A.I? We'd love to hear from you!
        </p>

        {/* Contact Form */}
        <form className="contact-form" onSubmit={handleSubmit}>
          {/* Name Field */}
          <div className="form-group">
            <label htmlFor="name">Name</label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="form-input"
              placeholder="Your name"
              required
            />
          </div>

          {/* Email Field */}
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className="form-input"
              placeholder="your.email@example.com"
              required
            />
          </div>

          {/* Subject Field */}
          <div className="form-group">
            <label htmlFor="subject">Subject</label>
            <input
              type="text"
              id="subject"
              name="subject"
              value={formData.subject}
              onChange={handleChange}
              className="form-input"
              placeholder="What is this about?"
              required
            />
          </div>

          {/* Message Field */}
          <div className="form-group">
            <label htmlFor="message">Message</label>
            <textarea
              id="message"
              name="message"
              value={formData.message}
              onChange={handleChange}
              className="form-textarea"
              placeholder="Your message here..."
              rows="6"
              required
            ></textarea>
          </div>

          {/* Submit Button */}
          <button type="submit" className="btn btn-primary">
            Send Message
          </button>
        </form>

        {/* Success Message */}
        {submitted && (
          <div className="alert alert-success success-message">
            <span className="alert-icon">✅</span>
            <p>Thank you! Your message has been sent successfully.</p>
          </div>
        )}

        {/* Contact Information */}
        <section className="contact-info">
          <h3>Other Ways to Reach Us</h3>
          <div className="info-items">
            <div className="info-item">
              <p className="info-label">📧 Email</p>
              <p className="info-value">info@ecoai.com</p>
            </div>
            <div className="info-item">
              <p className="info-label">🌐 Website</p>
              <p className="info-value">www.ecoai.com</p>
            </div>
            <div className="info-item">
              <p className="info-label">📱 Phone</p>
              <p className="info-value">+1 (555) 123-4567</p>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}

export default Contact;