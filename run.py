# Modules for styling
from art import *
from rich import *


# Mad lib reader template
class MadLibReader:
    def __init__(self, word_inputs, template):
        self.poem = poem
        self.word_inputs = word_inputs


# Welcome message
tprint("")


def get_user_input(word_inputs):
    words = []
    print("Please provide a few words for the text")
    for desc in word_inputs:
        user_input = input(desc + " ")
        words.append(user_input)
    return words


# Build the poem
def assemble_poem(template, words):
    template = "I love you, my {} {}!"
    words = get_user_input(["adjective", "noun"])
    poem = template.format(*words)
    return poem


