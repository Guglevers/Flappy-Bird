import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
test_font = pygame.font.Font("assets/Pixeltype.ttf", 50)

#surfaces
sky_surface = pygame.image.load("assets./Sky.png").convert()
ground_surface = pygame.image.load("assets./ground.png").convert()
text_surface = test_font.render("Hello World!!", False, "black")
snail_surface = pygame.image.load("assets./snail./snail1.png").convert_alpha()
snail_x = 800
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (20, 20))
    screen.blit(snail_surface, (snail_x, 265))
    snail_x -= 4
    if snail_x <= -100:
        snail_x = 800
    pygame.display.update() 
    clock.tick(60)
 