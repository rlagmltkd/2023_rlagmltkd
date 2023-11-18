import pygame

colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    '2': (236, 239, 241),
    '4': (207, 216, 220),
    '8': (176, 190, 197),
    '16': (144, 164, 174),
    '32': (120, 144, 156),
    '64': (96, 125, 139),
    '128': (84, 110, 122),
    '256': (69, 90, 100),
    '512': (55, 71, 79),
    '1024': (38, 50, 56),
    '2048': (29, 37, 41),


def initScreen():
    size = (500, 500)
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen = pygame.display.set_mode(size)
    screen.fill(white)
    pygame.display.update()


def run2048():
    pygame.init()
    initScreen()
    print("2048 게임 시작")

    pygame.quit()


run2048()
