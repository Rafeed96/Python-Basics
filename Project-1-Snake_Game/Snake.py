import pygame
import random
import time

pygame.init()


def Your_Score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesge = font_style.render(msg, True, color)
    dis.blit(mesge, [display_Width/6, display_Height/3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = display_Width/2
    y1 = display_Height/2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, display_Width-snake_block)/10.0)*10.0
    foody = round(random.randrange(0, display_Height-snake_block)/10.0)*10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press 'C' to Play Again or 'Q' to Quite The Game", red)

            Your_Score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                


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
