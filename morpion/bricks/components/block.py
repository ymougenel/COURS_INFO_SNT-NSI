import pygame

from bricks.constants import *


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Block, self).__init__()
        self.surf = pygame.Surface(NORMAL_BLOCK_SIZE)
        # TODO choose random color
        self.surf.fill(BLOCKS_COLORS[0])
        self.rect = self.surf.get_rect()
        self.rect.move_ip(x, y)

    def display(self, screen: pygame.Surface):
        screen.blit(self.surf, self.rect)
