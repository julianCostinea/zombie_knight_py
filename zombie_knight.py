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
        self.STARTING_ROUND_TIME = 30

        self.score = 0
        self.round_number = 1
        self.frame_count = 0
        self.round_time = self.STARTING_ROUND_TIME

        # set fonts
        self.title_font = pygame.font.Font("fonts/Poultrygeist.ttf", 48)
        self.HUD_font = pygame.font.Font("fonts/Pixel.ttf", 24)

    def update(self):
        self.frame_count += 1
        if self.frame_count % FPS == 0:
            self.round_time -= 1
            self.frame_count = 0

    def draw(self):
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)

        score_text = self.HUD_font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, WINDOW_HEIGHT - 50)

        health_text = self.HUD_font.render("Health: " + str(100), True, WHITE)
        health_rect = health_text.get_rect()
        health_rect.topleft = (10, WINDOW_HEIGHT - 25)

        title_text = self.title_font.render("Zombie Knight", True, GREEN)
        title_rect = title_text.get_rect()
        title_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 25)

        round_text = self.HUD_font.render("Night: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 50)

        time_text = self.HUD_font.render("Sunrise in: " + str(self.round_time), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 25)

        display_surface.blit(score_text, score_rect)
        display_surface.blit(health_text, health_rect)
        display_surface.blit(title_text, title_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(time_text, time_rect)

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
    def __init__(self, x, y, image_int, main_group, sub_group=''):
        super().__init__()
        if image_int == 1:
            self.image = pygame.transform.scale(pygame.image.load("images/tiles/Tile (1).png"), (32, 32))
        elif image_int == 2:
            self.image = pygame.transform.scale(pygame.image.load("images/tiles/Tile (2).png"), (32, 32))
            sub_group.add(self)
        elif image_int == 3:
            self.image = pygame.transform.scale(pygame.image.load("images/tiles/Tile (3).png"), (32, 32))
            sub_group.add(self)
        elif image_int == 4:
            self.image = pygame.transform.scale(pygame.image.load("images/tiles/Tile (4).png"), (32, 32))
            sub_group.add(self)
        elif image_int == 5:
            self.image = pygame.transform.scale(pygame.image.load("images/tiles/Tile (5).png"), (32, 32))
            sub_group.add(self)

        main_group.add(self)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, platform_group, portal_group, bullet_group):
        super().__init__()

        self.HORIZONTAL_ACCELERATION = 2
        self.HORIZONTAL_FRICTION = 0.15
        self.VERTICAL_ACCELERATION = 0.8
        self.VERTICAL_JUMP_SPEED = 18
        self.STARTING_HEALTH = 100

        self.move_left_sprites = []
        self.move_right_sprites = []
        self.idle_left_sprites = []
        self.idle_right_sprites = []
        self.jump_left_sprites = []
        self.jump_right_sprites = []
        self.attack_right_sprites = []
        self.attack_left_sprites = []

        self.move_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (1).png"), (64, 64)))
        self.move_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (2).png"), (64, 64)))
        self.move_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (3).png"), (64, 64)))
        self.move_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (4).png"), (64, 64)))
        self.move_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (5).png"), (64, 64)))
        self.move_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (6).png"), (64, 64)))
        self.move_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (7).png"), (64, 64)))
        self.move_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (8).png"), (64, 64)))
        self.move_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (9).png"), (64, 64)))
        self.move_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (10).png"), (64, 64)))
        for sprite in self.move_right_sprites:
            self.move_left_sprites.append(pygame.transform.flip(sprite, True, False))

        self.idle_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (1).png"), (64, 64)))
        self.idle_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (2).png"), (64, 64)))
        self.idle_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (3).png"), (64, 64)))
        self.idle_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (4).png"), (64, 64)))
        self.idle_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (5).png"), (64, 64)))
        self.idle_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (6).png"), (64, 64)))
        self.idle_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (7).png"), (64, 64)))
        self.idle_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (8).png"), (64, 64)))
        self.idle_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (9).png"), (64, 64)))
        self.idle_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (10).png"), (64, 64)))
        for sprite in self.idle_right_sprites:
            self.idle_left_sprites.append(pygame.transform.flip(sprite, True, False))

        self.jump_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (1).png"), (64, 64)))
        self.jump_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (2).png"), (64, 64)))
        self.jump_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (3).png"), (64, 64)))
        self.jump_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (4).png"), (64, 64)))
        self.jump_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (5).png"), (64, 64)))
        self.jump_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (6).png"), (64, 64)))
        self.jump_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (7).png"), (64, 64)))
        self.jump_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (8).png"), (64, 64)))
        self.jump_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (9).png"), (64, 64)))
        self.jump_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (10).png"), (64, 64)))
        for sprite in self.jump_right_sprites:
            self.jump_left_sprites.append(pygame.transform.flip(sprite, True, False))

        self.attack_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (1).png"), (64, 64)))
        self.attack_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (2).png"), (64, 64)))
        self.attack_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (3).png"), (64, 64)))
        self.attack_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (4).png"), (64, 64)))
        self.attack_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (5).png"), (64, 64)))
        self.attack_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (6).png"), (64, 64)))
        self.attack_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (7).png"), (64, 64)))
        self.attack_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (8).png"), (64, 64)))
        self.attack_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (9).png"), (64, 64)))
        self.attack_right_sprites.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (10).png"), (64, 64)))
        for sprite in self.attack_right_sprites:
            self.attack_left_sprites.append(pygame.transform.flip(sprite, True, False))

        self.current_sprite = 0
        self.image = self.idle_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        self.platform_group = platform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group

        self.animate_jump = False
        self.animate_fire = False

        self.jump_sound = pygame.mixer.Sound("sounds/jump_sound.wav")
        self.slash_sound = pygame.mixer.Sound("sounds/slash_sound.wav")
        self.portal_sound = pygame.mixer.Sound("sounds/portal_sound.wav")
        self.hit_sound = pygame.mixer.Sound("sounds/player_hit.wav")

        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        self.health = self.STARTING_HEALTH
        self.starting_x = x
        self.starting_y = y

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


class RubyMaker(pygame.sprite.Sprite):
    def __init__(self, x, y, main_group):
        super().__init__()

        self.ruby_sprites = []
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("images/ruby/tile000.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("images/ruby/tile001.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("images/ruby/tile002.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("images/ruby/tile003.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("images/ruby/tile004.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("images/ruby/tile005.png"), (64, 64)))

        self.current_sprite = 0

        self.image = self.ruby_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        main_group.add(self)

    def update(self):
        self.animate(self.ruby_sprites, 0.25)

    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]


class Ruby(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pass

    def update(self):
        pass

    def check_collisions(self):
        pass

    def move(self):
        pass

    def animate(self):
        pass


class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y, color, portal_group):
        super().__init__()

        self.portal_sprites = []

        if color == "green":
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile000.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile001.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile002.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile003.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile004.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile005.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile006.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile007.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile008.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile009.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile010.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile011.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile012.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile013.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile014.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile015.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile016.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile017.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile018.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile019.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile020.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile021.png"),
                                                              (72, 72)))


        elif color == "purple":
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile000.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile001.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile002.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile003.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile004.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile005.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile006.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile007.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile008.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile009.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile010.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile011.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile012.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile013.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile014.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile015.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile016.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile017.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile018.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile019.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile020.png"),
                                                              (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile021.png"),
                                                              (72, 72)))

        self.current_sprite = random.randint(0, len(self.portal_sprites) - 1)
        self.image = self.portal_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        portal_group.add(self)

    def update(self):
        self.animate(self.portal_sprites, 0.25)

    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]


