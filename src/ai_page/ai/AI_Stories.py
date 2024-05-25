from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import json
import base64
import requests
import time

app = Flask(__name__)
CORS(app)

class GameGenerator:

    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    def generate_game(self, prompt):
        messages = [
            {"role": "system", "content": "Ты гениальный сценарист, который умеет писать интересные и замечательные сценарий, сюжеты и предысторий игры на любой жанр от фэнтези до детективов"},
            {"role": "user", "content": prompt}  
        ]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=1000,
            temperature=0.7
        )
        
        return response.choices[0].message['content'].strip()


@app.route('/generate_game', methods=['POST'])
def generate_game():
    data = request.json
    prompt = data.get('prompt')
    game_generator = GameGenerator(openai_api_key="sk-org-uiupjxtl6nhsahmjscumzjdi-e6xVWysw9O3rAOrTJQwET3BlbkFJg0Xy3rI9eHB7YKDoXGaz")
    game_details = game_generator.generate_game(prompt)
    return jsonify({"game_details": game_details})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
