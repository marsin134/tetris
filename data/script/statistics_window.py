import pygame as pg
from . import constants, visual
from .button import Button


def statistics_window(screen: pg.display):
    """a window that displays statistics"""
    lines = [elem.replace("\n", "").split(':') for elem in read_file(constants.STATISTICS_TXT)]

    user = read_file(constants.USER_TXT)[1].split(':')

    user_name_text = constants.TEXT_FONT_USERNAME.render(f"USERNAME", True, (255, 255, 255))
    user_speed_text = constants.TEXT_FONT.render(user[2], True, (255, 255, 255))

    statistics_user_name = [line[0] for line in lines]
    statistics_user_points = [line[1] for line in lines]

    statistics_user_number_text = [constants.TEXT_FONT_STATISTICS.render(str(i), True, (255, 255, 255)) for i in
                                   range(len(statistics_user_name))]
    statistics_user_name_text = [constants.TEXT_FONT_STATISTICS.render(text, True, (255, 255, 255)) for text in
                                 statistics_user_name]
    statistics_user_points_text = [constants.TEXT_FONT_STATISTICS.render(text, True, (255, 255, 255)) for text in
                                   statistics_user_points]

    last_point_text = constants.TEXT_FONT.render(f"Last point: {user[1]}", True, (255, 255, 255))

    # creating table cells
    cells = []
    for i in range(len(statistics_user_name_text)):
        line_cell = []
        for cell in [constants.STATISTICS_FIRST_CELL, constants.STATISTICS_SECOND_CELL,
                     constants.STATISTICS_THIRD_CELL]:
            line_cell.append(pg.Rect(cell[0], cell[1] + cell[3] * i, cell[2], cell[3]))
        cells.append(line_cell)

    # basic values for the letter writing window
    active_write = False
    input_box = pg.Rect(constants.INPUT_BOX_RECT)
    color_inactive = constants.INPUT_BOX_CLOR_INACTIVE
    color_active = constants.INPUT_BOX_COLOR_ACTIVE
    color = color_inactive
    text = user[0]

    running = True
    while running:
        for event in pg.event.get():
            # when closing the window
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONUP:
                # we change the speed using the buttons
                if button_left.rect.collidepoint(event.pos) and int(user[2]) - 1 >= 1:
                    constants.MUSIC_CLICK.play()
                    user[2] = str(int(user[2]) - 1)
                    user_speed_text = constants.TEXT_FONT.render(user[2], True, (255, 255, 255))
                    update_user_speed(int(user[2]))

                elif button_right.rect.collidepoint(event.pos) and int(user[2]) + 1 <= 10:
                    constants.MUSIC_CLICK.play()
                    user[2] = str(int(user[2]) + 1)
                    user_speed_text = constants.TEXT_FONT.render(user[2], True, (255, 255, 255))
                    update_user_speed(int(user[2]))

                # We go out the window
                elif button_exit.rect.collidepoint(event.pos):
                    constants.MUSIC_CLICK.play()
                    return

                # If the user clicked on the input_box rect.
                elif input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active_write = not active_write
                else:
                    active_write = False
                    update_user_name(text)

                color = color_active if active_write else color_inactive

            # writing letters to enter the username
            if event.type == pg.KEYDOWN and active_write:
                if event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                elif len(text) <= 7:
                    text += event.unicode

        txt_surface = constants.TEXT_FONT_USERNAME.render(text, True, color)

        screen.fill(constants.SCREEN_FILL)

        # displaying the text
        screen.blit(icon_image, constants.ICON_CORDS)
        screen.blit(user_name_text, constants.NAME_CORDS)
        screen.blit(speed_text, constants.SPEED_CORDS_WORD)
        screen.blit(user_speed_text, constants.SPEED_CORDS_NUM)
        screen.blit(statistics_text, constants.STATISTICS_WORD_CORDS)
        screen.blit(last_point_text, constants.LAST_POINT_WORD_CORDS)

        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 2))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        # displaying the statistics table
        for i, line in enumerate(cells):
            for cell in line:
                pg.draw.rect(screen, (255, 255, 255), cell, width=1)
            screen.blit(statistics_user_number_text[i],
                        (line[0][0] + constants.INDENT_WIDTH, line[0][1] + constants.INDENT_HEIGHT_STATISTIC))
            screen.blit(statistics_user_name_text[i],
                        (line[1][0] + constants.INDENT_WIDTH, line[1][1] + constants.INDENT_HEIGHT_STATISTIC))
            screen.blit(statistics_user_points_text[i],
                        (line[2][0] + constants.INDENT_WIDTH, line[2][1] + constants.INDENT_HEIGHT_STATISTIC))

        button_statistic_group.update(screen)

        pg.display.flip()


