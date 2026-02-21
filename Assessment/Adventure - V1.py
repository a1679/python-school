# made on 20/02/26 in double period on Friday. I made it so there is a square that can move.

import pygame

pygame.init()

screen = pygame.display.set_mode((950, 600))
background_colour = pygame.color.Color("#624343")

pygame.display.set_caption("Adventure 2600") 

x = 200
y = 200

width_character = 20
height_character = 20

vel = 3

running = True
while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 950 - width_character:
        x += vel

    if keys[pygame.K_UP] and y > 0:
        y -= vel

    if keys[pygame.K_DOWN] and y < 600 - height_character:
        y += vel

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), (x, y, width_character, height_character))

    pygame.display.update()

pygame.quit()