import pygame
pygame.init()

import random
from player import Player
from enemy import Enemy
from coin import Coin
from constants import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT

pygame.display.set_caption("The Curse of Barnacle Briggs")

# Load a font to display the highscore
font = pygame.font.Font(None, 36)  # Use default font, size 36

# Load the sound file (supports .ogg and .wav formats)
background_music = pygame.mixer.Sound("sounds/background-music.mp3")  # Replace with "background.wav" if using .wav
background_music.play(loops=-1)  # -1 makes the music loops indefinitely
background_music.set_volume(0.25)

# Load background assets
far_bg = pygame.image.load("images/background-distant.png")
sand_bg = pygame.image.load("images/background-sand.png")

# Parallax background positions and speeds
far_x, sand_x = 0, 0
far_speed = 1
sand_speed = 2

# Create our player character
player = Player(x=20, y=50, movement_speed=3)

# Initialize empty enemies list
enemies = []

# Initialize emply coins list
coins = []
coins_collected = 0
time_since_last_coin_spawn = 0

# Timers and spawn settings
time_since_last_enemy_spawn = 0
enemy_spawn_interval = 2000  # Initial interval between enemy spawns in milliseconds
minimum_spawn_interval = 100  # Minimum possible spawn interval

# Game clock
clock = pygame.time.Clock()

def update_background():
    """
    Update and render the scrolling parallax background.
    """
    global far_x, sand_x

    # Update background positions
    far_x -= far_speed
    sand_x -= sand_speed

    # Reset positions for seamless scrolling
    if far_x <= -far_bg.get_width():
        far_x = 0
    if sand_x <= -sand_bg.get_width():
        sand_x = 0

    # Draw background layers
    SCREEN.blit(far_bg, (far_x, 0))
    SCREEN.blit(far_bg, (far_x + far_bg.get_width(), 0))

    SCREEN.blit(sand_bg, (sand_x, 0))
    SCREEN.blit(sand_bg, (sand_x + sand_bg.get_width(), 0))


# Game loop
alive = True
while alive:
    dt = clock.tick(60)  # Time since last frame in milliseconds

    # The pygame.QUIT event is triggered when the user clicks the close button or attempts to close the window in another way.
    # If you don’t handle this event, the window will remain open, and you might need to force-quit the program.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False

    # Draw background    
    update_background()

    # Manage Player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move("up")
    if keys[pygame.K_DOWN]:
        player.move("down")
    if keys[pygame.K_LEFT]:
        player.move("left")
    if keys[pygame.K_RIGHT]:
        player.move("right")
    
    player.update_state()

    # Draw the player
    player.draw()

    # Manage Coins
    for coin in coins.copy():
        coin.move()
        coin.draw()
        if player.rect.colliderect(coin.rect):
            Coin.coin_sound.play()
            coins_collected = coins_collected + 1
            coins.remove(coin)

    # Draw the enemys
    for enemy in enemies.copy():

        # Move the enemy
        enemy.move()

        # Update the enemy's state (if it's dead or off the screen)
        enemy.update_state()

        # Handle collisions only for active enemies
        if enemy.state == "active" and player.rect.colliderect(enemy.rect):
            player.handle_collision()  # Handle collision effects for the player
            enemy.handle_collision() # Handle collision for the enemy (set the state to dying)

        # Draw the enemy (based on it's state)
        enemy.draw()

        # Remove enemies that are in found in the "dead" state. 
        # This will stop them from being drawn in the future.
        if enemy.state == "dead":
            enemies.remove(enemy)






    # Spawn enemy
    # Define spawn interval range
    SPAWN_INTERVAL_MIN = 300 
    SPAWN_INTERVAL_MAX = 1000

    # Variable to store the current spawn interval
    current_spawn_interval = random.randint(SPAWN_INTERVAL_MIN, SPAWN_INTERVAL_MAX)

    # Update time since last enemy spawn
    time_since_last_enemy_spawn += dt  # 60 frames per second.

    # Check if it's time to spawn a new enemy
    if time_since_last_enemy_spawn >= current_spawn_interval:
        time_since_last_enemy_spawn = 0
        current_spawn_interval = random.randint(SPAWN_INTERVAL_MIN, SPAWN_INTERVAL_MAX)  # Reset interval
        new_enemy = Enemy()
        enemies.append(new_enemy)






    
    # Spawn coin
    time_since_last_coin_spawn += dt
    if time_since_last_coin_spawn >= random.randint(100, 1000):
        time_since_last_coin_spawn = 0
        new_coin = Coin()
        coins.append(new_coin)
        
    # Draw Collision Rectangles
    draw_collision_rect=False
    if draw_collision_rect:
        pygame.draw.rect(SCREEN, (255, 0, 0), player.rect, 1)  # Red for debugging

    # Draw Score
    score_surface = font.render(f"Lives: {player.lives}  Coins: {coins_collected}", True, (255, 255, 255))
    # Draw the text on the screen at position (10, 10)
    SCREEN.blit(score_surface, (10, 10))

    # End the game if the player is out of lives
    if player.lives <= 0:
        alive = False

    # Update display
    pygame.display.flip()

def game_over_screen():
    skull = pygame.image.load("images/skull.png")
    black_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    black_surface.fill((0,0,0))

    while True:

        # Draw the fade surface
        SCREEN.blit(black_surface, (0, 0))
        # Draw Skull and Game Over text
        SCREEN.blit(skull, (128, 0))  # Adjust position for center alignment
        game_over_surface = font.render("Game Over!!", True, (255,255,255))
        SCREEN.blit(game_over_surface, (190, 245))  # Adjust position as needed

        pygame.display.flip()

        # Handle events (e.g., quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

game_over_screen()   

pygame.quit()