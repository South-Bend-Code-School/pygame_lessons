import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 200, 200
FPS = 60

# Create Screen and Clock
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class AnimatedSprite:
    def __init__(self, image, frame_width, animation_speed_ms=150):
        """
        Initialize the animated spritesheet.

        Parameters:
        - image: A pygame image object.
        - frame_width: Width of each frame in pixels.
        - animation_speed_ms: The animation speed in milliseconds (1000 ms = 1 second).
        """
        # Load the sprite sheet.
        self.sprite_sheet = image
        self.frame_width = frame_width
        self.animation_speed_ms = animation_speed_ms

        # Calculate dimensions and frames.
        self.frame_height = self.sprite_sheet.get_height()  # Assumes sprite sheets are organized horizontally.
        self.frame_count = self.sprite_sheet.get_width() // frame_width  # Integer division
        self.current_frame = 0  # Start at the first frame of the animation.

        # Time tracking.
        self.time_since_last_frame = 0  # Start with 0 elapsed time.

    def get_frame(self, dt):
        """
        Get the current frame as a surface and update the animation frame if enough time has passed.
        
        Parameters:
        - dt: The time elapsed (in seconds) since the last update.
        """
        self.time_since_last_frame += dt * 1000  # Convert seconds to milliseconds.

        if self.time_since_last_frame >= self.animation_speed_ms:
            # Advance to the next frame.
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.time_since_last_frame = 0  # Reset elapsed time.

        x = self.current_frame * self.frame_width
        frame = self.sprite_sheet.subsurface((x, 0, self.frame_width, self.frame_height))
        return frame

# Load our sprite sheet as an image
gold_coin_img = pygame.image.load("coin-gold.png")
ruby_coin_img = pygame.image.load("coin-ruby.png")

# Create a new instance of our AnimatedSprite
animated_gold_coin = AnimatedSprite(image=gold_coin_img, frame_width=16, animation_speed_ms=150)
animated_ruby_coin= AnimatedSprite(image=ruby_coin_img, frame_width=16, animation_speed_ms=50)

running = True
while running:
    dt = clock.tick(FPS) / 1000.0  # Convert to seconds
    
    # Handle Exit Game Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    
    # Clear the screen
    SCREEN.fill((0, 0, 0))
    
    # Slower Spinning Gold Coin
    gold_coin_frame = animated_gold_coin.get_frame(dt)
    SCREEN.blit(gold_coin_frame, (112, 92))
    
    # Faster Spinning Ruby Coint
    ruby_coin_frame = animated_ruby_coin.get_frame(dt)
    SCREEN.blit(ruby_coin_frame, (72, 92))

    pygame.display.flip()
    
pygame.quit()