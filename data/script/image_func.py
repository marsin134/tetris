import os
import sys
import pygame as pg


def load_image(name, colorkey=None, transforms=None):
    """image upload functions"""
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

