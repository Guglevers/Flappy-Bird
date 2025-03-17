import pygame

class Player:
    def __init__(self):
        self.gravity = 0
        self.y = 350
        self.x = 10
        self.size = 50

    def jump(self):
        self.gravity = -13

    def draw(self, screen):
        pygame.draw.rect(screen, "yellow", (self.x, self.y, self.size, self.size))
        pygame.draw.rect(screen, "black", (self.x, self.y, self.size, self.size), 10)

    def apply_gravity(self):
        self.gravity += 0.5
        self.y += self.gravity

    def get_rect(self):
        return pygame.Rect((self.x, self.y, self.size, self.size)) 