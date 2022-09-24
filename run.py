# Modules for different functions, getting template, styling output.
import json
import os
from art import *
from rich import *


# Mad lib class
class MadLibReader:
    def __init__(self, word_inputs, template):
        self.poem = template
        self.word_inputs = word_inputs

    @classmethod(f)
    def get_template(cls, name, path="templates/"):
    fpath = os.path.join(path, name)
    with open(fpath, "r") as f:
        data = json.load(f)
    mad_lib = cls(**data)
    return mad_lib


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
    poem = template.format(*words)
    return poem


template_name = "poem_template.json"
mad_lib = MadLibReader.get_template(template_name)
words = get_user_input(mad_lib.word_inputs)
poem = assemble_poem(mad_lib.template, words)

print(poem)
