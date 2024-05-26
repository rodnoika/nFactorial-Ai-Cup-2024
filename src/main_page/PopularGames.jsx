import React from 'react';
import './Css_files/PopularGames.css';

const games = [
  { title: '3 Exciting Game', description: 'Alice, Bob, Carol', image: '  src/main_page/assets/0.jpg' },
  { title: 'Game Night Fun', description: 'Game Night Headquarters', image: 'src/main_page/assets/1.jpg' },
  { title: 'All About Strategy', description: 'Fun-filled Game Nights', image: 'src/main_page/assets/6.jpg' },
  { title: 'Laugh and play', description: 'Strategic Gameplay', image: 'src/main_page/assets/7.jpeg' },
  { title: 'It’s Game Time!', description: 'Board Game Expert, PhD', image: 'src/main_page/assets/01.jpg' },
];

const PopularGames = () => (
  <section className="popular-games">
    <h2>Discover our generated Board Games</h2>
    <div className="games-list">    
      {games.map((game, index) => (
        <div key={index} className="game-card">
          <img src={game.image} alt={game.title} />
          <h3>{game.title}</h3>
          <p>{game.description}</p>
        </div>
      ))}
    </div>
  </section>
);

export default PopularGames;
