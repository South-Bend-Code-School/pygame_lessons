"""
My Awesome Game - Starter 2D Game Template
Author: [Your Name]

Description:
This is a simple 2D game template using Pygame. It provides a basic game loop, 
player movement using arrow keys, and a simple boundary system to keep the player on screen.

Game Controls:
- Arrow Keys: Move the player (blue square) around the screen.
- Close Button: Exit the game.

This template is a great starting point for building your own game!
"""

import pygame  # Import the pygame library

# Initialize Pygame
pygame.init()

# Game Window Settings
SCREEN_WIDTH = 800  # Width of the game window
SCREEN_HEIGHT = 600  # Height of the game window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create the game window
pygame.display.set_caption("My Awesome Game")  # Set the window title

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

# Game Clock
clock = pygame.time.Clock()
FPS = 60  # Frames per second

# Player Settings
player_size = 50  # Square size of the player
player_x = SCREEN_WIDTH // 2  # Start in the middle of the screen
player_y = SCREEN_HEIGHT // 2
player_speed = 5  # How fast the player moves

# Game Loop Flag
running = True

# Game Loop
while running:
    clock.tick(FPS)  # Control the frame rate
    
    # Handle Events (e.g., Keyboard Input, Quitting the Game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the player closes the game window
            running = False
    
    # Get Key Presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed  # Move left
    if keys[pygame.K_RIGHT]:
        player_x += player_speed  # Move right
    if keys[pygame.K_UP]:
        player_y -= player_speed  # Move up
    if keys[pygame.K_DOWN]:
        player_y += player_speed  # Move down
    
    # Keep Player in Bounds
    player_x = max(0, min(SCREEN_WIDTH - player_size, player_x))
    player_y = max(0, min(SCREEN_HEIGHT - player_size, player_y))
    
    # Draw Everything
    SCREEN.fill(WHITE)  # Clear the screen
    pygame.draw.rect(SCREEN, BLUE, (player_x, player_y, player_size, player_size))  # Draw the player
    
    pygame.display.flip()  # Update the screen

# Quit Pygame when the loop ends
pygame.quit()