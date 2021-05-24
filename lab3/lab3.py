import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

x = 300
y = 200
r = 320
N = 10
color = (255, 207, 72)
eyes_color = (189, 218, 87)
left_eye_position_x = x - ((r / 2) * 0.8)
eye_position_y = y - ((r / 2) * 0.5)
right_eye_position_x = x + ((r / 2) * 0.8)
# drawing part
circle(screen, color, (x, y), r)
circle(screen, 'black', (left_eye_position_x, eye_position_y), r * 0.31)
circle(screen, 'black', (right_eye_position_x, eye_position_y), r * 0.21)
circle(screen, eyes_color, (left_eye_position_x, eye_position_y), r * 0.3)
circle(screen, eyes_color, (right_eye_position_x, eye_position_y), r * 0.2)
circle(screen, 'black', (left_eye_position_x, eye_position_y), r * 0.08)
circle(screen, 'black', (right_eye_position_x, eye_position_y), r * 0.08)
line(screen, 'black', (left_eye_position_x + r * 0.4, eye_position_y - r * 0.2),
     (left_eye_position_x - r * 0.4, eye_position_y - r * 0.5), 20)
line(screen, 'black', (right_eye_position_x - r * 0.2, eye_position_y - r * 0.2),
     (right_eye_position_x + r * 0.4, eye_position_y - r * 0.5), 20)
line(screen, 'black', (x + r * 0.4, y + r * 0.5),
     (x - r * 0.4, y + r * 0.5), 30)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
