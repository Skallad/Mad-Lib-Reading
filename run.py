# Modules for different functions, getting template, styling output.
import json
import os
from art import tprint
from rich import print


play = True

while play:
    """
    Title followed by user input prompt and y/n question in end
    which throws user back to beginning or ends game.
    """
    tprint("Mad Lib Reading", font="5lineoblique", chr_ignore=True)

    class MadLibReader:
        path = "templates/"

        def __init__(self, word_inputs, template):
            self.template = template
            self.word_inputs = word_inputs
            self.user_input = []
            self.poem = None

        @classmethod
        def get_template(cls, name, path=None):
            if not path:
                path = cls.path
            fpath = os.path.join(path, name)
            with open(fpath, "r") as f:
                data = json.load(f)
            mad_lib = cls(**data)
            return mad_lib

        # word prompts
        def get_user_input(self):
            print("""
            Hello and welcome to Mad Lib Reading, where you will be
            prompted to enter words that match the description.
            The end result will be a poem and hopefully you will enjoy!

            Maybe with a laugh or two to accompany you ;)

            Please enter an appropriate word
            then [b green]enter[/b green].
            """)
            for desc in self.word_inputs:
                ui = input(desc + ": \n")
                self.user_input.append(ui)
            return self.user_input

        def assemble_poem(self):
            self.poem = self.template.format(*self.user_input)
            return self.poem

        def show_poem(self):
            print(poem)

    template_name = "poem_template.json"
    mad_lib = MadLibReader.get_template(template_name)
    words = mad_lib.get_user_input()
    poem = mad_lib.assemble_poem()
    mad_lib.show_poem()

    # Question if want to play again
    again = input("\nDo you want to play again? Y or N:\n")
    if again == "N":
        play = False
    else:
        play = True
