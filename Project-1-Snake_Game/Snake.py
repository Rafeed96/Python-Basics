import pygame
import random
import time

pygame.init()


def Your_Score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 153, 213)
green = (0, 255, 0)
yellow = (255, 255, 102)


display_Width = 720
display_Height = 720

dis = pygame.display.set_mode(display_Width, display_Height)
pygame.display.set_caption("Snakes in Python")

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10


font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
