import React from 'react';
import './Css_files/Footer.css';

const Footer = () => (
  <footer className="footer">
    <div className="footer-content">
      <div className="footer-section">
        <h4>GameBoardG</h4>
        <div className="social-media">
          <a href="#"><img src="/path/to/instagram.png" alt="Instagram" /></a>
          <a href="#"><img src="/path/to/twitter.png" alt="Twitter" /></a>
          <a href="#"><img src="/path/to/spotify.png" alt="Spotify" /></a>
        </div>
      </div>
      <div className="footer-section">
        <h4>Company</h4>
        <ul>
          <li><a href="#">About Us</a></li>
          <li><a href="#">Careers</a></li>
        </ul>
      </div>
      <div className="footer-section">
        <h4>Community</h4>
        <ul>
          <li><a href="#">For Developers</a></li>
          <li><a href="#">Advertising</a></li>
          <li><a href="#">Vendors</a></li>
          <li><a href="#">Community Board</a></li>
        </ul>
      </div>
      <div className="footer-section">
        <h4>Help</h4>
        <ul>
          <li><a href="#">Customer Support</a></li>
          <li><a href="#">Mobile App</a></li>
        </ul>
      </div>
    </div>
  </footer>
);

export default Footer;
