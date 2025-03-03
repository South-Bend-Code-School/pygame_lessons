import pygame

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Keyboard Input Example")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Define font
font = pygame.font.SysFont("Arial", 10, bold=True)  # Decreased font size

# Define player properties
player_size = 50
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT // 2 - player_size // 2
player_speed = 5

def draw_grid():
    """Draws a grid on the background."""
    for x in range(0, SCREEN_WIDTH, 50):
        pygame.draw.line(SCREEN, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, 50):
        pygame.draw.line(SCREEN, GRAY, (0, y), (SCREEN_WIDTH, y))

# Main loop
running = True
while running:
    pygame.time.delay(30)  # Control game speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:  # Increase speed
                player_speed += 1
            elif event.key == pygame.K_MINUS or event.key == pygame.K_UNDERSCORE:  # Decrease speed
                player_speed = max(1, player_speed - 1)

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Move the player based on key input
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    
    # Quit if the player pressed escape
    if keys[pygame.K_ESCAPE]:
        running = False

    # Prevent player from moving out of bounds
    player_x = max(0, min(SCREEN_WIDTH - player_size, player_x))
    player_y = max(0, min(SCREEN_HEIGHT - player_size, player_y))

    # Drawing everything
    SCREEN.fill(WHITE)  # Clear screen
    draw_grid()  # Draw grid
    pygame.draw.rect(SCREEN, BLUE, (player_x, player_y, player_size, player_size))  # Draw player

    # Display instructions
    instructions = font.render("Use arrow keys to move the square | + / - to adjust speed", True, BLACK)
    SCREEN.blit(instructions, (SCREEN_WIDTH // 2 - instructions.get_width() // 2, 20))
    
    # Display player coordinates centered in the square
    coord_text = font.render(f"({player_x}, {player_y})", True, WHITE)
    coord_rect = coord_text.get_rect()
    coord_rect.center = (player_x + player_size // 2, player_y + player_size // 2)
    SCREEN.blit(coord_text, coord_rect.topleft)

    # Display player speed on the screen
    speed_text = font.render(f"Speed: {player_speed}", True, BLACK)
    SCREEN.blit(speed_text, (20, SCREEN_HEIGHT - 40))

    pygame.display.update()  # Update display

pygame.quit()