import pygame
import random
from pygame.locals import *

WINDOW_SIZE = (600, 600)
PIXEL_SIZE = (10)


def colisao_body(pos1, pos2):
    return pos1 == pos2


def colisao_wall(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True


def pos_random():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake')

snake_list = [(250, 50), (260, 50), (270, 50)]
snake_body = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_body.fill((255, 255, 255))
snake_direction = K_LEFT

apple_body = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
apple_body.fill((255, 0, 0))
apple_pos = pos_random()


def restart_game():
    global snake_list
    global apple_pos
    global snake_direction
    snake_list[(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    apple_pos = pos_random()


while True:
    pygame.time.Clock().tick(15)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    screen.blit(apple_body, apple_pos)

    if colisao_body(apple_pos, snake_list[0]):
        snake_list.append((-10, -10))
        apple_pos = pos_random()

    for posicao in snake_list:
        screen.blit(snake_body, posicao)

    for i in range(len(snake_list)-1, 0, -1):
        if colisao_body(snake_list[0], snake_list[i]):
            restart_game()
        snake_list[i] = snake_list[i-1]

    if colisao_wall(snake_list[0]):
        restart_game()

    if snake_direction == K_UP:
        snake_list[0] = (snake_list[0][0], snake_list[0][1] - PIXEL_SIZE)
    elif snake_direction == K_DOWN:
        snake_list[0] = (snake_list[0][0], snake_list[0][1] + PIXEL_SIZE)
    elif snake_direction == K_LEFT:
        snake_list[0] = (snake_list[0][0] - PIXEL_SIZE, snake_list[0][1])
    elif snake_direction == K_RIGHT:
        snake_list[0] = (snake_list[0][0] + PIXEL_SIZE, snake_list[0][1])

    pygame.display.update()
