import csv
import openai

coordinates = []


api_key = "your_openai_api_key"
openai.api_key = api_key

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    
    image_url = response['data'][0]['url']
    return image_url

    image_url = generate_image(prompt)
    print("Generated Image URL:", image_url)

with open('coordinates.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row
    for row in csvreader:
        frame_number, body_part, x, y = row
        coordinates.append({
            "Frame": int(frame_number),
            "BodyPart": body_part,
            "X": int(x),
            "Y": int(y)
        })

for coord in coordinates:
    print(coord)

frame_descriptions = {}
for coord in coordinates:
    frame = coord['Frame']
    body_part = coord['BodyPart']
    x = coord['X']
    y = coord['Y']
    
    if frame not in frame_descriptions:
        frame_descriptions[frame] = []
    
    frame_descriptions[frame].append(f"{body_part} at ({x}, {y})")

prompts = []
for frame, descriptions in frame_descriptions.items():
    description = "; ".join(descriptions)
    prompt = f"In frame {frame}, the positions of the body parts are: {description}."
    prompts.append(prompt)

for prompt in prompts:
    print(prompt)
