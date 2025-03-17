import pygame
from sys import exit
from classes.pipe import Pipe
from classes.player import Player

pygame.init()

WIDTH = 450
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.Font("assets/Pixeltype.ttf", 50)

player = Player()
pipe = Pipe()

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
            if event.key == pygame.K_SPACE:
                player.jump()
        
    if running:

        score_surf = font.render(f"Score: {str(score_value).rjust(5, "0")}", False, "black")
        score_rect = score_surf.get_rect(midleft = (20, 20))

        player.draw(screen)

        player.apply_gravity()    

        pipe.draw(screen)

        pipe.move()

        screen.blit(score_surf, score_rect)

        if pipe.x == -100:
            pipe = Pipe()
            score_value += 1

        for pipe_rect in pipe.get_rectangles():
            if player.get_rect().colliderect(pipe_rect):
                running = False

        if player.y <= 0 or player.y >= 800:
            running = False

    else:
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if fail_rect.collidepoint(event.pos):
                    player = Player()
                    pipe = Pipe()
                    score_value = 0
                    running = True
        
            if event.type == pygame.KEYDOWN:
                if pygame.K_SPACE:
                    player = Player()
                    pipe = Pipe() 
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