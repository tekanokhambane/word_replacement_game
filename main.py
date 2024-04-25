from flask import Flask, render_template, request, jsonify
import json
import random
from typing import List

app = Flask(__name__)

first_letters: List[str] = []
new_words: List[str] = []
word_list = []

with open("words_dictionary.json") as f:
    words_dictionary = json.load(f)
    word_list = list(words_dictionary.keys())


def get_new_word(letter: str, words_list: List[str]):
    words_starting_with_letter = [
        word for word in words_list if word.startswith(letter.lower())
    ]
    if words_starting_with_letter:
        new_word = random.choice(words_starting_with_letter)
        return new_word
    else:
        return None


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process_sentence():
    sentence = request.form["sentence"]
    words = sentence.split()
    first_letters = [word[0] for word in words]
    new_words.clear()
    for letter in first_letters:
        new_word = get_new_word(letter, word_list)
        if new_word:
            new_words.append(new_word)
    return jsonify({"sentence": sentence, "new_sentence": " ".join(new_words)})


if __name__ == "__main__":
    app.run(debug=True)
