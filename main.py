import pygame
import random

# Initialize pygame
pygame.init()

# Vytvaranie screenu
screen = pygame.display.set_mode((1280, 960))

# Pozadie
pozadie = pygame.image.load("obrazky/pozadie.png")

# Nazov a ikona okna
pygame.display.set_caption("snudi")
ikona = pygame.image.load("obrazky\jaboss_ikona.png")
pygame.display.set_icon(ikona)

# Hrac
playerImg = pygame.image.load("obrazky\sadge.png")
playerX = 625
playerY = 800
playerX_change = 0

# Nepriatel
enemyImg = pygame.image.load("obrazky\megalul_enemy.png")
enemyX = random.randint(0, 1280)
enemyY = random.randint(20, 250)
enemyX_change = 3
enemyY_change = 65

def hrac():
    screen.blit(playerImg, (playerX, playerY))

def nepriatel():
    screen.blit(enemyImg, (enemyX, enemyY))

# Game Loop
running = True
while running:

    #RGB
    screen.fill((0, 0, 0))

    # Obrazok na pozadi
    screen.blit(pozadie, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pozera na to, ci je nieco stlacene a ci ideme dolava/doprava
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Zmena pohybu po osi X, hraca/nepriatela
    playerX += playerX_change
    enemyX += enemyX_change

    # Okraje okna (boundaries) pre hraca
    if playerX <= 0:
        playerX = 0

    elif playerX >= 1218:
        playerX = 1218

    # Nepriatelsky pohyb
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change

    elif enemyX >= 1218:
        enemyX_change = -3
        enemyY += enemyY_change


    hrac()
    nepriatel()
    pygame.display.update()
