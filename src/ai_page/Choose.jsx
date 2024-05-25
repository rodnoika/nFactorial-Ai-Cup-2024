import React from 'react';
import './Css_files/Choose.css';

const GenMode = ({ image, title, description }) => (
    <div className="card">
      <img src={image} alt={title} className="card-image" />
      <div className="card-content">
        <h3 className="card-title">{title}</h3>
        <p className="card-description">{description}</p>
        <button className="card-button">View</button>
      </div>
    </div>
  );

const games = [
    {
      image: 'path/to/chess.jpg',
      title: 'Генерация персонажа',
      description: 'Опиши своего персонажа и мы сгенерируем!'
    },
    {
      image: 'path/to/risk.jpg',
      title: 'Генерация карточки для игры',
      description: 'Опиши карточку своего персонажа или действия и мы сгенерируем!'
    },
    {
      image: 'path/to/ticket-to-ride.jpg',
      title: 'Генерация правил для игры',
      description: 'Опиши свою игру и мы сгенерируем правила!'
    },
    {
      image: 'path/to/catan.jpg',
      title: 'Генерация историй',
      description: 'Опиши ситуацию в игре мы сгенерируем историю и сюжет!'
    },
    {
      image: 'path/to/catan.jpg',
      title: 'Генерация названия игры/имени персонажа',
      description: 'Опиши своего персонажа или игру и мы сгенерируем название'
    },
    {
      image: 'path/to/monopoly.jpg',
      title: 'Генеральная генерация',
      description: 'Опиши свою игру и мы все подготовим!'
    }
  ];
  
const Choose = () => (
    <div className="app">
      <div className="game-grid">
        {games.map((game, index) => (
          <GenMode
            key={index}
            image={game.image}
            title={game.title}
            description={game.description}
          />
        ))}
      </div>
    </div>
  );
  
export default Choose;