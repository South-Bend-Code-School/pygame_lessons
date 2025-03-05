import pygame
import random
from animated_sprite import AnimatedSprite
from constants import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT


class Enemy:
    enemy_fish_image = pygame.image.load("images/enemy-fish.png")
    enemy_fish_hit_image = pygame.image.load("images/fx-hit.png")

    def __init__(self, movement_speed=4):
        """
        Initialize an Enemy object.

        The Enemy spawns off-screen to the right at a random vertical position
        and moves toward the left. It uses a rectangle (`rect`) to represent
        its position and size for collision detection and rendering.

        Parameters:
        - movement_speed (int): The horizontal movement speed of the enemy.
          Defaults to 4, meaning the enemy moves 4 pixels per frame.
        """
        # The frame_width of our enmey is a constant
        self.frame_width = 48
        self.sprite = AnimatedSprite(Enemy.enemy_fish_image, frame_width=48, animation_speed_ms=100)
        self.sprite_hit = AnimatedSprite(Enemy.enemy_fish_hit_image, frame_width=52, animation_speed_ms=150)

        # The spawn position for the enemy
        x = SCREEN_WIDTH + random.randint(0, 15)  # Spawn off-screen to the right
        y = random.randint(0, SCREEN_HEIGHT)  # Random vertical position

        # The rectangle representing the enemy's position and size
        # Used for:
        # - Collision detection
        # - Tracking position for movement and rendering
        self.rect = pygame.Rect(x, y, self.frame_width, self.sprite.frame_height)

        # Horizontal speed of the enemy (pixels per frame)
        self.movement_speed = movement_speed

        # Track enemy states
        self.state = "active"  # Possible states: "active", "dead", "done"

    def move(self):
        """
        Update the enemy's position by moving it to the left.
        """
        self.rect.x -= self.movement_speed

    def update_state(self):
        if self.rect.right < 0: 
            self.state = "dead"

        if self.state == "dying" and self.sprite_hit.is_last_frame():
            self.state = "dead"

    def draw(self):
        """
        Draw the enemy's current frame on the global screen.
        """
        # Draw the enemy fish
        frame = self.sprite.get_frame()
        SCREEN.blit(frame, self.rect.topleft)

        # If dying, draw the hit impact effect on top of the fish.
        if self.state == "dying":
            frame = self.sprite_hit.get_frame()
            SCREEN.blit(frame, self.rect.topleft)
        
    def handle_collision(self):
        self.state = "dying"
           
        