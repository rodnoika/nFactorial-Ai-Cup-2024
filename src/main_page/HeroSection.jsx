import React from 'react';
import './Css_files/HeroSection.css';

const HeroSection = () => (
  <section className="hero-section">
    <div className="hero-content">
      <h1>Explore and enjoy a variety of board games!</h1>
      <p>Start your gaming journey.</p>
      <button className="start-playing">Start playing</button>
    </div>
    <div className="hero-image">
      <img src="src\main_page\assets\BoardGameIllustration.jpg" alt="Board game illustration" />
    </div>
  </section>
);

export default HeroSection;
