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
from bricks.events import Events
from bricks.events.Events import BALL_LOST


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.image.load("assets/ball.jpeg")
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        self.speed = BALL_DEFAULT_SPEED

        self.vx = 1
        self.vy = -1
        self.size = BALL_DEFAULT_SIZE

    def move(self):
        if self.rect.bottom - self.surf.get_height() < 0:
            print("Collision bottom")
            self.collide("bot")
        if self.rect.top + self.surf.get_height() > SCREEN_HEIGHT:
            print("Collision top")
            pygame.event.post(pygame.event.Event(BALL_LOST, {}))
            self.collide("top")
        if self.rect.left < 0:
            self.collide("left")

        if self.rect.right > SCREEN_WIDTH:
            self.collide("right")

        #TODO trigo
        self.rect.move_ip(self.speed * self.vx, self.speed * self.vy)

    def collide(self, direction):
        if direction == "top" or direction == "bot":
            self.vy *= -1
        elif direction == "left" or direction == "right":
            self.vx *= -1
        # TODO geometry angle

    def display(self, screen: pygame.Surface):
        screen.blit(self.surf, self.rect)