my_main_tile_group = pygame.sprite.Group()
my_platform_group = pygame.sprite.Group()

my_player_group = pygame.sprite.Group()
my_bullet_group = pygame.sprite.Group()

my_zombie_group = pygame.sprite.Group()

my_portal_group = pygame.sprite.Group()
my_ruby_group = pygame.sprite.Group()

tile_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     8, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
     4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4,
     4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
     4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     7, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
     2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1]
]

# Loop through the 23 lists (rows) in the tile map (i moves us down the map)
for i in range(len(tile_map)):
    # Loop through the 40 elements in a given list (cols) (j moves us across the map)
    for j in range(len(tile_map[i])):
        # Dirt tiles
        if tile_map[i][j] == 1:
            Tile(j * 32, i * 32, 1, my_main_tile_group)
        # Platform tiles
        elif tile_map[i][j] == 2:
            Tile(j * 32, i * 32, 2, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 3:
            Tile(j * 32, i * 32, 3, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 4:
            Tile(j * 32, i * 32, 4, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 5:
            Tile(j * 32, i * 32, 5, my_main_tile_group, my_platform_group)
        # Ruby Maker
        elif tile_map[i][j] == 6:
            RubyMaker(j * 32, i * 32, my_main_tile_group)
        # Portals
        elif tile_map[i][j] == 7:
            Portal(j * 32, i * 32, "green", my_portal_group)
        elif tile_map[i][j] == 8:
            Portal(j * 32, i * 32, "purple", my_portal_group)
        # Player
        elif tile_map[i][j] == 9:
            my_player = Player(j * 32, i * 32, my_platform_group, my_portal_group, my_bullet_group)
            my_player_group.add(my_player)

background_image = pygame.transform.scale(pygame.image.load("images/background.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

my_game = Game()

# Main loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(background_image, background_rect)

    # Draw
    my_main_tile_group.update()
    my_main_tile_group.draw(display_surface)

    my_portal_group.update()
    my_portal_group.draw(display_surface)

    my_player_group.update()
    my_player_group.draw(display_surface)

    my_game.update()
    my_game.draw()

    # Update
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
