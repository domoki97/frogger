import pygame
import random
from random import choice
from pygame.locals import *
from turtle import width
import pickle

try:
    with open('score.dat', 'rb') as file:
        score = pickle.load(file)
except:
    score = 0

high_score = "High score:  " + str(score)

WIDTH = 1098
HEIGHT = 1302
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

frog = pygame.image.load('frog.png')
frog_h = 70
frog_w = 70
frog = pygame.transform.scale(frog, (frog_h, frog_w))

goal = pygame.image.load('goal.png')
goal = pygame.transform.scale(goal, (1302, 5))

bg = pygame.image.load('background.png')

car_left2 = pygame.image.load('car_left2.png')
car_right1 = pygame.image.load('car_right1.png')

log = pygame.image.load('log.png')

font = pygame.font.Font('freesansbold.ttf', 48)
text_rect = pygame.Rect(300, 0, 48, 300)

goal_rect = goal.get_rect()
goal_rect.x = 0
goal_rect.top = 0


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

high_score_text = font.render(str(high_score), True, WHITE)

pygame.key.set_repeat(1)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = frog
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.bottom = HEIGHT - 32
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if keystate[pygame.K_w]:
            self.speedy = -5
        if keystate[pygame.K_s]:
            self.speedy = 5
        self.rect.y += self.speedy
        if self.rect.bottom > 1302:
            self.rect.bottom = 1302
        if self.rect.top < 0:
            self.rect.top = 0


class Car_Left(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = car_left2
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = choice((700, 900, 1100))
        self.speedx = random.randrange(4, 12)

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left > WIDTH + 200:
            self.rect.x = -100
            self.rect.y = choice((700, 900, 1100))
            self.speedx = random.randrange(4, 12)


class Log_Left(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = log
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = choice((200, 400, 500))
        self.speedx = random.randrange(4, 12)

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left > WIDTH + 200:
            self.rect.x = -100
            self.rect.y = choice((200, 400, 500))
            self.speedx = random.randrange(4, 12)


class Car_Right(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = car_right1
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = choice((800, 1000))
        self.speedx = random.randrange(-12, -4)

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left < WIDTH - 1300:
            self.rect.x = 1200
            self.rect.y = choice((800, 1000))
            self.speedx = random.randrange(-12, -4)


class Log_Right(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = log
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = choice((100, 300))
        self.speedx = random.randrange(-12, -4)

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left < WIDTH - 1300:
            self.rect.x = 1200
            self.rect.y = choice((100, 300))
            self.speedx = random.randrange(-12, -4)


def main():

    sec = 0
    clock = pygame.time.Clock()


def show_go_screen():
    WIN.blit(bg, (0, 0))
    text_surface = font.render("Press any key to play", True, WHITE)
    WIN.blit(text_surface, (WIDTH / 2, HEIGHT * 7 / 8))
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


game_over = True
running = True
sec = 0
score = 0
while running:

    if game_over:
        show_go_screen()
        score = 0
        game_over = False
        all_sprites = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        enemy = pygame.sprite.Group()

        for i in range(6):
            c = Car_Left()
            all_sprites.add(c)
            enemy.add(c)

        for i in range(6):
            c = Log_Left()
            all_sprites.add(c)
            enemy.add(c)

        for i in range(6):
            c = Log_Right()
            all_sprites.add(c)
            enemy.add(c)

        for i in range(6):
            c = Car_Right()
            all_sprites.add(c)
            enemy.add(c)

    clock.tick(FPS)

    sec += 1
    if sec == 60:
        score += 1
        sec = 0
    score_text = font.render(str(score), True, WHITE)
    sct = score_text.get_rect()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, enemy, False)
    if hits:
        game_over = True

    if goal_rect.colliderect(player.rect):
        with open('score.dat', 'wb') as file:
            pickle.dump(score, file)
            game_over = True

    WIN.blit(bg, (0, 0))
    WIN.blit(goal, (goal_rect.x, goal_rect.top))
    WIN.blit(score_text, (1025, 25))
    # WIN.blit(high_score, (50, 25))
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()

if __name__ == '__main__':
    main()
