import pygame

from bricks.boards.BlockTypes import BlockTypes
from bricks.components.block import Block
from bricks.constants import *
import random


def load_board(name):
    line = 0
    column = 0
    blocks = pygame.sprite.Group()
    file_name = "boards/done/" + name + ".board"
    board_content = []
    with open(file_name, "r") as input_file:
        for l in input_file.read().splitlines():
            line_content = [int(v) for v in l.split(",")]
            board_content.append(line_content)
    for line_content in board_content:
        for content in line_content:
            if content == BlockTypes.NORMAL.value:
                _add_block(blocks, line, column)
            column += 1
        line += 1

    return blocks


def _add_block(blocks, line, column):
    color = BLOCKS_COLORS[random.randint(0, len(BLOCKS_COLORS) - 1)]
    block = Block(NORMAL_BLOCK_SIZE[0] * column, NORMAL_BLOCK_SIZE[1] * line, color)
    blocks.add(block)
