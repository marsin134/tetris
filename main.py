import pygame as pg
from data.script import visual, constants, blocks_sprite, menu
from random import randint

clock = pg.time.Clock()

screen = constants.SCREEN


def game(screen: pg.display):
    blocks_sprite.clear_map()

    block_type = randint(2, 8)
    figure = blocks_sprite.Figure(block_type)
    block_type = randint(2, 8)

    points = 0
    speed_index = points // 300
    lines = 0
    cooldown = constants.DICT_SPEED[speed_index]

    update_time = pg.time.get_ticks()

    pause = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
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

            if event.type == pg.MOUSEBUTTONUP:
                if not pause:
                    if menu.button_left.rect.collidepoint(event.pos):
                        figure.move_left()
                    elif menu.button_down.rect.collidepoint(event.pos):
                        figure.move_down()
                    elif menu.button_right.rect.collidepoint(event.pos):
                        figure.move_right()
                    elif menu.button_rotate.rect.collidepoint(event.pos):
                        figure.rotate()
                    elif menu.button_pause.rect.collidepoint(event.pos):
                        pause = True
                else:
                    if menu.return_button_in_pause.rect.collidepoint(event.pos):
                        pause = False
                    elif menu.exit_in_pause.rect.collidepoint(event.pos):
                        return True

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

            menu.button_group_control.update(screen)

        if pause:
            screen.blit(visual.image_grey, (0, 0))
            screen.blit(menu.pause_text, constants.CORDS_TEXT_PAUSE)
            menu.button_group_pause.update(screen)

        pg.display.flip()
        pg.display.update()
        clock.tick(constants.FPS)


running = menu.menu(screen)
while running:
    running = exit_in_menu_flag = game(screen)
    if exit_in_menu_flag:
        running = menu.menu(screen)
