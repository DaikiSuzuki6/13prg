# Import tkinter
from tkinter import *

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
GRAVITY = 0.2  # Adjust this value to change the strength of gravity


# Create Bird
class Bird:
    """Create a bird for user to control"""

    # Height of jump when space is pressed
    JUMP_HEIGHT = 20

    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(150, SCREEN_HEIGHT // 2 - 10, 170, SCREEN_HEIGHT // 2 + 10, fill="red")
        self.velocity = 0
        self.alive = True
        self.coords = self.canvas.coords(self.id)

    def update(self):
        # Update the bird's position based on its velocity
        self.velocity += GRAVITY
        self.canvas.move(self.id, 0, self.velocity)
        self.coords = self.canvas.coords(self.id)

        # Keep the bird from going off the bottom of the screen
        if self.coords[3] >= SCREEN_HEIGHT:
            self.velocity = 0
            self.canvas.move(self.id, 0, SCREEN_HEIGHT - self.coords[3])

    def reset(self):
        """Reset the bird to its original position"""
        pass



class Pipes:
    def __init__(self):
        pass


class Score:
    def __init__(self):
        pass


class Game:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title('Flappy Bird')
        self.canvas = Canvas(self.main_window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.canvas.pack()

        # Create the bird
        self.bird = Bird(self.canvas)

        # Bind the space key to jump
        self.canvas.bind_all('<space>', self.bird_jump)

    def bird_jump(self, event):
        # Make the bird jump when the space key is pressed
        self.bird.velocity = -Bird.JUMP_HEIGHT

    def start(self):
        while True:
            self.bird.update()
            self.main_window.update_idletasks()
            self.main_window.update()


if __name__ == "__main__":
    game = Game()
    game.start()
