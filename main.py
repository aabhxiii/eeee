import pygame
import sys # TO USE sys IMPORT IT 
import random # TO USE random IMPORT IT

# Game Constants
SCREEN_WIDTH = 640 # USE CAPITAL LETTER FOR THE CONSTANTS
SCREEN_HEIGHT = 480 # THAT DO NOT CHANGE THROUGHT THE PROGRAM EXECUTION
PLAYER_SIZE = 50
ENEMY_SIZE = 50

# Game Settings
player_pos = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
enemy_pos = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]
running = True # variable for declaring the state of the game 

# Pygame initialize
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5

    # Collision detection
    if (player_pos[0] < enemy_pos[0] + ENEMY_SIZE and
        player_pos[0] + PLAYER_SIZE > enemy_pos[0] and
        player_pos[1] < enemy_pos[1] + ENEMY_SIZE and
        player_pos[1] + PLAYER_SIZE > enemy_pos[1]):
        running = False # terminate the loop and end the game
        print("GAME OVER!")

    # Screen update
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, (0, 255, 0), (enemy_pos[0], enemy_pos[1], ENEMY_SIZE, ENEMY_SIZE))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
