import os
import sys
import pygame as pg


def load_image(name, colorkey=None, transforms=None):
    fullname = os.path.join('data/image', name)

    if not os.path.isfile(fullname):
        print(f"The image file '{fullname}' was not found")
        sys.exit()
    image = pg.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    if transforms:
        image = pg.transform.scale(image, transforms)
    return image


def cut_sheet(list_sheet, count_sprites) -> []:
    url = "data/image/"
    frames = []

    sheet = load_image(f'{list_sheet}', colorkey=-1)
    rect = pg.Rect(0, 0, sheet.get_width() // count_sprites, sheet.get_height())

    for j in range(count_sprites):
        rect = pg.Rect(0, 0, sheet.get_width() // count_sprites, sheet.get_height())

        frame_location = (rect.w * j, 0)
        frames.append(sheet.subsurface(pg.Rect(frame_location, rect.size)))
    return frames
