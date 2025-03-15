import pygame

pygame.init()

clock = pygame.time.Clock()

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))


position_1 = ()
position_2 = ()

lines = []

running = True
while running:

    screen.fill("black")

    for line in lines:
        pygame.draw.line(screen, "yellow", line[0], line[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not position_1:
                position_1 = event.pos

            elif not position_2:
                position_2 = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and position_2:
            position_1 = ()
            position_2 = ()

    if position_1 and not position_2: 
        pygame.draw.line(screen, "red", position_1, pygame.mouse.get_pos(), 2)

    elif position_1 and position_2:
        pygame.draw.line(screen, "yellow", position_1, position_2, 6)
        lines.append((position_1, position_2))

    pygame.display.update()
    clock.tick(60)

pygame.quit()