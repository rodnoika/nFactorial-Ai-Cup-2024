import React from 'react';
import './Css_files/Header.css'

const Header = () => (
  <header className="header">
    <div className="header-logo">Board Games</div>
    <nav className="header-nav">
      <a href="#">Home</a>
      <a href="#">Categories</a>
      <a href="#">Games</a>
      <a href="#">Shop Now</a>
    </nav>
    <div className="header-auth">
      <button className="log-in">Log in</button>
      <button className="sign-up">Sign up</button>
    </div>
  </header>
);

export default Header;
