import React, { useState, useEffect } from 'react';
import './Css_files/Choose.css';
import { BrowserRouter, Routes, Route, Navigate, Link } from 'react-router-dom';

const GenMode = ({ image, title, description, url, onDelete }) => (
  <div className="card">
    <img src={image} alt={title} className="card-image" />
    <div className="card-content">
      <h3 className="card-title">{title}</h3>
      <p className="card-description">{description}</p>
      <Link to={url}>
        <button className="card-button">View</button>
      </Link>
    </div>
  </div>
);

const Choose = () => {
  const initialGames = [
    {
      image: 'src/ai_page/assets/3.jpg',
      title: 'Генерация персонажа',
      description: 'Опиши своего персонажа и мы сгенерируем!',
      url: '/AI/Character'
    },
    {
      image: 'src/ai_page/assets/2.jpg',
      title: 'Генерация карточки для игры',
      description: 'Опиши карточку своего персонажа или действия и мы сгенерируем!',
      url: '/AI/GameCard'
    },
    {
      image: 'path/to/ticket-to-ride.jpg',
      title: 'Генерация правил для игры',
      description: 'Опиши свою игру и мы сгенерируем правила!',
      url: '/AI/Rules'
    },
    {
      image: 'src/ai_pagea/ssets/5.png',
      title: 'Генерация историй',
      description: 'Опиши ситуацию в игре мы сгенерируем историю и сюжет!',
      url: '/AI/Story'
    },
    {
      image: 'path/to/catan.jpg',
      title: 'Генерация названия игры/имени персонажа',
      description: 'Опиши своего персонажа или игру и мы сгенерируем название',
      url: '/AI/Name'
    },
    {
      image: 'path/to/monopoly.jpg',
      title: 'Генеральная генерация',
      description: 'Опиши свою игру и мы все подготовим!',
      url: '/AI/Game'
    }
  ];

  const [games, setGames] = useState(() => {
    const savedGames = localStorage.getItem('games');
    return savedGames ? JSON.parse(savedGames) : initialGames;
  });

  useEffect(() => {
    localStorage.setItem('games', JSON.stringify(games));
  }, [games]);

  const handleDelete = (index) => {
    const updatedGames = games.filter((_, i) => i !== index);
    setGames(updatedGames);
    localStorage.setItem('games', JSON.stringify(updatedGames));
  };

  const handleReset = () => {
    setGames(initialGames);
    localStorage.setItem('games', JSON.stringify(initialGames));
  };

  return (
    <div className="app">
      <div className='top-left'>
        <Link to='/'> Назад</Link>
      </div>
      <div className="game-grid">
        {games.map((game, index) => (
          <GenMode
            key={index}
            image={game.image}
            title={game.title}
            description={game.description}
            url={game.url}
            onDelete={() => handleDelete(index)}
          />
        ))}
      </div>
    </div>
  );
};

export default Choose;
