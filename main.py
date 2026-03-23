import pygame as pg
from data.script import visual, constants, blocks_sprite
from random import randint

clock = pg.time.Clock()

screen = constants.SCREEN

block_type = randint(2, 8)
figure = blocks_sprite.Figure(block_type)
block_type = randint(2, 8)

points = 0
speed_index = points // 300
lines = 0
cooldown = constants.DICT_SPEED[speed_index]

running = True
update_time = pg.time.get_ticks()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                figure.rotate()

            if event.key == pg.K_DOWN:
                figure.move_down()
                update_time = pg.time.get_ticks()

            if event.key == pg.K_LEFT:
                figure.move_left()

            if event.key == pg.K_RIGHT:
                figure.move_right()

    visual.field_rendering(screen, points, speed_index, lines, block_type)

    if pg.time.get_ticks() - update_time > cooldown:
        figure.move_down()
        update_time = pg.time.get_ticks()

    if figure.stop_figure:
        line_count = blocks_sprite.scoring_points()
        lines += line_count
        points += constants.POINTS_PER_LINE[line_count] * (speed_index + 1)
        if points >= 2700:
            speed_index = 9
        else:
            speed_index = points // 300
        cooldown = constants.DICT_SPEED[speed_index]

        figure = blocks_sprite.Figure(block_type)
        block_type = randint(2, 8)

    pg.display.flip()
    pg.display.update()
    clock.tick(constants.FPS)
