import pygame
import random

class Pipe:
    def __init__(self):
        self.width = 100
        self.height = random.randint(60, 560)
        self.pipe_2_height = 800
        self.x = 450
        self.y = 0
        self.pipe_2_y = self.height + 250

    def draw(self, screen):
        pygame.draw.rect(screen, "green", (self.x, self.y, self.width, self.height))    
        pygame.draw.rect(screen, "green", (self.x, self.pipe_2_y, self.width, self.pipe_2_height))

    def get_rectangles(self):
        pipe_1 = pygame.Rect((self.x, self.y, self.width, self.height))    
        pipe_2 = pygame.Rect((self.x, self.pipe_2_y, self.width, self.pipe_2_height))

        return (pipe_1, pipe_2)
    
    def move(self):
        self.x -= 2
