import pygame
from animated_sprite import AnimatedSprite
from constants import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT


class Player:

    swimming_image = pygame.image.load("images/player-swiming.png")
    hurt_image = pygame.image.load("images/player-hurt.png")
    hurt_sound = pygame.mixer.Sound("sounds/player-hurt.wav") 

    def __init__(self, x, y, movement_speed=3):
        """
        Initialize the player object.

        Parameters:
        - x (int): Initial x-coordinate of the player.
        - y (int): Initial y-coordinate of the player.
        - frame_width (int): Width of a single frame in the sprite sheet.
        - movement_speed (int): Movement speed of the player. Defaults to 5.
        """
        frame_width = 47
        self.sprite_swimming = AnimatedSprite(Player.swimming_image, frame_width, animation_speed_ms=100)
        self.sprite_hurt = AnimatedSprite(Player.hurt_image, frame_width, animation_speed_ms=150)
        self.rect = pygame.Rect(x, y, frame_width, self.sprite_swimming.sprite_sheet.get_height())
        self.movement_speed = movement_speed
        
        # Possible states are "active", "hurt", "dead"
        self.state = "active"
        self.lives = 3
    
    def move(self, direction):
        """
        Move the player in the specified direction, ensuring they stay within bounds.

        Parameters:
        - direction (str): Direction to move ('up', 'down', 'left', 'right').
        """
        # Move based on direction
        if direction == "up":
            self.rect.y -= self.movement_speed
        elif direction == "down":
            self.rect.y += self.movement_speed
        elif direction == "left":
            self.rect.x -= self.movement_speed
        elif direction == "right":
            self.rect.x += self.movement_speed

        # Apply boundary constraints
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

    def handle_collision(self):
        if self.state == "active":
            self.lives = self.lives - 1
            self.state = "hurt"
            Player.hurt_sound.play()
        
    def update_state(self):
        if self.state == "hurt" and self.sprite_hurt.is_last_frame():
            self.state = "active"
            self.sprite_hurt.reset_animation()
        
        if self.lives == 0:
            self.state = "dead"

    def draw(self):
        """
        Draw the player's current frame based on the player's state
        """
        if self.state == "active":
            frame = self.sprite_swimming.get_frame()
        elif self.state == "hurt":
            frame = self.sprite_hurt.get_frame()
        else:
            print("unknown player state")
            return

        SCREEN.blit(frame, self.rect.topleft)
    
