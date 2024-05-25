import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import GameGenerator from './ai_page/gen_game.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <GameGenerator />
  </React.StrictMode>,  
)
