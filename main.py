import pygame
from sys import exit
import config
import components
import population
import buttercup

pygame.init()
clock = pygame.time.Clock()
population = population.Population(100)
butter = buttercup.Buttercup()
pygame.display.set_caption("Flappy Bird")
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
butter.alive = False
r = 1
score = 0
score1=0
last_score=0

class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				action = True

		#draw button
		config.window.blit(self.image, (self.rect.x, self.rect.y))

		return action

def generate_pipes():
    config.pipes.append(components.Pipes(config.win_width))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                butter.flap_wings()



def main():
    # Load background image
    background_image = pygame.image.load("./image/bg2.png")
    button_img=pygame.image.load("./image/restart.png")
    pipes_spawn_time = 10
    global score, r, score1, game_over,last_score
    button = Button(config.win_width // 2 -70, config.win_height //2 -20 , button_img)

    # Initialize game over delay
    game_over_delay = 20

    while True:
        clock.tick(1000)
        quit_game()

        # Draw background image
        config.window.blit(background_image, (0, 0))

        # Spawn Ground
        config.ground.draw(config.window)

        if not game_over:
            # Spawn Pipes
            if pipes_spawn_time <= 0:
                generate_pipes()
                pipes_spawn_time = 300
            pipes_spawn_time -= 1

            for p in config.pipes:
                p.draw(config.window)
                p.update()
                if p.off_screen:
                    config.pipes.remove(p)
                else:
                    if p.x + components.Pipes.width < population.players[0].x and not p.score_counted and not population.extinct():
                        score1 += 1
                        p.score_counted = True


            # Display scores
            font = pygame.font.Font(None, 36)
            score_surface = font.render(f"Round: {r}", True, (255, 255, 255))
            config.window.blit(score_surface, (10, 10))
            score_surface1 = font.render(f"Mojojojo Score: {score1}", True, (255, 255, 255))
            config.window.blit(score_surface1, (280, 10))
            score_surface2 = font.render(f"Last_score: {last_score}", True, (255, 255, 255))
            config.window.blit(score_surface2, (10, 40))
            

            # Check condition to update and draw Buttercup

            # Update population and increment r
            if not population.extinct() :
                population.update_live_players()
            else:
                print("Round: ",r)
                print("Score: ",score1)
                print("\n")
                last_score=score1
                score1 = 0
                score = 0
                config.pipes.clear()
                population.natural_selection()
                r += 1  # Increment r after the population is reset



    


        pygame.display.flip()

main()
