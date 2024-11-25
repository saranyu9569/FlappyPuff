import pygame
import random

class Ground:
    ground_level = 50

    def __init__(self, win_width):
        self.x, self.y = 0, Ground.ground_level
        self.rect = pygame.Rect(self.x, self.y, win_width, 500)

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), self.rect)


import pygame
import random

class Ground:
    ground_level = 680

    def __init__(self, win_width):
        self.x, self.y = 0, Ground.ground_level
        self.rect = pygame.Rect(self.x, self.y, win_width, 5)

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), self.rect)


class Pipes:
    width = 70
    opening = 150

    def __init__(self, win_width):
        self.x = win_width
        self.bottom_height = random.randint(150, 400)
        self.top_height = Ground.ground_level - self.bottom_height - self.opening
        # Load the original images
        self.bottom_image = pygame.image.load("./image/bottom.png")
        self.top_image = pygame.image.load("./image/top.png")
        # Resize the images
        self.bottom_image = pygame.transform.scale(self.bottom_image, (Pipes.width, self.bottom_height))
        self.top_image = pygame.transform.scale(self.top_image, (Pipes.width, self.top_height))
        self.bottom_rect, self.top_rect = pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0)
        self.passed = False
        self.off_screen = False
        self.score_counted = False
        self.score_counted1 = False

    def draw(self, window):
        self.bottom_rect = self.bottom_image.get_rect(midtop=(self.x, Ground.ground_level - self.bottom_height))
        window.blit(self.bottom_image, self.bottom_rect)

        top_y_position = 0 + self.top_height - 50  # Adjust the offset as needed
        self.top_rect = self.top_image.get_rect(midbottom=(self.x, top_y_position))
        window.blit(self.top_image, self.top_rect)

    def update(self):
        self.x -= 1
        if self.x + Pipes.width <= 50:
            self.passed = True
        if self.x <= -self.width:
            self.off_screen = True
            self.score_counted = False
