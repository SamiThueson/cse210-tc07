from game import constants
from game.word import Word
import random

class Words:
    def __init__(self):
        self.word_list = []

    def get_words(self):
        x = 0
        library = constants.LIBRARY
        while x < 5:
            text = random.choice(library)
            word = Word(text)
            self.word_list.append(word)
            x += 1

        return self.word_list
       
    
    # set word list


