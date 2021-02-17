import pygame
import sys

from bricks.components.ball import Ball
from bricks.components.block import Block
from bricks.constants import *

from pygame.locals import (
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


def _process_collition():
    block_collision = pygame.sprite.spritecollideany(ball, blocks)
    if block_collision:
        blocks.remove(block_collision)
        print("Collision")

def _gather_sprites():
    all_sprites = pygame.sprite.Group()
    all_sprites.add(ball)
    all_sprites.add(paddle)
    for b in blocks:
        all_sprites.add(b)
    return all_sprites

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    paddle = Paddle()
    ball = Ball()
    block = Block()

    blocks = pygame.sprite.Group()
    blocks.add(block)
    clock = pygame.time.Clock()

    bricks = [""]
    while bricks:

        # Handle inputs
        _process_quit()
        keyboard_inputs = pygame.key.get_pressed()
        paddle.move(keyboard_inputs)
        ball.move()

        _process_collition()
        # Display elements
        screen.fill(BACKGROUND_COLOR)

        for sprite in _gather_sprites():
            sprite.display(screen)
        # paddle.display(screen)
        # ball.display(screen)
        pygame.display.flip()
        # Ensure framerate
        clock.tick(30)

