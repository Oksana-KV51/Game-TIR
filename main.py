import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('игра ТИР')
icon = pygame.image.load('img/2024.jpg')
pygame.display.set_icon(icon)

background_img = pygame.image.load('img/3736.jpg')
target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 60

hit_points = 10
points_scored = 0

targets = []
for _ in range(5):
    target_x = random.randint(0, SCREEN_WIDTH - target_width)
    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    targets.append((target_x, target_y))

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
#color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

running = True
clock = pygame.time.Clock()

while running:
    screen.blit(background_img, (0, 0))  # Отобразить фоновое изображение

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for idx, target in enumerate(targets):
                target_x, target_y = target
                if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                    targets[idx] = (random.randint(0, SCREEN_WIDTH - target_width), random.randint(0, SCREEN_HEIGHT - target_height))
                    points_scored += hit_points

    for target in targets:
        target_x, target_y = target
        screen.blit(target_img, (target_x, target_y))

    pygame.display.update()

    clock.tick(30)

print(f'Summa hitting: {points_scored}')

pygame.quit()

