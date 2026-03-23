import pygame as pg

pg.init()

WIDTH, HEIGHT = SIZE = 500, 800
CELL_SIZE = 50

# SCREEN_FILL = "#041a20"
SCREEN_FILL = "#000000"

GAME_FRAME = "#166ae9"
GAME_FRAME_WIDTH = 300
GAME_FRAME_HEIGHT = 600
WIDTH_GAME_FRAME = 10

FPS = 60

COUNTER_PANEL_HEIGHT = 20
COLOR_COUNTER_PANEL = "#000000"
INDENT_WIDTH = 20
INDENT_HEIGHT = COUNTER_PANEL_HEIGHT

WIDTH_TEXT = GAME_FRAME_WIDTH + 70
WIDTH_FIGURE_NEXT = GAME_FRAME_WIDTH + 40

BLOCK_FRAME_COLOR = "#06262f"
RED_BLOCK = "red"
CYAN_BLOCK = "cyan"
YELLOW_BLOCK = "yellow"
PURPLE_BLOCK = "purple"
ORANGE_BLOCK = "orange"
BLUE_BLOCK = "blue"
GREEN_BLOCK = "green"
GREY_BLOCK = "grey"

BLOCK_SIZE = GAME_FRAME_WIDTH // 10

SCREEN = pg.display.set_mode(SIZE)

TIME_SECOND = 1000

POINTS_PER_LINE = {0: 0,
                   1: 40,
                   2: 100,
                   3: 300,
                   4: 1200}

DICT_SPEED = {0: 0.8 * TIME_SECOND,
              1: 0.72 * TIME_SECOND,
              2: 0.63 * TIME_SECOND,
              3: 0.55 * TIME_SECOND,
              4: 0.47 * TIME_SECOND,
              5: 0.38 * TIME_SECOND,
              6: 0.3 * TIME_SECOND,
              7: 0.22 * TIME_SECOND,
              8: 0.15 * TIME_SECOND,
              9: 0.1 * TIME_SECOND}

TEXT_FONT = pg.font.SysFont('arial', 36)
TEXT_SCORE = TEXT_FONT.render("SCORE", True, (255, 255, 255))
TEXT_LINES = TEXT_FONT.render("LINES", True, (255, 255, 255))
TEXT_LEVEL = TEXT_FONT.render("LEVEL", True, (255, 255, 255))
TEXT_NEXT = TEXT_FONT.render("NEXT", True, (255, 255, 255))