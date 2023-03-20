from tkinter import *
import random

class Bird:
    """Create a bird for user to control"""

    time_step = 0.01  # Time step in seconds
    gravity_pull = 1900.81  # Gravitational acceleration in m/s^2

    def __init__(self, master, v_init, y_init, size, canvas):
        self.master = master
        self.canvas = canvas
        self.v_init = v_init
        self.y_init = y_init
        self.size = size
        self.alive = True

        self.bird = self.canvas.create_rectangle(200 - self.size / 2,
                                                   720 - self.y_init - self.size / 2,
                                                   200 + self.size / 2,
                                                   720 - self.y_init + self.size / 2,
                                                    fill='red')

        # Bind the space key to jump
        self.master.bind_all("<space>", self.bird_jump)

    def bird_jump(self, event):

        # Reset the initial velocity going up each space press
        self.v_init = 500

        while self.y_init > 0 and self.alive:
            self.y_init = self.y_init + self.v_init * self.time_step
            self.v_init = self.v_init - self.gravity_pull * self.time_step

            if self.y_init < self.size:
                self.y_init = self.size

            if self.y_init > 720 - self.size:
                self.y_init = 720 - self.size
                self.v_init = 0

            self.canvas.coords(self.bird, 200 - self.size / 2,
                               720 - self.y_init - self.size / 2,
                               200 + self.size / 2, 720 - self.y_init + self.size / 2)

            self.master.update()

            self.canvas.after(10)

    def reset(self):
        """Reset the bird to its original position"""
        pass


class Pipes:
    def __init__(self, distance):
        pass



class Score:
    def __init__(self):
        pass


class Game:
    SCREEN_HEIGHT = 720
    SCREEN_WIDTH = 1280

    def __init__(self):
        self.main_window = Tk()
        self.main_window.title('Flappy Bird')

        self.canvas = Canvas(self.main_window, width=Game.SCREEN_WIDTH, height=Game.SCREEN_HEIGHT)
        self.canvas.pack()

        # Initialise the Jump function
        self.bird = Bird(self.main_window, canvas=self.canvas, v_init=500, y_init=360, size=20)

    def start(self):
        while True:
            self.main_window.update_idletasks()
            self.main_window.update()


if __name__ == "__main__":
    game = Game()
    game.start()
