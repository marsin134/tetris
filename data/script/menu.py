import pygame as pg
from . import visual
from . import constants

image_buttons = visual.load_image('button.png', transforms=constants.BUTTON_SIZE)


class Button(pg.sprite.Sprite):

    def __init__(self, pos, text, shift, font_normal=constants.TEXT_FONT_BUTTON.render,
                 font_min_text=constants.TEXT_FONT_BUTTON_MIN.render, color='black'):
        pg.sprite.Sprite.__init__(self)
        self.image = image_buttons
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.text = [font_normal(text, 1, pg.Color(color)),
                     font_min_text(text, 1, pg.Color(color))]
        self.shift = shift
        self.hovered = False

    def update(self, surface):
        surface.blit(self.image, self.rect)
        if self.rect.collidepoint(pg.mouse.get_pos()) and not self.hovered:
            self.hovered = True
        elif not self.rect.collidepoint(pg.mouse.get_pos()):
            self.hovered = False

        if self.hovered:
            surface.blit(self.text[1], (self.rect.x + self.shift[0], self.rect.y + self.shift[1]))
        else:
            surface.blit(self.text[0], (self.rect.x + self.shift[0], self.rect.y + self.shift[1]))


def menu(screen: pg.display):
    running = True
    while running:
        for event in pg.event.get():
            # when closing the window
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONUP:
                # if you click on the start button, we start the game
                if start.rect.collidepoint(event.pos):
                    return True

                # if you click on the exit button, we end the game
                elif exit_in_menu.rect.collidepoint(event.pos):
                    return False
        # show fon
        screen.fill(constants.SCREEN_FILL)

        # show button
        button_group_menu.update(screen)
        screen.blit(name_game_text, constants.CORDS_TEXT_TETRIS)

        pg.display.flip()


button_group_menu = pg.sprite.Group()

# music_click = pygame.mixer.Sound('data/music/data_music_click_m.wav')
# music_fon_menu = pygame.mixer.Sound('data/music/Oklou_Casey_MQ_-_Lurk.mp3')
# music_hooked = pygame.mixer.Sound('data/music/data_music_hooked_m.wav')

# create fon
# fon = pygame.transform.scale(visual.load_image('fons/fon_menu.png'), (CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT))

# create button
start = Button(constants.CORDS_START_BUTTON,
               'Play', (100, 20))

statistics_button = Button(constants.CORDS_STATISTICS_BUTTON,
                           'Statistics', (37, 17))

exit_in_menu = Button(constants.CORDS_EXIT_BUTTON,
                      'Exit', (100, 20))

exit_in_pause = Button(constants.CORDS_PAUSE_BUTTON,
                       'Exit in menu', (95, 20))

# create inscriptions
name_game_text = constants.BIG_TEXT_FONT.render('Tetris', True, (255, 255, 255))
name_game_text.set_alpha(200)

pause_text = constants.BIG_TEXT_FONT.render('Pause', True, (255, 255, 255))

button_in_menu = [start, statistics_button, exit_in_menu]

for one_button in button_in_menu:
    button_group_menu.add(one_button)

# purchase_sound = pygame.mixer.Sound('data/music/buyTrue.mp3')
# purchase_cancelled_sound = pygame.mixer.Sound('data/music/buyFalse.mp3')
# mem_sound = pygame.mixer.Sound('data/music/the sound for Easter eggs.mp3')
