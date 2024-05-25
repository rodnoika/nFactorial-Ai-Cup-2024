import React from 'react';
import './Css_files/GameCategories.css';

const categories = [
  'Strategy', 'Family', 'Adventure', 'Mystery', 'Party', 'Educational', 'Fantasy',
  'Cooperative', 'Card', 'Dice', 'Classic', 'Role-playing', 'Trivia', 'Puzzle', 'Euro-style',
  'Social deduction', 'Deck-building'
];

const GameCategories = () => (
  <section className="game-categories">
    <h2>Game Categories</h2>
    <div className="categories-list">
      {categories.map((category, index) => (
        <span key={index} className="category">{category}</span>
      ))}
    </div>
  </section>
);

export default GameCategories;
