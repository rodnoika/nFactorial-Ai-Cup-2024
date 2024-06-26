from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import json
import base64
import requests
import time

ai_app_5 = Flask(__name__)
CORS(ai_app_5)

class GameGeneratorRules:

    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    def generate_game(self, prompt):
        messages = [
            {"role": "system", "content": "Ты генератор справедливых правил(с списком нескольками пунктами) и целей для настольной игры"},
            {"role": "user", "content": prompt}  
        ]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=1000,
            temperature=0.7
        )
        
        return response.choices[0].message['content'].strip()


@ai_app_5.route('/generate_game', methods=['POST'])
def generate_game():
    data = request.json
    prompt = data.get('prompt')
    game_generator = GameGenerator(openai_api_key="")
    game_details = game_generator.generate_game(prompt)
    return jsonify({"game_details": game_details})


if __name__ == '__main__':
    ai_app_5.run(host='0.0.0.0', port=5000)
