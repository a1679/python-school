#Started on 25/02/26, Finished : 25/02/26 . Made it so the second level of the game has a drawbridge that in future will be coded with buttons that you can press to open.

import pygame

pygame.init()

screen = pygame.display.set_mode((950, 600))
background_colour = pygame.color.Color("#624343")

pygame.display.set_caption("Adventure 2600") 


width_character = 35
height_character = 35

rect_1_width = 100
rect_1_height = 50

vel = 3

player = pygame.Rect(0, 0, width_character, height_character)
player.center = screen.get_rect().center

thickness = 50

# DEFINE THESE FIRST
internal_wall_y = 200
hole_width = 250
hole_left = (950 - hole_width) // 2
hole_right = hole_left + hole_width

drawbridge = pygame.Rect(hole_left, internal_wall_y, hole_width, thickness)

# LEVEL 1
level_1_walls = [
    pygame.Rect(0, 0, 375, thickness),
    pygame.Rect(575, 0, 375, thickness),
    pygame.Rect(0, 600 - thickness, 950, thickness),
    pygame.Rect(0, 0, thickness, 600),
    pygame.Rect(950 - thickness, 0, thickness, 600),
]

# LEVEL 2
level_2_walls = [

    # INTERNAL WALL with wider hole
    pygame.Rect(0, internal_wall_y, hole_left, thickness),
    pygame.Rect(hole_right, internal_wall_y, 950 - hole_right, thickness),

    pygame.Rect(hole_left, internal_wall_y, hole_width, thickness),

    # LEFT WALL stops at internal wall
    pygame.Rect(0, internal_wall_y, thickness, 600 - internal_wall_y),

    # RIGHT WALL stops at internal wall
    pygame.Rect(950 - thickness, internal_wall_y, thickness, 600 - internal_wall_y),

    # BOTTOM WALL
    pygame.Rect(0, 600 - thickness, 375, thickness),      # left of hole
    pygame.Rect(575, 600 - thickness, 375, thickness),    # right of hole
]

levels = [level_1_walls, level_2_walls]

current_level = 0
walls = levels[current_level]


# COLORS
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
DARK_GREY = (60, 60, 60)

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
    if keys[pygame.K_a]:
        test_player = player.copy()
        test_player.x -= vel

        if not any(test_player.colliderect(wall) for wall in walls):
            player.x -= vel

    # RIGHT
    if keys[pygame.K_d]:
        test_player = player.copy()
        test_player.x += vel

        if not any(test_player.colliderect(wall) for wall in walls):
            player.x += vel

    # UP
    if keys[pygame.K_w]:
        test_player = player.copy()
        test_player.y -= vel

        if not any(test_player.colliderect(wall) for wall in walls):
            player.y -= vel

    # DOWN
    if keys[pygame.K_s]:
        test_player = player.copy()
        test_player.y += vel

        if not any(test_player.colliderect(wall) for wall in walls):
            player.y += vel
    
    # LEVEL TRANSITIONS
    if player.top <= 0:  # top exit
        current_level = (current_level + 1) % len(levels)
        walls = levels[current_level]
        player.bottom = 600 - thickness  

    elif player.bottom >= 600:  # bottom exit
        current_level = (current_level + 1) % len(levels)
        walls = levels[current_level]
        player.top = thickness  

    elif player.left <= 0:  # left exit
        current_level = (current_level + 1) % len(levels)
        walls = levels[current_level]
        player.right = 950 - thickness  

    elif player.right >= 950:  # right exit
        current_level = (current_level + 1) % len(levels)
        walls = levels[current_level]
        player.left = thickness  

    # Background
    if current_level == 1:
        # water area
        pygame.draw.rect(screen, (0, 120, 255), (0, 0, 950, internal_wall_y))
        pygame.draw.rect(screen, (BLACK), (0, internal_wall_y, 950, 600 - internal_wall_y))
    else:
        screen.fill(BLACK)

    pygame.draw.rect(screen, (col), (player))
    for wall in walls:
        pygame.draw.rect(screen,(GREEN), (wall))
    
    if current_level == 1:
        pygame.draw.rect(screen, DARK_GREY, drawbridge)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()