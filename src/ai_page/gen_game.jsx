// GameGenerator.jsx
import React, { useState } from 'react';
import './Css_files/gen_GameCard.css';
import { BrowserRouter, Routes, Route, Navigate, Link } from 'react-router-dom';


const GameGenerator = () => {
  const [prompt, setPrompt] = useState('');
  const [gameDetails, setGameDetails] = useState('');
  const [imageData, setImageData] = useState('');

  const handleGenerateGame = async (prompt) => {
    const promptId = 2; // Устанавливаем значение promptId равным 1
    const response = await fetch('http://46.101.221.73generate_game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt, promptId })
    });
    const data = await response.json();
    if (data.game_details) {
        setGameDetails(data.game_details);
        addToJSON({ promptId, content: data.game_details });
    } else {
        alert('Failed to generate game');
    }
};

const handleGenerateImage = async () => {
    const response = await fetch('http://46.101.221.73:5000/generate_image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt })
    });
    const data = await response.json();
    if (data.image_data) {
        setImageData(`data:image/jpeg;base64,${data.image_data}`);
        // Добавляем сгенерированные данные об изображении в JSON файл
        addToJSON({ image: `data:image/jpeg;base64,${data.image_data}` });
    } else {
        alert('Failed to generate image');
    }
};
const addToJSON = async (data, fileName = 'game.json') => {
  try {
      const response = await fetch('http://46.101.221.73:5000/add_to_json', {
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
};

  return (
    <div className="container">
      <div className='top-left'><Link to = '/AI'> Назад</Link></div>
      <h1>Character Generator</h1>
      <textarea 
        value={prompt} 
        onChange={(e) => setPrompt(e.target.value)} 
        placeholder="Enter your game prompt here" 
        rows="5" 
        cols="50"
      />
      <br />
      <button onClick={handleGenerateGame}>Generate Game</button>
      <button onClick={handleGenerateImage}>Generate Image</button>
      <div className="game-details">
        <h2>Generated Game Details:</h2>
        <pre>{gameDetails}</pre>
      </div>
      <div className="image-container">
        <h2>Generated Image:</h2>
        {imageData && <img src={imageData} alt="Generated" />}
      </div>
    </div>
  );
};

export default GameGenerator;
