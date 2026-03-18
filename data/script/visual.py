import os
import sys
import pygame as pg
from . import constants
from . import blocks_sprite
from .image_func import load_image

frame = pg.Rect(constants.INDENT_WIDTH,
                constants.INDENT_HEIGHT,
                constants.GAME_FRAME_WIDTH + constants.WIDTH_GAME_FRAME * 2,
                constants.GAME_FRAME_HEIGHT + constants.WIDTH_GAME_FRAME * 2)

panel = load_image("panel.png", transforms=(constants.WIDTH, constants.COUNTER_PANEL_HEIGHT))

blocks = []
for height in range(frame[1] + constants.WIDTH_GAME_FRAME, frame[3] + frame[1] - constants.WIDTH_GAME_FRAME,
                    constants.BLOCK_SIZE):  # 20 cells wide
    line = []
    for width in range(frame[0] + constants.WIDTH_GAME_FRAME, frame[2] + frame[0] - constants.WIDTH_GAME_FRAME,
                       constants.BLOCK_SIZE):  # 10 cells in length
        line.append(blocks_sprite.Block((width, height)))
    blocks.append(line)


def field_rendering(screen: pg.display):
    screen.fill(constants.SCREEN_FILL)
    pg.draw.rect(screen, constants.GAME_FRAME, frame, width=constants.WIDTH_GAME_FRAME)
    screen.blit(panel, (0, 0))

    for lines in blocks:
        for block in lines:
            block.update()
            block.draw(screen)

