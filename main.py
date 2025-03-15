import pygame
from sys import exit
from tests.teste import draw_line

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
test_font = pygame.font.Font("assets/Pixeltype.ttf", 50)

#surfs
sky_surf = pygame.image.load("assets./Sky.png").convert()
ground_surf = pygame.image.load("assets./ground.png").convert()

text_surf = test_font.render("Hello World!!", False, "black")
text_rect = text_surf.get_rect(center = (400, 20))

snail_surf = pygame.image.load("assets./snail./snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (800, 300))

player_surf = pygame.image.load("assets./player./player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

cursor_surf = pygame.image.load("assets./aim.png").convert_alpha()

while True:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))
    screen.blit(text_surf, text_rect)

    screen.blit(snail_surf, snail_rect)
    snail_rect.left -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(player_surf, player_rect)

    pygame.draw.line(screen, "black", (0, 0), (800, 400), 1)

    draw_line(screen, events)

    pygame.display.update() 
    clock.tick(60)

