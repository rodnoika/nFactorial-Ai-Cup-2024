import React, { useState } from 'react';
import './Css_files/gen_character.css';
import { BrowserRouter, Routes, Route, Navigate, Link } from 'react-router-dom';


const NameGenerator = () => {
  const [prompt, setPrompt] = useState('');
  const [gameDetails, setGameDetails] = useState('');

    const handleGenerateGame = async () => {
      const response = await fetch('http://localhost:5000/generate_game', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ prompt })
      });
      const data = await response.json();
      setGameDetails(data.game_details);
      // Добавляем сгенерированные данные об игре в JSON файл
      addToJSON({ content: data.game_details });
  };
  const addToJSON = async (data, fileName = 'name.json') => {
    try {
        const response = await fetch('http://localhost:5000/add_to_json', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data, file_name: fileName }) // Передаем данные и имя файла
        });
        if (response.ok) {
            console.log('Data added to JSON file successfully');
        } else {
            console.error('Failed to add data to JSON file');
        }
    } catch (error) {
        console.error('Error adding data to JSON file:', error);
    }
    }; (
    <div className="container">
      <div className='top-left'><Link to = '/AI'> Назад</Link></div>
      <h1>Name Generator</h1>
      <textarea 
        value={prompt} 
        onChange={(e) => setPrompt(e.target.value)} 
        placeholder="Enter your game prompt here" 
        rows="5" 
        cols="50"
      />
      <br />
      <button onClick={handleGenerateGame}>Generate Rules</button>
      <div className="game-details">
        <h2>Generated Game Details:</h2>
        <pre>{gameDetails}</pre>
      </div>
    </div>
  );
};

export default NameGenerator;
