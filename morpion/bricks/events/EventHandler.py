import pygame, sys
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from bricks.events.Events import BALL_LOST


def __process_quit(events):
    for event in events:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
        elif event.type == QUIT:
            sys.exit()


def process_events():
    events = pygame.event.get()
    __process_quit(events)
    __process_custom_events(events)


def __process_custom_events(events):
    for event in events:
        if event.type == BALL_LOST:
            print("You lost")
            #TODO: improve ending
            sys.exit()
