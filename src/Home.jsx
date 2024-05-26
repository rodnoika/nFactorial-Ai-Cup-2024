import React, { useState } from 'react';
import { BrowserRouter, Routes, Route, Navigate, Link } from 'react-router-dom';
import App from './App.jsx';
import Choose from './ai_page/Choose.jsx'
import GameGenerator from './ai_page/gen_game.jsx'
import CharGenerator from './ai_page/gen_character.jsx'
import GameCardGenerator from './ai_page/gen_GameCard.jsx'
import NameGenerator from './ai_page/gen_name.jsx'
import StoryGenerator from './ai_page/gen_stories.jsx'
import RulesGenerator from './ai_page/gen_rules.jsx'
function Home() {
  const [redirect, setRedirect] = useState(false);
  const [redirectPath, setRedirectPath] = useState("/");

  return (
    <BrowserRouter>
      <Routes>
        <Route path='' element={<App />}/>
        <Route path='/AI' element={<Choose />} />
        <Route path='/AI/Character' element={<CharGenerator/>}/>
        <Route path='/AI/Game' element={<GameGenerator/>}/>
        <Route path='/AI/Name' element={<NameGenerator/>}/>
        <Route path='/AI/GameCard' element={<GameCardGenerator/>}/>
        <Route path='/AI/Story' element={<StoryGenerator/>}/>
        <Route path='/AI/Rules' element={<RulesGenerator/>}/>
      </Routes>
    </BrowserRouter>
  );
}
export default Home;