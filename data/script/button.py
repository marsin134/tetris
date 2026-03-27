import pygame as pg
from . import constants, visual


class Button(pg.sprite.Sprite):

    def __init__(self, pos, text, shift, font_normal=constants.TEXT_FONT_BUTTON.render,
                 font_min_text=constants.TEXT_FONT_BUTTON_MIN.render, color='black', size_button=constants.BUTTON_SIZE):
        pg.sprite.Sprite.__init__(self)

        self.image = visual.load_image('button.png', transforms=size_button)

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
