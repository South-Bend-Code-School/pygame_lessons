import pygame

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Drawing Shapes in Pygame")

# Define constants for a few colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (175, 175, 150)

# Initialize font
pygame.font.init()
FONT = pygame.font.SysFont("Arial", 12)  # Decreased font size

def draw_grid():
    """Draws a grid on the screen with labels at 50-pixel increments."""
    
    label = FONT.render("x,y=0,0", True, GRAY)
    SCREEN.blit(label, (2, 2))

    for x in range(50, SCREEN_WIDTH, 50):
        pygame.draw.line(SCREEN, GRAY, (x, 0), (x, SCREEN_HEIGHT), 1)
        label = FONT.render(f"x={x}", True, GRAY)
        SCREEN.blit(label, (x + 2, 2))
    
    for y in range(50, SCREEN_HEIGHT, 50):
        pygame.draw.line(SCREEN, GRAY, (0, y), (SCREEN_WIDTH, y), 1)
        label = FONT.render(f"y={y}", True, GRAY)
        SCREEN.blit(label, (2, y + 2))

# Game loop
running = True
while running:
    SCREEN.fill(WHITE)  # Fill the screen with a white background
    
    draw_grid()  # Draw the coordinate grid
    
    # Draw shapes
    pygame.draw.rect(SCREEN, RED, (50, 50, 200, 100))  # Draw a red rectangle at (50,50) with width 200 and height 100
    pygame.draw.circle(SCREEN, GREEN, (400, 300), 50)  # Draw a green circle centered at (400,300) with radius 50
    pygame.draw.line(SCREEN, BLUE, (100, 500), (700, 500), 5)  # Draw a blue line from (100,500) to (700,500) with thickness 5
    pygame.draw.polygon(SCREEN, BLACK, [(600, 100), (650, 200), (550, 200)])  # Draw a black triangle with points at (600,100), (650,200), (550,200)
    pygame.draw.ellipse(SCREEN, RED, (300, 400, 150, 80))  # Draw a red ellipse inside a bounding box at (300,400) with width 150 and height 80

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    
    pygame.display.flip()  # Update the display

# Quit Pygame
pygame.quit()