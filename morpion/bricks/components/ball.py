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
        self.surf = pygame.image.load("assets/ball.jpeg")
        self.rect = self.surf.get_rect()
        # self.rect.size = (BALL_DEFAULT_SIZE, BALL_DEFAULT_SIZE)
        self.rect.move_ip(SCREEN_WIDTH / 2, 20)
        self.speed = BALL_DEFAULT_SPEED

        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.vx = 0
        self.vy = 1
        self.size = BALL_DEFAULT_SIZE

    def move(self):
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.vy *= -1
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.vx *= -1
        self.rect.move_ip(self.speed * self.vx, self.speed * self.vy)


        # TODO lose detection

    def display(self, screen: pygame.Surface):
        screen.blit(self.surf, self.rect)
