from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
ITEMS_FILE = os.path.join(app.root_path, 'items.json')

def read_items():
    with open(ITEMS_FILE, 'r') as file:
        return json.load(file)

def write_items(items):
    with open(ITEMS_FILE, 'w') as file:
        json.dump(items, file, indent=2)

@app.route('/items', methods=['GET'])
def get_items():
    try:
        items = read_items()
        return jsonify(items)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/items', methods=['POST'])
def add_item():
    try:
        new_item = request.json
        items = read_items()
        items.append(new_item)
        write_items(items)
        return jsonify(new_item), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/add_to_json', methods=['POST'])
def add_to_json():
    data = request.json
    try:
        with open('data.json', 'a') as file:
            file.write(json.dumps(data))
            file.write('\n')
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run( debug=True)
