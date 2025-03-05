import pygame  # Import the pygame library

# Initialize Pygame
pygame.init()

# Game Window Settings
SCREEN_WIDTH = 800  # Width of the game window
SCREEN_HEIGHT = 600  # Height of the game window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create the game window
pygame.display.set_caption("Animated Sprite")  # Set the window title

# Import the time module.
# We will track how long each frame has been on the screen to control the animation speed.
import time

class AnimatedSprite:
    def __init__(self, image, frame_width, animation_speed_ms=150):
        """
        Initialize the animated sprite.

        Parameters:
        - image: A pygame Surface object representing the sprite sheet.
        - frame_width: The width of each animation frame in pixels.
        - animation_speed_ms: The duration each frame is displayed (in milliseconds).
        """
        self.sprite_sheet = image
        self.frame_width = frame_width
        self.animation_speed_ms = animation_speed_ms

        # Calculate frame dimensions
        self.frame_height = self.sprite_sheet.get_height()
        self.frame_count = self.sprite_sheet.get_width() // frame_width
        self.current_frame = 0

        # Time tracking
        self.last_update_time = time.time()

    def get_frame(self):
        """
        Extract the current animation frame.
        """
        current_time = time.time()
        elapsed_time_ms = (current_time - self.last_update_time) * 1000

        if elapsed_time_ms >= self.animation_speed_ms:
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.last_update_time = current_time

        # Extract the frame from the sprite sheet
        x = self.current_frame * self.frame_width
        frame = self.sprite_sheet.subsurface((x, 0, self.frame_width, self.frame_height))
        return frame

    def is_last_frame(self):
        """
        Returns True if the current frame is the last in the animation sequence.
        """
        return self.current_frame == self.frame_count - 1

    def reset_animation(self):
        """
        Resets the animation to the first frame.
        """
        self.current_frame = 0

# Game Clock
clock = pygame.time.Clock()
FPS = 60  # Frames per second

# Game Loop Flag
running = True

# Load our sprite sheet as an image
coin_img = pygame.image.load("coin-gold.png")

# Create a new instance of our AnimatedSprite
animated_coin = AnimatedSprite(image=coin_img, frame_width=16, animation_speed_ms= 100)

# Game Loop
while running:
    clock.tick(FPS)  # Control the frame rate
    
    # Handle Exit Game Events (e.g., Close the Window or Press Escape)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the player closes the game window
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    
    # Create a white background
    SCREEN.fill(pygame.Color(0,0,0))  # Clear the screen with white

    # Get the postiion of the mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Get the current frame we want to draw
    coin_frame = animated_coin.get_frame()

    # Draw the coin onto our SCREEN buffer
    SCREEN.blit(coin_frame,(mouse_x-16,mouse_y-16))
    
    # flip the buffer to the front 
    pygame.display.flip()  # Update the screen


# Quit Pygame when the loop ends
pygame.quit()