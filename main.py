from flask import Flask, render_template, request
from flask_frozen import Freezer
import random

app = Flask(__name__)
freezer = Freezer(app)

adjectives = ['awesome', 'smart', 'creative', 'talented',
              'amazing', 'cool', 'funny', 'kind', 'charming', 'dazzling']
nouns = ['genius', 'star', 'artist', 'leader', 'superstar',
         'champion', 'hero', 'legend', 'maestro', 'virtuoso']


def generate_phrase(name):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    compliment_formats = [
        f"Hey {name}, you're a {adjective} {noun}!",
        f"{name}, you possess {adjective} {noun} qualities.",
        f"With your {adjective} mind, you're a true {noun}.",
        f"You're a {adjective} {noun} in every way, {name}!",
        f"{name}, you're as {adjective} as a {noun}.",
    ]

    phrase = random.choice(compliment_formats)
    return phrase


@app.route('')
def index():
    return render_template('index.html')


@app.route('', methods=['POST'])
def process_form():
    name = request.form['name']
    phrase = generate_phrase(name)
    return render_template('index.html', phrase=phrase)


if __name__ == '__main__':
    app.run(debug=True)
