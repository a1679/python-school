#Started on 20/02/26 and finished in the afternoon. Made it so there are walls that you can collide with and not go through around the border..

import pygame

pygame.init()

screen = pygame.display.set_mode((950, 600))
background_colour = pygame.color.Color("#624343")

pygame.display.set_caption("Adventure 2600") 


width_character = 20
height_character = 20

rect_1_width = 100
rect_1_height = 50

vel = 3

player = pygame.Rect(0, 0, width_character, height_character)
player.center = screen.get_rect().center

thickness = 40

walls = [

    pygame.Rect(0, 0, 950, thickness),                     # top
    pygame.Rect(0, 600 - thickness, 950, thickness),      # bottom

    pygame.Rect(0, 0, thickness, 600),                    # left
    pygame.Rect(950 - thickness, 0, thickness, 600),      # right

]

#COLORS

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
    







    screen.fill((BLACK))

    pygame.draw.rect(screen, (col), (player))
    for wall in walls:
        pygame.draw.rect(screen,(GREEN), (wall))

    pygame.display.flip()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()