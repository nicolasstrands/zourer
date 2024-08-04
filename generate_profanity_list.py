import json

def generate_profanity_list():
    with open('src/defintions.json', 'r') as f:
        profanity_defs = json.load(f)

    profanity_list = list(profanity_defs.keys())

    with open('data/list.json', 'w') as f:
        json.dump(profanity_list, f, indent=2)

if __name__ == "__main__":
    generate_profanity_list()