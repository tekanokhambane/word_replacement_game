from flask import Flask, render_template, request, jsonify
import json
import random
from typing import List

app = Flask(__name__)

first_letters: List[str] = []
new_words: List[str] = []
word_list = []

with open("words_alpha.txt") as f:
    words_list = f.read().splitlines()
    word_list = list(words_list)


def get_new_word(letter: str, words_list: List[str], old_word: str):
    words_starting_with_letter = [
        word for word in words_list if word.startswith(letter.lower())
    ]
    if words_starting_with_letter:
        same_length_words = [
            word for word in words_starting_with_letter if len(word) == len(old_word)
        ]
        if same_length_words:
            new_word = random.choice(same_length_words)
            return new_word
        else:
            new_word = old_word
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
    first_letters = [word for word in words]
    new_words.clear()
    for word in first_letters:
        new_word = get_new_word(word[0], word_list, word)
        if new_word:
            new_words.append(new_word)
    return jsonify({"sentence": sentence, "new_sentence": " ".join(new_words)})


if __name__ == "__main__":
    app.run(debug=True)
