# Lesson: Keyboard Input in Pygame

In this lesson, students will learn how to handle keyboard input in Pygame. We will cover:
- Detecting when a key is pressed or released.
- Moving an object with the arrow keys.
- Handling multiple keys at once.
- Displaying instructions on the screen.

---

## **1. Introduction to Keyboard Input**
- Pygame detects keyboard input using `pygame.KEYDOWN` and `pygame.KEYUP` events.
- Each key has a unique constant (e.g., `pygame.K_LEFT` for the left arrow key).

---

## **2. Example Code: Moving a Square with Arrow Keys**
This example moves a square around the screen using arrow keys and displays instructions.

```python
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

# Define font
font = pygame.font.Font(None, 30)

# Define player properties
player_size = 50
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT // 2 - player_size // 2
player_speed = 5

# Main loop
running = True
while running:
    pygame.time.delay(30)  # Control game speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    # Prevent player from moving out of bounds
    player_x = max(0, min(SCREEN_WIDTH - player_size, player_x))
    player_y = max(0, min(SCREEN_HEIGHT - player_size, player_y))

    # Drawing everything
    SCREEN.fill(WHITE)  # Clear screen
    pygame.draw.rect(SCREEN, BLUE, (player_x, player_y, player_size, player_size))  # Draw player

    # Display instructions
    instructions = font.render("Use arrow keys to move the square", True, BLACK)
    SCREEN.blit(instructions, (SCREEN_WIDTH // 2 - instructions.get_width() // 2, 20))

    pygame.display.update()  # Update display

pygame.quit()
```

---

## **3. Concepts Covered**
✅ **Listening for Key Presses**  
   - Using `pygame.key.get_pressed()` to check if a key is being held down.  

✅ **Moving an Object**  
   - Updating `player_x` and `player_y` based on key input.  
   - Using `max()` and `min()` to keep the square inside the screen.  

✅ **Displaying Text on the Screen**  
   - Using `pygame.font.Font()` to create and display text.  
   - Positioning text at the top center of the screen.