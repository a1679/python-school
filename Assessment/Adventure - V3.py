#Started on 21/02/26, Finished 22/02/26 : . Made it so there are holes in different levels and they teleport you to the next level.

import pygame

pygame.init()

screen = pygame.display.set_mode((950, 600))
background_colour = pygame.color.Color("#624343")

pygame.display.set_caption("Adventure 2600") 


width_character = 25
height_character = 25

rect_1_width = 100
rect_1_height = 50

vel = 3

player = pygame.Rect(0, 0, width_character, height_character)
player.center = screen.get_rect().center

thickness = 50

# LEVEL 1
level_1_walls = [

    pygame.Rect(0, 0, 375, thickness),          # top left part
    pygame.Rect(575, 0, 375, thickness),        # top right part

    pygame.Rect(0, 600 - thickness, 950, thickness),    # bottom wall
    pygame.Rect(0, 0, thickness, 600),                    # left wall
    pygame.Rect(950 - thickness, 0, thickness, 600),     # right wall

]

# LEVEL 2
level_2_walls = [

    pygame.Rect(0, 600 - thickness, 375, thickness),      # left of hole
    pygame.Rect(575, 600 - thickness, 375, thickness),    # right of hole
    
    pygame.Rect(0, 0, 950, thickness),# TOP WALL
    pygame.Rect(0, 0, thickness, 600),    # LEFT WALL
    pygame.Rect(950 - thickness, 0, thickness, 600),# RIGHT WALL
    pygame.Rect(200, 200, 550, thickness),# INTERNAL WALL
]

levels = [level_1_walls, level_2_walls]

current_level = 0
walls = levels[current_level]

# COLORS
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.mouse.set_visible(False)

running = True
while running:
    pygame.time.delay(10)

    col = BLUE
    for wall in walls:
        if player.colliderect(wall):
            col = RED

    keys = pygame.key.get_pressed()

    # LEFT
    if keys[pygame.K_LEFT]:
        test_player = player.copy()
        test_player.x -= vel

        if not any(test_player.colliderect(wall) for wall in walls):
            player.x -= vel

    # RIGHT
    if keys[pygame.K_RIGHT]:
        test_player = player.copy()
        test_player.x += vel

        if not any(test_player.colliderect(wall) for wall in walls):
            player.x += vel

    # UP
    if keys[pygame.K_UP]:
        test_player = player.copy()
        test_player.y -= vel

        if not any(test_player.colliderect(wall) for wall in walls):
            player.y -= vel

    # DOWN
    if keys[pygame.K_DOWN]:
        test_player = player.copy()
        test_player.y += vel

        if not any(test_player.colliderect(wall) for wall in walls):
            player.y += vel
    
    # LEVEL TRANSITIONS
    # If player exits through top, bottom, left, or right
    if player.top <= 0:  # top exit
        current_level = (current_level + 1) % len(levels)
        walls = levels[current_level]
        player.bottom = 600 - thickness  # appear at bottom of next level, X stays same

    elif player.bottom >= 600:  # bottom exit
        current_level = (current_level + 1) % len(levels)
        walls = levels[current_level]
        player.top = thickness  # appear at top of next level, X stays same

    elif player.left <= 0:  # left exit
        current_level = (current_level + 1) % len(levels)
        walls = levels[current_level]
        player.right = 950 - thickness  # appear at right of next level, Y stays same

    elif player.right >= 950:  # right exit
        current_level = (current_level + 1) % len(levels)
        walls = levels[current_level]
        player.left = thickness  # appear at left of next level, Y stays same

    screen.fill((BLACK))

    pygame.draw.rect(screen, (col), (player))
    for wall in walls:
        pygame.draw.rect(screen,(GREEN), (wall))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()