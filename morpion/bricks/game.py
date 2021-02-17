import pygame
import sys

from bricks.components.ball import Ball
from bricks.constants import *

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from bricks.components.paddle import Paddle


def _process_quit():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
        elif event.type == QUIT:
            sys.exit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    paddle = Paddle()
    ball = Ball()

    bricks = [""]
    while bricks:

        # Handle inputs
        _process_quit()
        keyboard_inputs = pygame.key.get_pressed()
        paddle.move(keyboard_inputs)
        ball.move(keyboard_inputs)

        # Display elements
        screen.fill(BACKGROUND_COLOR)
        paddle.display(screen)
        ball.display(screen)
        pygame.display.flip()
