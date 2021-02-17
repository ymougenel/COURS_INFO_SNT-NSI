from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
import pygame

from bricks.constants import *


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.speed = BALL_DEFAULT_SPEED
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.vx = 1
        self.vy = 1
        self.size = BALL_DEFAULT_SIZE
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill(PADDLE_COLOR)
        # self.rect = self.surf.get_rect()
        # self.rect.move_ip(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 7)

    def move(self, pressed_keys):
        self.y += self.vy

        if self.y < 0 or self.y > SCREEN_HEIGHT:
            self.vy *= -1
        # TODO lose detection

    def display(self, screen: pygame.Surface):
        pygame.draw.circle(screen, BALL_COLOR, (self.x, self.y), BALL_DEFAULT_SIZE)
