import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

pygame.display.set_caption('игра ТИР')
icon = pygame.image.load('img/photo_2024-03-22_21-35-39.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGTH - target_height)
color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))


running = True
while running:
    pass

pygame.quit()

