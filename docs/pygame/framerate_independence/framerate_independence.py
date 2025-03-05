import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (30, 30, 30)
SQUARE_COLOR = (0, 255, 0)
FPS_COLOR = (255, 255, 255)
TEXT_COLOR = (255, 255, 255)

# Set FPS (Change this value to 15, 30, or 60 to adjust FPS)
TARGET_FPS = 30

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spinning Square with FPS Counter")

# Clock for FPS control
clock = pygame.time.Clock()

# Square properties
square_size = 100
square_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
angle = 0
rotation_speed = 90  # Degrees per second

# Load a monospaced font for consistent number heights
font = pygame.font.Font(pygame.font.match_font('courier', bold=True), 20)

# Instructions
instructions = [
    "Controls:",
    "Up Arrow - Increase Rotation Speed",
    "Down Arrow - Decrease Rotation Speed",
    "Right Arrow - Increase FPS",
    "Left Arrow - Decrease FPS",
    "ESC - Quit"
]

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rotation_speed += 10
            elif event.key == pygame.K_DOWN:
                rotation_speed = max(10, rotation_speed - 10)
            elif event.key == pygame.K_RIGHT:
                TARGET_FPS = min(60, TARGET_FPS + 10)
            elif event.key == pygame.K_LEFT:
                TARGET_FPS = max(10, TARGET_FPS - 10)
            elif event.key == pygame.K_ESCAPE:
                running = False

    # Clear screen
    screen.fill(BACKGROUND_COLOR)
    
    # Get delta time (time since last frame in seconds)
    delta_time = clock.get_time() / 1000.0
    
    # Rotate square based on delta time
    angle += rotation_speed * delta_time  # Rotation speed is now time-based
    square_surface = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
    pygame.draw.rect(square_surface, SQUARE_COLOR, (0, 0, square_size, square_size))
    rotated_square = pygame.transform.rotate(square_surface, angle)
    rect = rotated_square.get_rect(center=square_center)
    
    # Draw rotated square
    screen.blit(rotated_square, rect.topleft)
    
    # Display FPS
    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, FPS_COLOR)
    screen.blit(fps_text, (SCREEN_WIDTH - 100, 10))
    
    # Display rotation speed below the spinning square
    speed_text = font.render(f"Rotation Speed: {rotation_speed}°/s", True, TEXT_COLOR)
    fps_target_text = font.render(f"Target FPS Speed: {TARGET_FPS}", True, TEXT_COLOR)
    screen.blit(speed_text, (square_center[0] - speed_text.get_width() // 2, square_center[1] + square_size // 2 + 30))
    screen.blit(fps_target_text, (square_center[0] - speed_text.get_width() // 2, square_center[1] + square_size // 2 + 60))
    
    # Display instructions
    y_offset = 50
    for line in instructions:
        text_surface = font.render(line, True, TEXT_COLOR)
        screen.blit(text_surface, (10, y_offset))
        y_offset += 30
    
    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(TARGET_FPS)

pygame.quit()
sys.exit()