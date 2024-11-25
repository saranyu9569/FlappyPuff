import pygame
import config

class Buttercup:
    def __init__(self):
        # Image
        self.bird_image = pygame.image.load("./image/cup1.png")
        self.bird_image = pygame.transform.scale(self.bird_image, (132//2, 80//2))

        # Bird
        self.x, self.y = 50, 200
        self.rect = self.bird_image.get_rect(topleft=(self.x, self.y))
        self.vel = 0
        self.flap = False
        self.alive = True
        self.lifespan = 0

        self.fall_animation_counter = 0  # Counter for fall animation frames
        self.fall_animation_speed = 5    # Speed of fall animation


    # Game related functions
    def draw(self, window):
        window.blit(self.bird_image, self.rect)



    def ground_collision(self, ground):
        return pygame.Rect.colliderect(self.rect, ground)

    def pipe_collision(self):
        for p in config.pipes:
            if pygame.Rect.colliderect(self.rect, p.top_rect) or \
               pygame.Rect.colliderect(self.rect, p.bottom_rect):
                return True
        return False

    def update(self, ground):
        if self.alive:
            if not (self.ground_collision(ground) or self.pipe_collision()):
                # Gravity
                self.vel += 0.25
                self.rect.y += self.vel
                if self.vel > 5:
                    self.vel = 5
                # Increment lifespan
                self.lifespan += 1
            else:
                self.alive = False
                self.vel = 0
                # Rotate the bird
                self.bird_image = pygame.transform.rotate(self.bird_image, -90)
                # Move Buttercup to the bottom of the screen
                while self.rect.bottom < config.win_height:
                    self.rect.y += 10  # Move down by 10 pixels

    def flap_wings(self):
        if self.alive and not self.sky_collision():  # Only flap if not at the top
            self.flap = True
            self.vel = -5

    def sky_collision(self):
        return bool(self.rect.y < 30)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.flap_wings()
    
    def restart(self):
        self.bird_image = pygame.image.load("./image/cup1.png")
        self.bird_image = pygame.transform.scale(self.bird_image, (132//2, 80//2))
        self.x, self.y = 50, 200
        self.rect = self.bird_image.get_rect(topleft=(self.x, self.y))
        self.alive = True
        

