import React from 'react';
import './Css_files/Header.css'
import { BrowserRouter, Routes, Route, Navigate, Link } from 'react-router-dom';


const Header = () => (
  <header className="header">
    <div className="header-logo">Board Games</div>
    <nav className="header-nav">
      <a href="#">Home</a>
      <a href="#">Create</a>
    </nav>  
  </header>
);

export default Header;
