from game.actor import Actor
from game.point import Point
from game import constants

class Buffer(Actor):

    def __init__(self):
        super().__init__()
        self._letters = []
        
        position = Point(0, constants.MAX_Y)
        self.set_position(position)
        


    def get_text(self):
        text = "Buffer: "
        for letter in self._letters:
            text += letter
        return text
        
        

    def add_letter(self,letter):
        self._letters.append(letter)

    def clear_letters(self):
        self._letters.clear()