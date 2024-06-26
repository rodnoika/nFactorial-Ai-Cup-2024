from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import json
import base64
import requests
import time
from AI_Stories import GameGeneratorStories
from AI_GameCard import GameGeneratorCard
from AI_Rules import GameGeneratorRules
from AI_name import GameGeneratorName
from AI_characters import GameGeneratorCharacters

ai_app_2 = Flask(__name__)
CORS(ai_app_2)

class GameGenerator:

    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    def generate_game(self, prompt):
        messages = [
            {"role": "system", "content": "Ты генератор идей для настольных игр, сверх сценарист для интересных сюжетов, лучший описыватель предметов и персонажей, справедливый создатель правил со списокм и цели для игры, генератор историй, характера и силы персонажей и количество персонажей должно быть не меньше четыре"},
            {"role": "user", "content": prompt}  
        ]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=1000,
            temperature=0.7
        )
        
        return response.choices[0].message['content'].strip()

class Text2ImageAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=2, width=512, height=512):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
            "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)


@ai_app_2.route('/generate_game', methods=['POST'])
def generate_game():
    data = request.json
    prompt = data.get('prompt')
    prompt_id = data.get('promptId')
    if(prompt_id == 2):
        game_generator = GameGenerator(openai_api_key="")
    elif(prompt_id == 1):
        game_generator = GameGeneratorCharacters(openai_api_key="")
    elif(prompt_id == 3):
        game_generator = GameGeneratorCard(openai_api_key="")
    elif(prompt_id == 4):
        game_generator = GameGeneratorName(openai_api_key="")
    elif(prompt_id == 5):
        game_generator = GameGeneratorRules(openai_api_key="")
    elif(prompt_id == 6):
        game_generator = GameGeneratorStories(openai_api_key="")
    
    game_details = game_generator.generate_game(prompt)
    return jsonify({"game_details": game_details})

@ai_app_2.route('/generate_image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt')
    fusionbrain_api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '7DD5CC138E256C8D3CB7C223EB53D382', 'EBD7F63382235ED0E73644B010ABE3CE')
    data = request.json
    prompt = data.get('prompt')
    model_id = fusionbrain_api.get_model()
    uuid = fusionbrain_api.generate("logo, {prompt}", model_id)
    if uuid:
        images = fusionbrain_api.check_generation(uuid)
        if images:
            image_data = base64.b64decode(images[0])
            image_base64 = base64.b64encode(image_data).decode('utf-8')  # Encode to base64
            return jsonify({"image_data": image_base64})
    return jsonify({"error": "Failed to generate image"}), 500

if __name__ == '__main__':
    ai_app_2.run(host='0.0.0.0', port=5000)
