import json
import random
from typing import List

first_letters: List[str] = []
words: List[str] = []
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
        new_words.append(new_word)
    else:
        return None


def get_sentence():
    sentence = ""
    while sentence.count(" ") < 1:
        print("Please enter a sentence with at least 2 words.")
        sentence = input("Enter a sentence: ")
    words = sentence.split()
    first_letters = [word[0] for word in words]
    for letter in first_letters:
        get_new_word(letter, word_list)
    return sentence


def start_game():
    sentence = get_sentence()
    new_sentence = " ".join(new_words)
    print("Original Sentence:", sentence)
    print("New Sentence:", new_sentence)


if __name__ == "__main__":
    print("Welcome to the word replacement game!")
    print("ctrl + c to exit")
    start_game()
    print("Thanks for playing!")
