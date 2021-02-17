import pygame
from bricks.CollisionHandler import process_collisions
from bricks.boards.BoardLoader import load_board
from bricks.components.ball import Ball
from bricks.components.block import Block
from bricks.constants import *
from bricks.components.paddle import Paddle
from bricks.events.EventHandler import process_events

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
    blocks = load_board("Choungui")
    clock = pygame.time.Clock()

    bricks = [""]
    while bricks:

        # Move ball and paddle
        keyboard_inputs = pygame.key.get_pressed()
        paddle.move(keyboard_inputs)
        ball.move()

        # Process collisions
        process_collisions(ball, paddle, blocks)

        # Handle events
        process_events()

        # Display elements
        screen.fill(BACKGROUND_COLOR)
        for sprite in _gather_sprites():
            sprite.display(screen)
        pygame.display.flip()
        # Ensure framerate
        clock.tick(30)
