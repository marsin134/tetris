import pygame as pg
from data.script import visual, constants, blocks_sprite, menu
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

update_time = pg.time.get_ticks()

pause = False

running = menu.menu(screen)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pause = not pause

            if not pause:
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

    if not pause:
        if pg.time.get_ticks() - update_time > cooldown:
            figure.move_down()
            update_time = pg.time.get_ticks()

        if figure.stop_figure:
            line_count = blocks_sprite.scoring_points()
            lines += line_count
            points += constants.POINTS_PER_LINE[line_count] * (speed_index + 1)
            speed_index = blocks_sprite.calculating_speed_index(points)
            cooldown = constants.DICT_SPEED[speed_index]

            figure = blocks_sprite.Figure(block_type)
            block_type = randint(2, 8)

    if pause:
        screen.blit(visual.image_grey, (0, 0))
        screen.blit(menu.pause_text, constants.CORDS_TEXT_PAUSE)

    pg.display.flip()
    pg.display.update()
    clock.tick(constants.FPS)
