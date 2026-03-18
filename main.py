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
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                figure.rotate()
        #
        #     if event.key == pg.K_DOWN:
        #         snake.rotate(180)
        #         turn_group.append([snake.rect, 180])
        #
            if event.key == pg.K_LEFT:
                figure.moving_left()

            if event.key == pg.K_RIGHT:
                figure.moving_right()

    visual.field_rendering(screen)
    if pg.time.get_ticks() - update_time > cooldown:
        figure.update_figure()
        update_time = pg.time.get_ticks()


    # #
    # # if pg.time.get_ticks() - update_time > cooldown:
    # #     for elem in turn_group:
    # #         del_turn = True
    # #         for snakes in snake_group:
    # #             if snakes.rect == elem[0]:
    # #                 snakes.rotate(elem[1])
    # #                 del_turn = False
    # #         if del_turn:
    # #             del turn_group[turn_group.index(elem)]
    #
    #     update_time = pg.time.get_ticks()
    #     snake_group.update()
    #     cooldown -= 2

    pg.display.flip()
    pg.display.update()
    clock.tick(constants.FPS)
