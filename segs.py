import pygame

# Game ki setting
screen_width = 640
screen_height = 480
player_size = 50
player_pos = [screen_width/2, screen_height/2]
enemy_size = 50
enemy_pos = [random.randint(0, screen_width), random.randint(0, screen_height)]

# Pygame initialize
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

# Game loop
while True:
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
    if (player_pos[0] < enemy_pos[0] + enemy_size and
        player_pos[0] + player_size > enemy_pos[0] and
        player_pos[1] < enemy_pos[1] + enemy_size and
        player_pos[1] + player_size > enemy_pos[1]):
        print("Game over!")

    # Screen update
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, (0, 255, 0), (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
