import pygame
import random

vector = pygame.math.Vector2

pygame.init()

# Screen - title size is 32*32 so 1280/32 = 40 tiles wide, 736/32 = 23 tiles high
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Knight")

# Set PFS and clock
FPS = 60
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def add_zombie(self):
        pass

    def check_collisions(self):
        pass

    def check_round_completion(self):
        pass

    def check_game_over(self):
        pass

    def start_new_round(self):
        pass

    def pause_game(self):
        pass

    def reset_game(self):
        pass


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pass


class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pass

    def update(self):
        pass

    def move(self):
        pass

    def check_collisions(self):
        pass

    def check_animations(self):
        pass

    def jump(self):
        pass

    def fire(self):
        pass

    def reset(self):
        pass

    def animate(self):
        pass


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, direction):
        pass

    def update(self):
        pass


class Zombie(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pass

    def update(self):
        pass

    def move(self):
        pass

    def check_collisions(self):
        pass

    def check_animations(self):
        pass

    def animate(self):
        pass


background_image = pygame.transform.scale(pygame.image.load("images/background.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

# Main loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(background_image, background_rect)

    # Update
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
