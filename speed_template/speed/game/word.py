from game.actor import Actor
from game.point import Point
import random

class Word(Actor):

    def __init__(self, text):
        super().__init__()
        self.set_text(text)
        x = random.randint(0, 60)
        y = random.randint(0, 40)
        position = Point(x, y)
        self.set_position(position)
        velocity = Point(1, 0)
        self.set_velocity(velocity)