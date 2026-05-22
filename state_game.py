import pygame

class GameState:
    def __init__(self):
        self.state = "menu"

    def change_state(self, new_state):
        self.state = new_state

class MainMenu:
    def __init__(self, game):
        self.game = game

    def update(self):
        # Handle menu logic here
        pass

class GameOver:
    def __init__(self, game):
        self.game = game

    def update(self):
        # Habdle game over logic here
        pass
