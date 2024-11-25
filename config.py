import components
import pygame

win_height = 1024/1.5
win_width = 768/1.5
window = pygame.display.set_mode((win_width, win_height))

ground = components.Ground(win_width)
pipes = []