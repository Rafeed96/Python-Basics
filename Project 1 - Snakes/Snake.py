# Snake game

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


# Class for apple or cube

class cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

# Class for snake


class snake(object):
    def __int__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):

    pass


def redrawWindow(surface):
    global rows, width
    win.fill((0, 0, 0))
    drawGrid(surface)
    pygame.display.update()
    pass


def randomSnack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width,height))
    s = snake((255,0,0), (10,10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(60)
        clock.tick(10)

        redrawWindow(win)
    pass


main()