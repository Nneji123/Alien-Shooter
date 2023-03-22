"""A space invader game created using Pygame
"""
import pygame
from pygame import mixer
import random
import math


# Initialize the game engine
pygame.init()

#create the screen
screen = pygame.display.set_mode([800,600])

# Background image
background = pygame.image.load('assets/background.png')

#Background Sound
mixer.music.load('assets/sfx.mp3')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Alien Shooter")
icon = pygame.image.load('assets/player.png')
pygame.display.set_icon(icon)

# create a new font object
watermark_font = pygame.font.Font(None, 20)
# render the text onto a surface
watermark_text = watermark_font.render("Made by Ifeanyi Nneji", True, (255, 255, 255))
# blit the watermark onto the screen


# Player Image
playerImg = pygame.image.load('assets/player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy Image

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5
for _ in range(num_of_enemies):
    enemyImg.append(pygame.image.load('assets/alien.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# Bullet Image
bulletImg = pygame.image.load('assets/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0.3
bulletY_change = 1
bullet_state = 'ready'


# Score
score_value = 0
font = pygame.font.Font('assets/SPACEBOY.ttf', 32)

textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font('assets/SPACEBOY.ttf', 64)



def show_score(x,y):
    score = font.render(f"Score:{str(score_value)}", True, (255,255,255))
    screen.blit(score,(x,y))
    screen.blit(watermark_text, (screen.get_width() - watermark_text.get_width() - 10, 10))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (160,250))

def player(x, y):
    screen.blit(playerImg,(x,y))

def enemy(x, y, i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 13))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + (math.pow(enemyY-bulletY,2)))
    return distance < 27


# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletSound = mixer.Sound("assets/laser.mp3")
                bulletSound.play()
                # Get the current x cordinate of the spaceship
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP and event.key in [
            pygame.K_LEFT,
            pygame.K_RIGHT,
        ]:
            playerX_change = 0


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.7
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.7
            enemyY[i] += enemyY_change[i]

        if collision := isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            explosionSound = mixer.Sound("assets/explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

