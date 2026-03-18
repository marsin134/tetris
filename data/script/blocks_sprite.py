import pygame as pg
from random import randint
from . import constants

# blocks = image_func.cut_sheet("sprites.png", 7)
map_block = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

hash_block_color = {0: constants.BLOCK_FRAME_COLOR,
                    1: constants.RED_BLOCK}

hash_block_cords = {
    1: [[[0, 0], [0, 1], [0, 2], [1, 2]],
        [[0, 2], [1, 2], [2, 2], [2, 1]],
        [[1, 2], [1, 1], [1, 0], [0, 0]],
        [[2, 0], [1, 0], [0, 0], [0, 1]]],  # [height, width]
    2: [[0, 0], [0, 1], [0, 2], [1, 1]],
    3: [[0, 0], [0, 1], [0, 2], [1, 0]],
    4: [[1, 0], [1, 1], [0, 1], [0, 2]],
    5: [[0, 0], [0, 1], [0, 2], [0, 3]],
    6: [[0, 0], [1, 0], [1, 1], [0, 1]],
    7: [[0, 0], [0, 1], [1, 1], [1, 2]]}


class Block:
    def __init__(self, cords):
        self.color = constants.BLOCK_FRAME_COLOR
        self.width_frame = 1

        self.rect = pg.Rect(cords[0],
                            cords[1],
                            constants.BLOCK_SIZE,
                            constants.BLOCK_SIZE)
        self.update()

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect, width=self.width_frame)

    def update(self):
        height_index = (self.rect[1] - constants.INDENT_HEIGHT) // constants.BLOCK_SIZE
        width_index = (self.rect[0] - constants.INDENT_WIDTH) // constants.BLOCK_SIZE
        index_block = map_block[height_index][width_index]
        self.color = hash_block_color[index_block]
        # self.width_frame = 1 if index_block == 0 else 0


class Figure:
    def __init__(self):
        self.rotate_index = 0
        self.index_block = 1
        self.blocks = hash_block_cords[self.index_block][self.rotate_index]
        for i in range(len(self.blocks)):
            self.blocks[i][1] += 4

        self.on_move = True
        # self.random_block()

    def update_figure(self):
        # clear old blocks
        for i in range(len(self.blocks)):
            if self.blocks[i][0] > 0 and [self.blocks[i][0] - 1, self.blocks[i][1]] not in self.blocks:
                map_block[self.blocks[i][0] - 1][self.blocks[i][1]] = 0

        # write shift blocks down by one
        for i in range(len(self.blocks)):
            map_block[self.blocks[i][0]][self.blocks[i][1]] = self.index_block
            if self.blocks[i][0] + 1 == len(map_block):
                self.on_move = False

            self.blocks[i][0] += 1

    def moving_left(self):
        # clear old figure
        for block in self.blocks:
            map_block[block[0] - 1][block[1]] = 0

        for i in range(len(self.blocks)):
            self.blocks[i][1] -= 1
            map_block[self.blocks[i][0] - 1][self.blocks[i][1]] = self.index_block

    def moving_right(self):
        # clear old figure
        for block in self.blocks:
            map_block[block[0] - 1][block[1]] = 0

        for i in range(len(self.blocks)):
            self.blocks[i][1] += 1
            map_block[self.blocks[i][0] - 1][self.blocks[i][1]] = self.index_block

    def rotate(self):
        self.rotate_index = (self.rotate_index + 1) % 4

        # clear old figure
        for block in self.blocks:
            map_block[block[0] - 1][block[1]] = 0

        old_block = sorted(self.blocks)[0]
        self.blocks = hash_block_cords[self.index_block][self.rotate_index]
        for i in range(len(self.blocks)):
            self.blocks[i][0] += old_block[0]
            self.blocks[i][1] += old_block[1]
            map_block[self.blocks[i][0] - 1][self.blocks[i][1]] = self.index_block

    def random_block(self):
        self.index_block = randint(1, 7)
        self.blocks = hash_block_cords[self.index_block][self.rotate_index]
