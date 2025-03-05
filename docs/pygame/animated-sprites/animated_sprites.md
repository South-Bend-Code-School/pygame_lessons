# Creating an Animated Sprite

## **Lesson Objective**

Create an `AnimatedSprite` class that:

- Loads a sprite sheet where frames are laid out horizontally.
- Loops through the animation frames at a controlled speed.
- Returns the current frame for rendering.

---

## **Concepts Covered**

1. **Sprite Sheets** – Understanding how images with multiple animation frames are organized.
2. **Subsurface Extraction** – Extracting individual frames from a sprite sheet.
3. **Frame Timing & Animation** – Cycling through frames based on elapsed time.
4. **Object-Oriented Programming** – Encapsulating animation logic in a class.

---

## Understanding Sprite Sheets

A sprite sheet is a single image containing multiple animation frames. Instead of loading multiple images, we extract sections of this sheet to create an animation.

For this lesson, we assume all frames are laid out **horizontally** in a single row.

Example: **`coin-gold.png`**

![Coin Sprite](../coin-gold.png)

This sprite has 5 frames.

```
-------------------------------------------------
| Frame 1 | Frame 2 | Frame 3 | Frame 4 | Frame 5 |
-------------------------------------------------
```

Each frame has the same width and height.  

- Width: 16 pixels
- Heigh  16 pixels

---

## The `AnimatedSprite` Class
Below is a class that will handle sprite animation.

```python
import pygame
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
```


## **Challenges**
1. Modify `animation_speed_ms` to **speed up or slow down** the animation.
2. Add **a second sprite animation** to the scene.
3. Modify `AnimatedSprite` to **support vertically laid out sprites** (e.g., stacked frames).