from pygame.locals import (
    K_LEFT,
    K_RIGHT,
)
import pygame

from bricks.constants import *


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super(Paddle, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill(PADDLE_COLOR)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 7)

    def move(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-PADDLE_SPEED, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(PADDLE_SPEED, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def display(self, screen: pygame.Surface):
        screen.blit(self.surf, self.rect)
