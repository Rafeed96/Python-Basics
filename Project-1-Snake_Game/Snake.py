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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= display_Width or x1 < 0 or y1 >= display_Height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change

            dis.fill(blue)

            pygame.draw.rect(
                dis, green, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)

            snake_List.append(snake_Head)

            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            Your_Score(Length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(
                    0, display_Width-snake_block)/10.0)*10.0

                foody = round(random.randrange(
                    0, display_Height-snake_block)/10.0)*10.0

                Length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()
    gameLoop()


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