def read_file(filename: str) -> []:
    """reading a file"""
    with open(f"{constants.URL_TXT_FILE}{filename}", "r") as file:
        return file.readlines()


def write_statistics():
    """record of sorted statistics, including the current user's last game"""
    user_statistic = ":".join(read_file(constants.USER_TXT)[1].replace("\n", "").split(":")[:2])
    statistic_lines = read_file(constants.STATISTICS_TXT)
    heading = statistic_lines[0]
    records = [elem.replace("\n", "") for elem in statistic_lines[1:]]
    records.append(user_statistic)

    for i in range(len(records)):
        records[i] = records[i].split(":")
    records = sorted(records, key=lambda x: int(x[1]), reverse=True)

    with open(f"{constants.URL_TXT_FILE}{constants.STATISTICS_TXT}", "w") as file:
        file.write(heading)
        for i in range(min(len(records), constants.COUNT_MAX_USERS)):
            file.write(f'{":".join(records[i])}\n')


def update_user_name(user_name: str):
    """writing a new username to a file"""
    line = read_file(constants.USER_TXT)
    with open(f"{constants.URL_TXT_FILE}last_user.txt", "w") as file:
        file.write(line[0])
        user = line[1].split(':')
        file.write(f"{user_name}:0:{user[2]}")


def update_user_points(points: int):
    """writing a new points to a file"""
    line = read_file(constants.USER_TXT)
    with open(f"{constants.URL_TXT_FILE}{constants.USER_TXT}", "w") as file:
        file.write(line[0])
        user = line[1].split(':')
        file.write(f"{user[0]}:{points}:{user[2]}")


def update_user_speed(speed: int):
    """writing a new speed to a file"""
    line = read_file(constants.USER_TXT)
    with open(f"{constants.URL_TXT_FILE}{constants.USER_TXT}", "w") as file:
        file.write(line[0])
        user = line[1].split(':')
        file.write(f"{user[0]}:{user[1]}:{speed}")


# creating things necessary for the window interface
icon_image = visual.load_image("icon.png", transforms=constants.ICON_SIZE)
speed_text = constants.TEXT_FONT.render("Speed", True, (255, 255, 255))
button_left = Button(constants.CORDS_SPEED_BUTTON_LEFT,
                     '←', (11, 3), size_button=constants.BUTTON_CONTROL_SIZE,
                     font_normal=constants.TEXT_FONT_CONTROL.render,
                     font_min_text=constants.TEXT_FONT_CONTROL_MIN.render)
button_right = Button(constants.CORDS_SPEED_BUTTON_RIGHT,
                      '→', (11, 3), size_button=constants.BUTTON_CONTROL_SIZE,
                      font_normal=constants.TEXT_FONT_CONTROL.render,
                      font_min_text=constants.TEXT_FONT_CONTROL_MIN.render)
button_exit = Button(constants.EXIT_FROM_STATISTIC_WINDOW_CORDS,
                     '→', (13, 7), size_button=(constants.BUTTON_STATISTIC_EXIT_SIZE),
                     font_normal=constants.TEXT_FONT_PAUSE.render,
                     font_min_text=constants.TEXT_FONT_PAUSE_MIN.render)

statistics_text = constants.TEXT_FONT.render("Statistics:", True, (255, 255, 255))

button_statistic_group = pg.sprite.Group()
for button in [button_right, button_left, button_exit]:
    button_statistic_group.add(button)
