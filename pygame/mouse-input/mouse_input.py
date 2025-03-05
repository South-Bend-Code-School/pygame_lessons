import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mouse Painting with Instructions")

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Default circle color
circle_color = BLUE

# Background surface to store drawn circles
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.fill(WHITE)

# Font setup
font = pygame.font.Font(None, 24)  # Default pygame font

# Track mouse position
mouse_x, mouse_y = pygame.mouse.get_pos()

# Track if mouse is being held down
mouse_held = False  

# Game loop
running = True
while running:
    SCREEN.blit(background, (0, 0))  # Redraw the saved background

    # Track mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Start drawing on click
            mouse_held = True
            pygame.draw.circle(background, circle_color, (mouse_x, mouse_y), 10)
        elif event.type == pygame.MOUSEBUTTONUP:  # Stop drawing when released
            mouse_held = False
        elif event.type == pygame.MOUSEMOTION and mouse_held:  # Draw while dragging
            pygame.draw.circle(background, circle_color, (mouse_x, mouse_y), 10)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Clear screen
                background.fill(WHITE)
            elif event.key == pygame.K_c:  # Change to random color
                circle_color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
            elif event.key == pygame.K_ESCAPE: # Quit
                running = False

    # Draw a circle under the mouse cursor
    pygame.draw.circle(SCREEN, circle_color, (mouse_x, mouse_y), 10)

    # Display instructions
    instructions = [
        "Click to draw circles",
        "Hold & drag to paint",
        "Press SPACE to clear the screen",
        "Press C to change color",
        f"Current Color: RGB{circle_color}",
    ]
    
    for i, text in enumerate(instructions):
        instruction_surface = font.render(text, True, BLACK)
        SCREEN.blit(instruction_surface, (10, 10 + i * 25))  # Offset each line

    pygame.display.flip()  # Update the screen

# Quit pygame
pygame.quit()