# Understanding Frame Rate Independence in Game Development

<div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
    <!-- Download Button -->
    <div>
        <a href="../framerate_indpendence.py" download class="md-button md-button--primary">
            ⬇ Download framerate_independence.py
        </a>
    </div> 
</div>

<!-- Grid for Animation Comparison -->
<div style="display: flex; flex-direction: column; gap: 20px; align-items: center;">
    <!-- Frame Rate Independent Card -->
    <div style="border: 2px solid #4CAF50; border-radius: 10px; padding: 20px; width: 80%; background-color: #e8f5e9; text-align: center;">
        <div style="font-weight: bold; font-size: 20px; color: #2E7D32;">✅ Frame Rate Independent (Delta Time) - GOOD</div>
        <div style="margin-bottom: 10px;">Rotates at 160 degrees per second, maintaining consistent motion across all frame rates.</div>
        <pre style="background-color: #dff0d8; padding: 10px; border-radius: 5px; text-align: left; overflow-x: auto;">delta_time = clock.get_time() / 1000.0</br>angle += 160 * delta_time</pre>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
            <div>
                <img src="../independent_10fps.gif" alt="Independent 10 FPS" width="300">
                <div>9 FPS (160 degrees per second)</div>
            </div>
            <div>
                <img src="../independent_60fps.gif" alt="Independent 60 FPS" width="300">
                <div>60 FPS (160 degrees per second)</div>
            </div>
        </div>
    </div>

    <!-- Frame Rate Dependent Card -->
    <div style="border: 2px solid #D32F2F; border-radius: 10px; padding: 20px; width: 80%; background-color: #ffebee; text-align: center;">
        <div style="font-weight: bold; font-size: 20px; color: #C62828;">❌ Frame Rate Dependent - BAD</div>
        <div style="margin-bottom: 10px;">Rotates 160 degrees per frame, causing inconsistency in motion across different frame rates.</div>
        <pre style="background-color: #f8d7da; padding: 10px; border-radius: 5px; text-align: left; overflow-x: auto;">angle += 160</pre>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
            <div>
                <img src="../dependent_10fps.gif" alt="Dependent 10 FPS" width="300">
                <div>9 FPS (160 degrees per frame)</div>
            </div>
            <div>
                <img src="../dependent_60fps.gif" alt="Dependent 60 FPS" width="300">
                <div>60 FPS (160 degrees per frame)</div>
            </div>
        </div>
    </div>
</div>

## Why Should You Care About Frame Rate Independence?

Imagine you are playing a game where a character moves at a fixed speed of 5 pixels per frame. Now, imagine the game runs at 60 frames per second (FPS). That means the character moves **5 × 60 = 300 pixels per second**. But what if your computer slows down and runs at 30 FPS? Suddenly, the character moves **5 × 30 = 150 pixels per second**, making the game feel sluggish and unfair.

This is why we use **frame rate-independent movement**! Instead of moving by a fixed amount per frame, we adjust movement based on the time that has passed, ensuring the game plays consistently regardless of FPS.

## How the Code Works

In our game, we have a spinning square, and we make sure it rotates at a constant speed, no matter what the FPS is.

### **Key Concepts**

### **Milliseconds and `delta_time`**
Computers run really fast, so instead of measuring time in seconds, we use **milliseconds** (1 second = 1000 milliseconds). 

We calculate the time since the last frame using:
```python
    delta_time = clock.get_time() / 1000.0
```
`clock.get_time()` gives the time in milliseconds since the last frame, and we divide by 1000 to convert it into seconds.


### **Framerate Independent Rotation**
Instead of adding a fixed amount to the angle each frame, we multiply the rotation speed by `delta_time`:
```python
    angle += rotation_speed * delta_time
```

If the game runs slower, `delta_time` is larger, ensuring the square still rotates at the correct speed.


By adjusting the amount of movement each frame by the time it took to render the frame, we ensure that no matter how fast or slow the game runs, the square **always rotates at 90 degrees per second**.

## Try It in Your Own Projects!
If you’re making a game where objects move, always make sure your movement is based on time, not frames. Use `delta_time` for:

- **Character movement**
- **Animations**
- **Physics calculations**
- **Rotations (like our square!)**

By making games frame rate-independent, you ensure a smooth and fair experience for all players!

---

## **Walkthrough of `game_loop.py`**

### **Initializing Pygame and Creating the Window**
```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spinning Square with FPS Counter")
```
This sets up Pygame and creates a window that is 800x600 pixels.

### **Defining the Square and Frame Rate Settings**
```python
TARGET_FPS = 30
square_size = 100
square_center = (400, 300)
angle = 0
rotation_speed = 90  # Degrees per second
```
We set the square size, its center, and rotation speed. The FPS starts at 30 but can be changed.

#### **Using `delta_time` for Frame Rate Independence**
```python
delta_time = clock.get_time() / 1000.0
angle += rotation_speed * delta_time
```

Instead of increasing `angle` by a fixed amount per frame, we scale `rotation_speed` by `delta_time`, ensuring smooth rotation at any FPS.

#### **Handling User Input to Adjust FPS and Rotation Speed**
```python
elif event.key == pygame.K_UP:
    rotation_speed += 10
elif event.key == pygame.K_DOWN:
    rotation_speed = max(10, rotation_speed - 10)
elif event.key == pygame.K_RIGHT:
    TARGET_FPS = min(60, TARGET_FPS + 10)
elif event.key == pygame.K_LEFT:
    TARGET_FPS = max(10, TARGET_FPS - 10)
```
This allows users to change the FPS and rotation speed dynamically while the game is running.

#### **Drawing the Rotating Square**
```python
square_surface = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
pygame.draw.rect(square_surface, (0, 255, 0), (0, 0, square_size, square_size))
rotated_square = pygame.transform.rotate(square_surface, angle)
rect = rotated_square.get_rect(center=square_center)
screen.blit(rotated_square, rect.topleft)
```

We create a square surface, rotate it, and draw it at the center of the screen.

#### **Displaying FPS and Rotation Speed**
```python
fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (255, 255, 255))
screen.blit(fps_text, (700, 10))
```
The FPS is displayed in the top-right corner.

#### **Updating the Screen and Controlling FPS**
```python
pygame.display.flip()
clock.tick(TARGET_FPS)
```

The display is updated each frame, and the frame rate is capped at `TARGET_FPS`.