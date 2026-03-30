import pygame as pg
from . import constants
from . import blocks_sprite
from .image_func import load_image

# create game frame
frame = pg.Rect(constants.INDENT_WIDTH,
                constants.INDENT_HEIGHT,
                constants.GAME_FRAME_WIDTH + constants.WIDTH_GAME_FRAME * 2,
                constants.GAME_FRAME_HEIGHT + constants.WIDTH_GAME_FRAME * 2)

# create blocks on game frame
blocks = []
for height in range(frame[1] + constants.WIDTH_GAME_FRAME, frame[3] + frame[1] - constants.WIDTH_GAME_FRAME,
                    constants.BLOCK_SIZE):  # 20 cells wide
    line = []
    for width in range(frame[0] + constants.WIDTH_GAME_FRAME, frame[2] + frame[0] - constants.WIDTH_GAME_FRAME,
                       constants.BLOCK_SIZE):  # 10 cells in length
        line.append(blocks_sprite.Block((width, height)))
    blocks.append(line)

# create a transparent gray field for pause
image_grey = pg.Surface((constants.WIDTH, constants.HEIGHT))
image_grey.fill((128, 128, 128))
image_grey.set_colorkey((0, 0, 0))
image_grey.set_alpha(100)


def field_rendering(screen: pg.display, points: int, level: int, lines: int, next_figure_type: int):
    """display of the game board, words, and statistics"""

    # create words statistics
    text_points = constants.TEXT_FONT.render(str(points), True, (255, 255, 255))
    text_level = constants.TEXT_FONT.render(str(level + 1), True, (255, 255, 255))
    text_lines = constants.TEXT_FONT.render(str(lines), True, (255, 255, 255))

    screen.fill(constants.SCREEN_FILL)
    # displaying game frame
    pg.draw.rect(screen, constants.GAME_FRAME, frame, width=constants.WIDTH_GAME_FRAME)

    # displaying blocks
    for lines in blocks:
        for block in lines:
            block.update()
            block.draw(screen)

    # displaying words
    screen.blit(constants.TEXT_SCORE, (constants.WIDTH_TEXT, constants.INDENT_HEIGHT))
    screen.blit(constants.TEXT_LEVEL, (constants.WIDTH_TEXT, constants.INDENT_HEIGHT * 5.5))
    screen.blit(constants.TEXT_LINES, (constants.WIDTH_TEXT, constants.INDENT_HEIGHT * 10))
    screen.blit(constants.TEXT_NEXT, (constants.WIDTH_TEXT, constants.INDENT_HEIGHT * 15))
    screen.blit(text_points, (constants.WIDTH_TEXT, constants.INDENT_HEIGHT * 3))
    screen.blit(text_level, (constants.WIDTH_TEXT, constants.INDENT_HEIGHT * 7.5))
    screen.blit(text_lines, (constants.WIDTH_TEXT, constants.INDENT_HEIGHT * 12))

    # displaying shape
    blocks_sprite.rect_figure((constants.WIDTH_FIGURE_NEXT, constants.INDENT_HEIGHT * 17), next_figure_type, screen)
