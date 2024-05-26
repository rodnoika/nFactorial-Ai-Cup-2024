from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from '.src/ai_page/ai/AI_characters.py' import game_app_1
from '.src/ai_page/ai/AI_Game.py' import game_app_2
from '.src/ai_page/ai/AI_GameCard.py' import game_app_3
from '.src/ai_page/ai/AI_name.py' import game_app_4
from '.src/ai_page/ai/AI_Rules.py' import game_app_5
from '.src/ai_page/ai/AI_Stories.py' import game_app_6
from './AI_Stories.py' import app

application = DispatcherMiddleware(app, {
    '/Ai1': game_app_1,
    '/Ai2': game_app_2,
    '/Ai3': game_app_3,
    '/Ai4': game_app_4,
    '/Ai5': game_app_5,
    '/Ai6': game_app_6  
})

if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)
