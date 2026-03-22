import pygame as pg
from data.script import visual, constants, blocks_sprite

clock = pg.time.Clock()

screen = constants.SCREEN

figure = blocks_sprite.Figure()

cooldown = 1 * constants.TIME_SECOND

running = True
update_time = pg.time.get_ticks()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and figure.can_move:
            if event.key == pg.K_UP:
                figure.rotate()

            if event.key == pg.K_DOWN:
                figure.move_down()
                update_time = pg.time.get_ticks()

            if event.key == pg.K_LEFT:
                figure.move_left()

            if event.key == pg.K_RIGHT:
                figure.move_right()

    visual.field_rendering(screen)

    if pg.time.get_ticks() - update_time > cooldown:
        figure.move_down()
        update_time = pg.time.get_ticks()

    if not figure.can_move:
        figure = blocks_sprite.Figure()

    pg.display.flip()
    pg.display.update()
    clock.tick(constants.FPS)
