import pygame
from sys import exit
from tests.teste import draw_line

pygame.init()

game_active = True

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
font = pygame.font.Font("assets/Pixeltype.ttf", 50)

#surfs
sky_surf = pygame.image.load("assets./Sky.png").convert()
ground_surf = pygame.image.load("assets./ground.png").convert()
ground_rect = ground_surf.get_rect(topleft = (0, 300))

score_surf = font.render("Hello World!!", False, "black")
score_rect = score_surf.get_rect(center = (400, 20))

fail_surf = font.render("Tente Novamente", False, "black")
fail_rect = fail_surf.get_rect(center = (400, 200))

snail_surf = pygame.image.load("assets./snail./snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (800, 300))

player_surf = pygame.image.load("assets./player./player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

cursor_surf = pygame.image.load("assets./aim.png").convert_alpha()

while True:

    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and player_rect.bottom == 300:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

        elif event.type == pygame.MOUSEBUTTONDOWN:
           if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
               player_gravity = -20

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, ground_rect)
        screen.blit(score_surf, score_rect)

        screen.blit(snail_surf, snail_rect)
        snail_rect.left -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800

        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        
        screen.blit(player_surf, player_rect)

        if snail_rect.colliderect(player_rect):
            game_active = False

    else: 
        screen.fill("black")

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if fail_rect.collidepoint(event.pos):
                    player_rect.midbottom = (80, 300)
                    player_gravity = 0
                    snail_rect.left = 800
                    game_active = True

        pygame.draw.rect(screen, "white", fail_rect)
        pygame.draw.rect(screen, "white", fail_rect, 10)
        screen.blit(fail_surf, fail_rect)

        draw_line(screen, events)
        
    pygame.display.update() 
    clock.tick(60)

