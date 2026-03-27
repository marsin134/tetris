import pygame as pg
from . import constants, visual
from .button import Button


def statistics_window(screen: pg.display):
    lines = [elem.replace("\n", "").split(':') for elem in read_file(constants.STATISTICS_TXT)]
    max_line_len = len(max(lines, key=lambda x: len(x[0]))[0])
    statistics_user_name = [line[0] for line in lines]
    statistics_user_points = [line[1] for line in lines]

    statistics_user_name_text = [constants.TEXT_FONT_STATISTICS.render(text, True, (255, 255, 255)) for text in
                                 statistics_user_name]
    statistics_user_points_text = [constants.TEXT_FONT_STATISTICS.render(text, True, (255, 255, 255)) for text in
                                   statistics_user_points]

    running = True
    while running:
        for event in pg.event.get():
            # when closing the window
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONUP:
                pass
                # # if you click on the start button, we start the game
                # if start_button.rect.collidepoint(event.pos):
                #     return True
                #
                # # if you click on the exit button, we end the game
                # elif exit_in_menu.rect.collidepoint(event.pos):
                #     return False

        screen.fill(constants.SCREEN_FILL)

        for i in range(1, len(statistics_user_points_text)):
            screen.blit(statistics_user_name_text[i], (10, i * 50))
            screen.blit(statistics_user_points_text[i], (170, i * 50))

        pg.display.flip()


def read_file(filename: str) -> []:
    with open(f"{constants.URL_TXT_FILE}{filename}", "r") as file:
        return file.readlines()


def write_statistics():
    user_statistic = read_file(constants.USER_TXT)[1].replace("\n", "")
    statistic_lines = read_file(constants.STATISTICS_TXT)
    heading = statistic_lines[0]
    records = [elem.replace("\n", "") for elem in statistic_lines[1:]]
    records.append(user_statistic)

    for i in range(len(records)):
        records[i] = records[i].split(":")
    records = sorted(records, key=lambda x: x[1], reverse=True)

    with open(f"{constants.URL_TXT_FILE}{constants.STATISTICS_TXT}", "w") as file:
        file.write(heading)
        for i in range(min(len(records), 10)):
            file.write(f'{":".join(records[i])}\n')


def update_user_name(user_name: str):
    line = read_file(constants.USER_TXT)
    with open(f"{constants.URL_TXT_FILE}last_user.txt", "w") as file:
        file.write(line[0])
        file.write(f"{user_name:0}")


def update_user_points(points: int):
    line = read_file(constants.USER_TXT)
    with open(f"{constants.URL_TXT_FILE}{constants.USER_TXT}", "w") as file:
        file.write(line[0])
        file.write(f"{line[1].split(':')[0]}:{points}")
