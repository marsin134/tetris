import pygame as pg
from random import randint
from . import constants
from copy import deepcopy

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
                    1: constants.CYAN_BLOCK,
                    2: constants.YELLOW_BLOCK,
                    3: constants.PURPLE_BLOCK,
                    4: constants.ORANGE_BLOCK,
                    5: constants.BLUE_BLOCK,
                    6: constants.GREEN_BLOCK,
                    7: constants.RED_BLOCK}

hash_block_cords = {
    # I-shape (Cyan)
    1: [
        [[0, 0], [0, 1], [0, 2], [0, 3]],  # Horizontal
        [[0, 0], [1, 0], [2, 0], [3, 0]],  # Vertical
        [[0, 0], [0, 1], [0, 2], [0, 3]],  # Horizontal (same as 0°)
        [[0, 0], [1, 0], [2, 0], [3, 0]]  # Vertical (same as 90°)
    ],

    # O-shape (Yellow)
    2: [
        [[0, 0], [0, 1], [1, 0], [1, 1]],  # Square (all rotations same)
        [[0, 0], [0, 1], [1, 0], [1, 1]],
        [[0, 0], [0, 1], [1, 0], [1, 1]],
        [[0, 0], [0, 1], [1, 0], [1, 1]]
    ],

    # T-shape (Purple)
    3: [
        [[0, 1], [1, 0], [1, 1], [1, 2]],  # 0°
        [[0, 1], [1, 1], [2, 1], [1, 2]],  # 90°
        [[1, 0], [1, 1], [1, 2], [2, 1]],  # 180°
        [[0, 1], [1, 0], [1, 1], [2, 1]]  # 270°
    ],

    # L-shape (Orange)
    4: [
        [[0, 0], [0, 1], [0, 2], [1, 2]],  # 0°
        [[0, 1], [1, 1], [2, 1], [2, 0]],  # 90°
        [[0, 0], [1, 0], [1, 1], [1, 2]],  # 180°
        [[0, 0], [1, 0], [2, 0], [0, 1]]  # 270°
    ],

    # J-shape (Blue)
    5: [
        [[0, 0], [1, 0], [0, 1], [0, 2]],  # 0°
        [[0, 1], [0, 2], [1, 2], [2, 2]],  # 90°
        [[0, 2], [1, 0], [1, 1], [1, 2]],  # 180°
        [[0, 0], [1, 0], [2, 0], [2, 1]]  # 270°
    ],

    # S-shape (Green)
    6: [
        [[0, 1], [0, 2], [1, 0], [1, 1]],  # 0°
        [[0, 0], [1, 0], [1, 1], [2, 1]],  # 90°
        [[0, 1], [0, 2], [1, 0], [1, 1]],  # 180° (same as 0°)
        [[0, 0], [1, 0], [1, 1], [2, 1]]  # 270° (same as 90°)
    ],

    # Z-shape (Red)
    7: [
        [[0, 0], [0, 1], [1, 1], [1, 2]],  # 0°
        [[0, 1], [1, 0], [1, 1], [2, 0]],  # 90°
        [[0, 0], [0, 1], [1, 1], [1, 2]],  # 180° (same as 0°)
        [[0, 1], [1, 0], [1, 1], [2, 0]]  # 270° (same as 90°)
    ]
}


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
        """Rendering a block"""
        pg.draw.rect(screen, self.color, self.rect, width=self.width_frame)

    def update(self):
        """Update block"""
        height_index = (self.rect[1] - constants.INDENT_HEIGHT) // constants.BLOCK_SIZE
        width_index = (self.rect[0] - constants.INDENT_WIDTH) // constants.BLOCK_SIZE
        index_block = map_block[height_index][width_index]
        self.color = hash_block_color[index_block]
        self.width_frame = 1 if index_block == 0 else 0


class Figure:
    def __init__(self):
        self.block_type = randint(1, 7)
        self.rotate_index = 0
        self.x = 4
        self.y = 0
        self.can_move = True

        self.shapes = deepcopy(hash_block_cords[self.block_type])
        self.update_shape_positions()
        self.blocks = self.get_blocks()

        # Check game over condition
        if self.check_collision(self.blocks):
            # Game over logic here
            pass

        self.update_map()

    def update_shape_positions(self):
        """Update all shape rotations positions relative to current coordinates"""
        for rotation in self.shapes:
            for block in rotation:
                block[0] = self.y + block[0]
                block[1] = self.x + block[1]

    def get_blocks(self, rot_index=None, x=None, y=None):
        """Get blocks at specified position and rotation"""
        rot = rot_index if rot_index is not None else self.rotate_index
        new_x = x if x is not None else self.x
        new_y = y if y is not None else self.y

        blocks = deepcopy(hash_block_cords[self.block_type][rot])
        for block in blocks:
            block[0] = new_y + block[0]
            block[1] = new_x + block[1]
        return blocks

    def check_collision(self, blocks):
        """Check collision with walls or other blocks"""
        for block in blocks:
            # Check boundaries
            if block[0] >= len(map_block) or block[1] < 0 or block[1] >= len(map_block[0]):
                return True

            # Check collision with other blocks (excluding current figure)
            if block[0] >= 0 and map_block[block[0]][block[1]] != 0 and block not in self.blocks:
                return True
        return False

    def clear_from_map(self):
        """Remove current figure from map"""
        for block in self.blocks:
            if (0 <= block[0] < len(map_block) and
                    0 <= block[1] < len(map_block[0]) and
                    map_block[block[0]][block[1]] == self.block_type):
                map_block[block[0]][block[1]] = 0

    def draw_on_map(self):
        """Draw current figure on map"""
        for block in self.blocks:
            if 0 <= block[0] < len(map_block):
                map_block[block[0]][block[1]] = self.block_type

    def update_map(self):
        """Update figure position on map"""
        self.clear_from_map()
        self.blocks = self.get_blocks()

        # Check if figure can move down
        blocks_down = self.get_blocks(y=self.y + 1)
        self.can_move = not self.check_collision(blocks_down)

        self.draw_on_map()

    def try_move(self, dx=0, dy=0):
        """Try to move figure by (dx, dy)"""
        new_blocks = self.get_blocks(x=self.x + dx, y=self.y + dy)

        if not self.check_collision(new_blocks):
            self.clear_from_map()
            self.x += dx
            self.y += dy
            self.update_shape_positions()
            self.update_map()
            return True
        return False

    def move_left(self):
        """Move figure left"""
        self.try_move(dx=-1)

    def move_right(self):
        """Move figure right"""
        self.try_move(dx=1)

    def move_down(self):
        """Move figure down, return False if stuck"""
        return self.try_move(dy=1)

    def rotate(self):
        """Rotate figure clockwise"""
        new_rot = (self.rotate_index + 1) % 4
        new_blocks = self.get_blocks(rot_index=new_rot)

        if not self.check_collision(new_blocks):
            self.clear_from_map()
            self.rotate_index = new_rot
            self.shapes = deepcopy(hash_block_cords[self.block_type])
            self.update_shape_positions()
            self.blocks = new_blocks
            self.draw_on_map()
