from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import json
import base64
import requests
import time

ai_app_3 = Flask(__name__)
CORS(ai_app_3)

class GameGeneratorCard:

    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    def generate_game(self, prompt):
        messages = [
            {"role": "system", "content": "Ты генератор понятных описаний карточек из настольных игр, это может быть карточка персонажа, карточка предмета, карточка способности/закллинания или карточка действия, в карточке должно быть написана раса персонажа(если это персонаж), цифра силы и уровень силы карточки"},
            {"role": "user", "content": prompt}  
        ]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=2000,
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

    def generate(self, prompt, model, images=1, width=256, height=256):
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


@ai_app_3.route('/generate_game', methods=['POST'])
def generate_game():
    data = request.json
    prompt = data.get('prompt')
    game_generator = GameGenerator(openai_api_key="")
    game_details = game_generator.generate_game(prompt)
    return jsonify({"game_details": game_details})

@ai_app_3.route('/generate_image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt')
    fusionbrain_api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '7DD5CC138E256C8D3CB7C223EB53D382', 'EBD7F63382235ED0E73644B010ABE3CE')
    data = request.json
    prompt = data.get('prompt')
    model_id = fusionbrain_api.get_model()
    uuid = fusionbrain_api.generate(prompt, model_id)
    if uuid:
        images = fusionbrain_api.check_generation(uuid)
        if images:
            image_data = base64.b64decode(images[0])
            image_base64 = base64.b64encode(image_data).decode('utf-8')  # Encode to base64
            return jsonify({"image_data": image_base64})
    return jsonify({"error": "Failed to generate image"}), 500

if __name__ == '__main__':
    ai_app_3.run(host='0.0.0.0', port=5000)
