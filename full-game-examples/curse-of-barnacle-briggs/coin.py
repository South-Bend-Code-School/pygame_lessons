import pygame
import random
from animated_sprite import AnimatedSprite
from constants import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT


class Coin:
    """
    Represents a collectible coin in the game.

    Each coin has a random type (gold, ruby, or silver) and is initialized
    at a specific position. The class uses shared images and sound effects
    for efficiency.
    """

    # Class-level attributes for shared resources
    # These are loaded only once and shared by all Coin instances.

    # Images for coin types
    gold_image = pygame.image.load("images/coin-gold.png")
    ruby_image = pygame.image.load("images/coin-ruby.png")
    silver_image = pygame.image.load("images/coin-silver.png")

    # Sound effect for coin collection
    coin_sound = pygame.mixer.Sound("sounds/coin-pickup.wav")

    def __init__(self):
        """
        Initialize a new coin at a random position.
        """
        # Randomly select the type of coin
        coin_type = random.randint(1, 3)  # Randomly pick 1, 2, or 3

        # Assign the appropriate sprite based on the coin type
        if coin_type == 1:
            self.sprite = AnimatedSprite(Coin.gold_image, frame_width=16)
        elif coin_type == 2:
            self.sprite = AnimatedSprite(Coin.ruby_image, frame_width=16)
        else:  # coin_type == 3
            self.sprite = AnimatedSprite(Coin.silver_image, frame_width=16)

        # The spawn position for the coin
        x = SCREEN_WIDTH + random.randint(0, 16)  # Spawn off-screen to the right
        y = random.randint(0, SCREEN_HEIGHT)  # Random vertical position

        # Position and size of the coin
        self.rect = pygame.Rect(x, y, 16, 16)

        # Movement speed (matches the background speed for a stationary illusion)
        self.movement_speed = 2

    def move(self):
        """
        Update the coins's position by moving it to the left.
        """
        self.rect.x -= self.movement_speed

    def draw(self):
        """
        Draw the enemy's current frame
        """
        coin_frame = self.sprite.get_frame()
        SCREEN.blit(coin_frame, self.rect.topleft)