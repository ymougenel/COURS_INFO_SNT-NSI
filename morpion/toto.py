import sys, pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

size = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
ship = [0, 0]
black = 0, 0, 0

surf = pygame.Surface((50, 50))
surf.fill((0, 0, 0))

rect = surf.get_rect()


# Move the sprite based on user keypresses

def update(pressed_keys):
    global rect
    if pressed_keys[K_UP]:
        rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
        rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        rect.move_ip(5, 0)

while 1:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pressedKeys = pygame.key.get_pressed()
    update(pressedKeys)

    screen = pygame.display.set_mode(size)

    # Fill the background with white
    screen.fill((255, 255, 255))

    screen.blit(surf, rect)
    pygame.display.flip()
