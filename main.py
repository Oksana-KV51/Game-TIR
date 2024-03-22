import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

pygame.display.set_caption('игра ТИР')
icon = pygame.image.load('img/2024.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGTH - target_height)
color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mous_x, mous_y = pygame.mouse.get_pos()
            if target_x < mous_x < target_x + target_width and target_y < mous_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGTH - target_height)
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()

