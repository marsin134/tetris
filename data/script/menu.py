import pygame as pg
from . import constants, statistics_window
from .button import Button


def menu(screen: pg.display):
    running = True
    while running:
        for event in pg.event.get():
            # when closing the window
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONUP:
                # if you click on the start button, we start the game
                if start_button.rect.collidepoint(event.pos):
                    return True

                # if you click on the exit button, we end the game
                elif exit_in_menu.rect.collidepoint(event.pos):
                    return False

                elif statistics_button.rect.collidepoint(event.pos):
                    statistics_window.statistics_window(screen)
        # show fon
        screen.fill(constants.SCREEN_FILL)

        # show button
        button_group_menu.update(screen)
        screen.blit(name_game_text, constants.CORDS_TEXT_TETRIS)

        pg.display.flip()


# music_click = pygame.mixer.Sound('data/music/data_music_click_m.wav')
# music_fon_menu = pygame.mixer.Sound('data/music/Oklou_Casey_MQ_-_Lurk.mp3')
# music_hooked = pygame.mixer.Sound('data/music/data_music_hooked_m.wav')

# create button
start_button = Button(constants.CORDS_START_BUTTON,
                      'Play', (100, 20))

statistics_button = Button(constants.CORDS_STATISTICS_BUTTON,
                           'Statistics', (37, 17))

exit_in_menu = Button(constants.CORDS_EXIT_BUTTON,
                      'Exit', (100, 20))

return_button_in_pause = Button(constants.CORDS_RETURN_BUTTON,
                                "Return game", (20, 15), size_button=constants.BUTTON_SIZE_PAUSE,
                                font_normal=constants.TEXT_FONT_PAUSE.render,
                                font_min_text=constants.TEXT_FONT_PAUSE_MIN.render)

exit_in_pause = Button(constants.CORDS_EXIT_IN_MENU_BUTTON,
                       'Exit in menu', (22, 15), size_button=constants.BUTTON_SIZE_PAUSE,
                       font_normal=constants.TEXT_FONT_PAUSE.render, font_min_text=constants.TEXT_FONT_PAUSE_MIN.render)

button_left = Button(constants.CORDS_BUTTON_LEFT,
                     '←', (11, 3), size_button=constants.BUTTON_CONTROL_SIZE,
                     font_normal=constants.TEXT_FONT_CONTROL.render,
                     font_min_text=constants.TEXT_FONT_CONTROL_MIN.render)

button_down = Button(constants.CORDS_BUTTON_DOWN,
                     '↓', (25, 0), size_button=constants.BUTTON_CONTROL_SIZE,
                     font_normal=constants.TEXT_FONT_CONTROL.render,
                     font_min_text=constants.TEXT_FONT_CONTROL_MIN.render)

button_right = Button(constants.CORDS_BUTTON_RIGHT,
                      '→', (11, 3), size_button=constants.BUTTON_CONTROL_SIZE,
                      font_normal=constants.TEXT_FONT_CONTROL.render,
                      font_min_text=constants.TEXT_FONT_CONTROL_MIN.render)

button_rotate = Button(constants.CORDS_BUTTON_ROTATE,
                       'r', (30, 5), size_button=constants.BUTTON_CONTROL_SIZE,
                       font_normal=constants.TEXT_FONT_CONTROL.render,
                       font_min_text=constants.TEXT_FONT_CONTROL_MIN.render)

button_pause = Button(constants.CORDS_BUTTON_PAUSE,
                      '||', (27, 1), size_button=constants.BUTTON_CONTROL_SIZE,
                      font_normal=constants.TEXT_FONT_CONTROL.render,
                      font_min_text=constants.TEXT_FONT_CONTROL_MIN.render)

# create inscriptions
name_game_text = constants.BIG_TEXT_FONT.render('Tetris', True, (255, 255, 255))
name_game_text.set_alpha(200)
pause_text = constants.BIG_TEXT_FONT.render('Pause', True, (255, 255, 255))

button_in_menu = [start_button, statistics_button, exit_in_menu]
button_in_pause = [return_button_in_pause, exit_in_pause]
button_control = [button_left, button_down, button_right, button_rotate, button_pause]

button_group_menu = pg.sprite.Group()
button_group_pause = pg.sprite.Group()
button_group_control = pg.sprite.Group()

for button in button_in_menu:
    button_group_menu.add(button)
for button in button_in_pause:
    button_group_pause.add(button)
for button in button_control:
    button_group_control.add(button)
