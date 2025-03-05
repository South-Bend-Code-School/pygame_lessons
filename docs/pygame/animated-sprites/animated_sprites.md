# Creating an Animated Sprites

![Coin Sprite](../ruby-gold-animated.gif)

<a href="../animated_sprites.py" download class="md-button md-button--primary">
    ⬇ Download animated_sprites.py
</a>

<a href="../coin-gold.png" download class="md-button md-button--primary">
    ⬇ Download Gold Coin Spritesheet
</a>

<a href="../coin-ruby.png" download class="md-button md-button--primary">
    ⬇ Download Ruby Coin Spritesheet
</a>

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

By drawing 1 frame at a time, an incrementing one frame every few milliseconds the sprite animates!

![Coin Sprite Animated](../coin-gold-animated.gif)
---

## Understanding the `AnimatedSprite` Class

In Python, a **class** is like a blueprint—it defines how an object should behave, just like a **cookie cutter** defines the shape of a cookie. But a class itself is not an object; it just tells Python how to create one. When we create an instance of a class, we are making an actual object (like baking a cookie from the cutter).

The `AnimatedSprite` class is a blueprint for animated sprites. It keeps track of:

- The current frame being displayed.
- How long each frame should be visible before moving to the next one.
- How to extract a frame from a sprite sheet.

### A simple `AnimatedSprite` Class example

```python
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
```

### How to Use the AnimatedSprite Class (Making a Cookie)

To use the `AnimatedSprite` class, we need to create an **instance** of it. This is like using the cookie cutter to actually make a cookie.  

In our class definition, creating an instance is handled by the __init__() function. This special function, known as the initializer, runs automatically whenever a new instance of the class is created.

The __init__ function:

- Defines what data is required to create a new instance.
- Sets up the attributes for this specific instance.
- Allows multiple objects to be created independently from the same class definition.

Think of a class as a cookie cutter and an instance as an individual cookie made from it.

### Creating an Instance
The following code creates a new instance of our AnimatedSprite.

```python
# Load our sprite sheet as an image
coin_img = pygame.image.load("coin-gold.png")

# Create an animated sprite using our class blueprint
animated_coin = AnimatedSprite(image=coin_img, frame_width=16, animation_speed_ms=100)
```

- `pygame.image.load("coin-gold.png")` loads a sprite sheet containing multiple frames.
- `AnimatedSprite(image=coin_img, frame_width=16, animation_speed_ms=100)` creates an instance (a new object) of our AnimatedSprite class.

The instance animated_coin now holds:

- The loaded sprite sheet.
- The width of a single animation frame (16 pixels).
- The speed at which the animation should update (every 100 milliseconds).

Since we might want multiple animated sprites in a game, we can create additional instances as needed:

Here is a ruby coin sprite sheet!

![Coin Sprite](../coin-gold.png)

```python
# Load another sprite sheet for a different animation
ruby_coin_img = pygame.image.load("coin-ruby.png")

# Create another animated sprite
ruby_coin_animated = AnimatedSprite(image=ruby_coin_img, frame_width=16, animation_speed_ms=80)
```

This allows us to animate multiple instances independently in our game!  Each object instance tracks it's own state and animation speed.

### Using `get_frame()` in the Game Loop

The `get_frame(dt)` function must be called inside the **game loop**, where we pass in the time that has elapsed since the last frame update. This ensures the animation progresses correctly over time.

Example usage inside a game loop:

```python
running = True
clock = pygame.time.Clock()
while running:
    dt = clock.tick(60) / 1000.0  # Get the time passed since last frame in seconds
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the updated frame with delta time
    coin_frame = animated_coin.get_frame(dt)
    
    # Draw the updated frame
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(coin_frame, (100, 100))
    pygame.display.flip()

pygame.quit()
```

### How It Works

- The `animated_coin` object now keeps track of the current animation frame.
- Every time we call `get_frame(dt)`, we pass in the time that has elapsed since the last update.
- The method checks if enough time has passed to switch to the next frame before returning it.
- The animation automatically updates within `get_frame()`.

### Summary

This class is useful because we can create **many different animated sprites** using the same blueprint!