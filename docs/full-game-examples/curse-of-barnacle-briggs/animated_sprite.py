import pygame
import time

class AnimatedSprite:
    def __init__(self, image, frame_width, animation_speed_ms=150):
        """
        Initialize the animated spritesheet.

        Parameters:
        - image: A pygame image object.
        - frame_width: Width of each frame in pixels. Defaults to 32 pixels.
        - animation_speed_ms: The animation speed in milliseconds (1000 ms = 1 second).
        """
        # Load the sprite sheet.
        self.sprite_sheet = image
        self.frame_width = frame_width
        self.animation_speed_ms = animation_speed_ms

        # Calculate dimensions and frames.
        self.frame_height = self.sprite_sheet.get_height()  # Assumes sprite sheets are organized horizontally.
        self.frame_count = self.sprite_sheet.get_width() // frame_width # integer division //
        self.current_frame = 0  # Start at the first frame of the animation.

        # Time tracking.
        self.last_update_time = time.time()  # Record the last time the frame was updated.

    def get_frame(self):
        """
        Get the current frame as a surface.
        """
        current_time = time.time()
        elapsed_time_ms = (current_time - self.last_update_time) * 1000  # Convert seconds to milliseconds.

        if elapsed_time_ms >= self.animation_speed_ms:
            # Advance to the next frame.
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.last_update_time = current_time  # Reset the last update time.

        x = self.current_frame * self.frame_width
        frame = self.sprite_sheet.subsurface((x, 0, self.frame_width, self.frame_height))
        return frame
    
    def is_last_frame(self):
        """
        Check if the current frame is the last frame in the animation.
        Returns:
        - True if the current frame is the last frame, otherwise False.
        """
        return self.current_frame == self.frame_count - 1

    def reset_animation(self):
        self.current_frame = 0