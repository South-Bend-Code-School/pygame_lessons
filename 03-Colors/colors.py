import pygame

# Initialize Pygame
pygame.init()

# Set up screen
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RGB Color Mixer")

# Define initial RGB values
red = 255
green = 100
blue = 50

# Define circle radius
CIRCLE_RADIUS = 60

# Set font for displaying RGB values
font = pygame.font.Font(None, 24)
font_bold = pygame.font.Font(None, 28)

# Game loop
running = True
while running:
    SCREEN.fill((255, 255, 255))  # Clear screen with white background
    
    # Get the state of modifier keys
    keys = pygame.key.get_pressed()
    shift_pressed = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if shift_pressed:
                    red = min(255, red + 10)  # Increase red
                else:
                    red = max(0, red - 10)  # Decrease red
            elif event.key == pygame.K_g:
                if shift_pressed:
                    green = min(255, green + 10)  # Increase green
                else:
                    green = max(0, green - 10)  # Decrease green
            elif event.key == pygame.K_b:
                if shift_pressed:
                    blue = min(255, blue + 10)  # Increase blue
                else:
                    blue = max(0, blue - 10)  # Decrease blue
            elif event.key == pygame.K_ESCAPE:
                running = False
    
    # Draw RGB component circles
    pygame.draw.circle(SCREEN, (red, 0, 0), (200, 200), CIRCLE_RADIUS)
    pygame.draw.circle(SCREEN, (0, green, 0), (350, 200), CIRCLE_RADIUS)
    pygame.draw.circle(SCREEN, (0, 0, blue), (500, 200), CIRCLE_RADIUS)
    pygame.draw.circle(SCREEN, (red, green, blue), (650, 200), CIRCLE_RADIUS)
    
    # Draw plus and equals signs
    plus_text1 = font_bold.render("+", True, (0, 0, 0))
    plus_text2 = font_bold.render("+", True, (0, 0, 0))
    equals_text = font_bold.render("=", True, (0, 0, 0))
    SCREEN.blit(plus_text1, (270, 190))
    SCREEN.blit(plus_text2, (420, 190))
    SCREEN.blit(equals_text, (570, 190))
    
    # Render color labels centered below circles
    red_text = font.render("Red", True, (255, 0, 0))
    green_text = font.render("Green", True, (0, 255, 0))
    blue_text = font.render("Blue", True, (0, 0, 255))
    final_color_text = font.render("Final Color", True, (red, green, blue))
    
    SCREEN.blit(red_text, (200 - red_text.get_width() // 2, 280))
    SCREEN.blit(green_text, (350 - green_text.get_width() // 2, 280))
    SCREEN.blit(blue_text, (500 - blue_text.get_width() // 2, 280))
    SCREEN.blit(final_color_text, (650 - final_color_text.get_width() // 2, 280))
    
    # Render RGB values inside each circle
    red_value = font.render(str(red), True, (255, 255, 255))
    green_value = font.render(str(green), True, (255, 255, 255))
    blue_value = font.render(str(blue), True, (255, 255, 255))
    final_value = font.render(f"({red}, {green}, {blue})", True, (255, 255, 255))
    
    SCREEN.blit(red_value, (200 - red_value.get_width() // 2, 190))
    SCREEN.blit(green_value, (350 - green_value.get_width() // 2, 190))
    SCREEN.blit(blue_value, (500 - blue_value.get_width() // 2, 190))
    SCREEN.blit(final_value, (650 - final_value.get_width() // 2, 190))
    
    # Render instructions
    instructions = [
        "Press R to decrease Red, Shift+R to increase Red",
        "Press G to decrease Green, Shift+G to increase Green",
        "Press B to decrease Blue, Shift+B to increase Blue"
    ]
    y_offset = 20
    for line in instructions:
        text_surface = font.render(line, True, (0, 0, 0))
        SCREEN.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, y_offset))
        y_offset += 25
    
    # Update the display
    pygame.display.flip()
    
# Quit Pygame
pygame.quit()