import openai
import json
import time
import base64   
import requests

class GameGenerator:

    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    def generate_game(self, prompt):
        messages = [
            {"role": "system", "content": "Ты генератор идей для настольных игр."},
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

    def generate(self, prompt, model, images=1, width=1024, height=1024):
        params = {
            "type": "ANIME",
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
        try:
            response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
            response.raise_for_status()
            data = response.json()
            uuid = data.get('uuid')
            if uuid is None:
                print("UUID not found in response:", data)
            return uuid
        except Exception as e:
            print("Error generating image:", e)
            return None

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)


if __name__ == '__main__':
    openai_api_key = "sk-org-uiupjxtl6nhsahmjscumzjdi-e6xVWysw9O3rAOrTJQwET3BlbkFJg0Xy3rI9eHB7YKDoXGaz"
    fusionbrain_api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '7DD5CC138E256C8D3CB7C223EB53D382', 'EBD7F63382235ED0E73644B010ABE3CE')
    game_generator = GameGenerator(openai_api_key)

    prompt = "Придумай настольную игру, которую можно сыграть в реальном мире с друзьями и близкими людьми с правилами, названием и целью, полностью расписать способности, карточки персонажей и событий"
    game_details = game_generator.generate_game(prompt)
    print("Сгенерированная настольная игра:")
    print(game_details)

    model_id = fusionbrain_api.get_model()
    uuid = fusionbrain_api.generate(game_details, model_id)
    if uuid:
        print("Генерация изображения...")
        images = fusionbrain_api.check_generation(uuid)
        image_data = base64.b64decode(images[0])
        with open("generated_image.jpg", "wb") as file:
            file.write(image_data)
        print("Изображение сохранено.")
    else:
        print("Не удалось сгенерировать изображение.")
