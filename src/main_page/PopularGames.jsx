import React from 'react';
import './Css_files/PopularGames.css';

const games = [
  { title: '3 Exciting Game', description: 'Alice, Bob, Carol', image: '/path/to/image1.jpg' },
  { title: 'Game Night Fun', description: 'Game Night Headquarters', image: '/path/to/image2.jpg' },
  { title: 'Laugh and Play', description: 'Fun-filled Game Nights', image: '/path/to/image3.jpg' },
  { title: 'All About Strategy', description: 'Strategic Gameplay', image: '/path/to/image4.jpg' },
  { title: 'It’s Game Time!', description: 'Board Game Expert, PhD', image: '/path/to/image5.jpg' },
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
