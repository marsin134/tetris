import pygame as pg
from data.script import visual, constants, blocks_sprite, menu, statistics_window
from random import randint


def game(screen: pg.display):
    """Tetris game function"""

    constants.MUSIC_BACKGROUND.play(-1)
    pg.mixer.music.set_volume(constants.VOLUME)

    # setting the basic values
    blocks_sprite.clear_map()

    block_type = randint(2, 8)
    figure = blocks_sprite.Figure(block_type)
    block_type = randint(2, 8)

    points = 0
    speed_index = int(statistics_window.read_file(constants.USER_TXT)[1].split(":")[2]) - 1
    lines = 0
    cooldown = constants.DICT_SPEED[speed_index]

    update_time = pg.time.get_ticks()

    pause = False

    while True:
        for event in pg.event.get():  # processing keyboard and mouse events
            if event.type == pg.QUIT:
                return False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pause = not pause

                if not pause and not figure.game_over:
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
                        statistics_window.update_user_points(points)
                        statistics_window.write_statistics()
                        constants.MUSIC_BACKGROUND.stop()
                        return True

        # displaying the playing field
        visual.field_rendering(screen, points, speed_index, lines, block_type)

        # if the game is over, notify the user
        if figure.game_over:
            screen.blit(constants.TEXT_GAME_OVER, constants.CORDS_GAME_OVER)
            screen.blit(constants.TEXT_PRESS_ESC, constants.CORDS_PRESS_ESC)

        elif not pause:
            if pg.time.get_ticks() - update_time > cooldown:
                figure.move_down()
                update_time = pg.time.get_ticks()

            if figure.stop_figure and not figure.game_over:
                line_count = blocks_sprite.scoring_points()
                lines += line_count
                points += constants.POINTS_PER_LINE[line_count] * (speed_index + 1)
                speed_index = blocks_sprite.calculating_speed_index(points, speed_index)
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


if __name__ == '__main__':
    clock = pg.time.Clock()
    screen = constants.SCREEN

    running = menu.menu(screen)
    while running:
        running = exit_in_menu_flag = game(screen)
        if exit_in_menu_flag:
            running = menu.menu(screen)

    pg.quit()
