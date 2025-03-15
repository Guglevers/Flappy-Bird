import pygame

position_1 = None
position_2 = None

lines = []

def draw_line(screen, events):

    global position_1, position_2, lines

    for line in lines:
        pygame.draw.line(screen, "yellow", line[0], line[1])

    for event in events:

        if event.type == pygame.MOUSEBUTTONDOWN:
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