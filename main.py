"""Flappy Bird Game. Press space to jolt up to go through spaces between pipes."""
# Import tkinter
from tkinter import *


# Create Bird
class Bird:
    """Create a bird for user to control"""

    # Height of jump when space is pressed
    JUMP_HEIGHT = 20

    def __init__(self, canvas, height, width, space_key, colour):
        self._space_key = space_key
        self.canvas = canvas
        self._height = height
        self._width = width
        self.colour = "black"

    def reset(self):
        """Reset the bird to its original position"""
        pass


    def update(self):
        #Binding the keys to move into one direction
        pass

class Pipes:
    def __init__(self):
        pass


class Score:
    def __init__(self):
        pass


class Game:
    def __init__(self, screen_height, screen_width):
        self.screen_height = screen_height
        self.screen_width = screen_width
        root = Tk()


if __name__ == "__main__":
    Game(1200, 720)

