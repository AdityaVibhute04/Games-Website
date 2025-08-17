import pygame 
from pygame.locals import *
import sys
from random import randint, choice

pygame.font.init()

screen_width = 1080
screen_height = 720
yPos1 = 360
yPos2 = 360
player_speed = 5

ball_speed_x = randint(3, 7) * choice([1, -1])
ball_speed_y = randint(3, 7) * choice([1, -1])

# Creating display
surface = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Pong')

# Drawings
ball = Rect(screen_width / 2, screen_height / 2, 7.5, 7.5)

font = pygame.font.SysFont('Courier', 18, 1, 1)

score1 = 0
score2 = 0

def static():
    global yPos1, yPos2, ball, ball_speed_x, ball_speed_y

    yPos1 = 360
    yPos2 = 360
    ball.x = screen_width / 2
    ball.y = screen_height / 2

    surface.fill((0, 0, 0))
    pygame.draw.line(surface, (255, 255, 255), (0, 60), (screen_width, 60), 2)
    pygame.draw.line(surface, (255, 255, 255), (screen_width / 2, 0), (screen_width / 2, screen_height), 2)
    pygame.draw.rect(surface, (255, 255, 255), [0, yPos1, 10, 70], 0)
    pygame.draw.rect(surface, (255, 255, 255), [1070, yPos2, 10, 70], 0)
    ball = pygame.draw.rect(surface, (255, 255, 255), [screen_width / 2, screen_height / 2, 7.5, 7.5], 0)
    scorePlayer1 = font.render(str(score1), True, (255, 255, 255))
    scorePlayer2 = font.render(str(score2), True, (255, 255, 255))
    welcome = font.render("Press SPACE to begin", True, (255, 255, 255))
    surface.blit(scorePlayer1, (screen_width / 2 - 60, 25))
    surface.blit(scorePlayer2, (screen_width / 2 + 50, 25))
    surface.blit(welcome, (screen_width / 2 - 42, screen_height / 2 - 200))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                waiting = False

    ball_speed_x = randint(3, 7) * choice([1, -1])
    ball_speed_y = randint(3, 7) * choice([1, -1])

pygame.init()
static()

running = True

# Main loop
while running:
    surface.fill((0, 0, 0))

    scorePlayer1 = font.render(str(score1), True, (255, 255, 255))
    scorePlayer2 = font.render(str(score2), True, (255, 255, 255))
    pygame.draw.line(surface, (255, 255, 255), (0, 60), (screen_width, 60), 2)
    pygame.draw.line(surface, (255, 255, 255), (screen_width / 2, 0), (screen_width / 2, screen_height), 2)
    player1 = pygame.draw.rect(surface, (255, 255, 255), [0, yPos1, 10, 70], 0)
    player2 = pygame.draw.rect(surface, (255, 255, 255), [1070, yPos2, 10, 70], 0)

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.left <= 0:
        score2 += 1
        static()

    if ball.right >= 1080:
        score1 += 1
        static()

    if ball.top <= 60 or ball.bottom >= (screen_height - 7.5):
        ball_speed_y *= -1

    surface.blit(scorePlayer1, (screen_width / 2 - 60, 25))
    surface.blit(scorePlayer2, (screen_width / 2 + 50, 25))

    pygame.draw.rect(surface, (255, 255, 255), ball)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and yPos1 > 60:
        yPos1 -= player_speed
    if keys[pygame.K_s] and yPos1 < screen_height - 70:
        yPos1 += player_speed

    if keys[pygame.K_UP] and yPos2 > 60:
        yPos2 -= player_speed
    if keys[pygame.K_DOWN] and yPos2 < screen_height - 70:
        yPos2 += player_speed

    if ball.colliderect(pygame.Rect(0, yPos1, 10, 70)):
        ball_speed_x *= -1

    if ball.colliderect(pygame.Rect(1070, yPos2, 10, 70)):
        ball_speed_x *= -1

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

        

