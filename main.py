import pygame
import random
from sys import exit

pygame.init()

WIDTH = 450
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.Font("assets/Pixeltype.ttf", 50)

player_gravity = 0
player_y = 350

pipe_height = random.randrange(60, 560)
pipe_x = 450 
pipe_y = -10

score_value = 0

running = True

while True:

    screen.fill("lightblue")    

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        elif event.type == pygame.KEYDOWN:
            if pygame.K_SPACE:
                player_gravity = -13
        
    if running:


        score_surf = font.render(f"Score: {str(score_value).rjust(5, "0")}", False, "black")
        score_rect = score_surf.get_rect(midleft = (20, 20))

        player = pygame.draw.rect(screen, "yellow", (10, player_y, 50, 50))
        player = pygame.draw.rect(screen, "black", (10, player_y, 50, 50), 10)

        player_gravity += 0.5
        player_y += player_gravity    

        pipe0 = pygame.draw.rect(screen, "green", (pipe_x, pipe_y, 100, pipe_height))    
        pipe1 = pygame.draw.rect(screen, "green", (pipe_x, pipe_height + 250, 100, 800))
        
        pipe2 = pygame.draw.rect(screen, "darkgreen", (pipe_x, pipe_y, 100, pipe_height), 10)    
        pipe3 = pygame.draw.rect(screen, "darkgreen", (pipe_x, pipe_height + 250, 100, 800), 10)

        pipes = [pipe0, pipe1, pipe2, pipe3]

        screen.blit(score_surf, score_rect)

        pipe_x-=2

        if pipe_x == -100:
            pipe_x = 450
            pipe_height = random.randrange(60, 560)
            score_value += 1

        for pipe in pipes:
            if player.colliderect(pipe):
                running = False

        if player.top <= 0 or player.bottom >= 800:
            running = False

    else:
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if fail_rect.collidepoint(event.pos):
                    player_gravity = 0
                    player_y = 350
                    pipe_height = random.randrange(60, 560)
                    pipe_x = 450 
                    pipe_y = -10
                    score_value = 0
                    running = True
        
            if event.type == pygame.KEYDOWN:
                if pygame.K_SPACE:
                    player_gravity = 0
                    player_y = 350
                    pipe_height = random.randrange(60, 560)
                    pipe_x = 450 
                    pipe_y = -10
                    score_value = 0
                    running = True

        fail_surf = font.render("Tentar Novamente", False, "black")
        fail_rect = fail_surf.get_rect(center = (225, 350))
        screen.blit(fail_surf, fail_rect)

        score_surf = font.render(f"Score: {str(score_value).rjust(5, "0")}", False, "black")
        score_rect = score_surf.get_rect(center = (225, 410))
        screen.blit(score_surf, score_rect)

    pygame.display.update()
    clock.tick(60)