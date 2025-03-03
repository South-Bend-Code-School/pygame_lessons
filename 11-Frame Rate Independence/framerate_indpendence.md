# Understanding Frame Rate Independence in Game Development

## Why Should You Care About Frame Rate Independence?

Imagine you are playing a game where a character moves at a fixed speed of 5 pixels per frame. Now, imagine the game runs at 60 frames per second (FPS). That means the character moves **5 × 60 = 300 pixels per second**. But what if your computer slows down and runs at 30 FPS? Suddenly, the character moves **5 × 30 = 150 pixels per second**, making the game feel sluggish and unfair.

This is why we use **frame rate-independent movement**! Instead of moving by a fixed amount per frame, we adjust movement based on the time that has passed, ensuring the game plays consistently regardless of FPS.

## How the Code Works

In our game, we have a spinning square, and we make sure it rotates at a constant speed, no matter what the FPS is.

### **Key Concepts**

### 1. **Milliseconds and `delta_time`**
Computers run really fast, so instead of measuring time in seconds, we use **milliseconds** (1 second = 1000 milliseconds). 

We calculate the time since the last frame using:
```python
    delta_time = clock.get_time() / 1000.0
```
`clock.get_time()` gives the time in milliseconds since the last frame, and we divide by 1000 to convert it into seconds.

#### **Analogy:** 
Think of a car's speedometer. If a car moves at 60 miles per hour, it doesn’t matter how often you check—it should always move at 60 miles per hour, not 60 miles per check! **`delta_time` helps us adjust movement speed based on real-world time instead of the number of frames.**

### 2. **Frame Rate-Independent Rotation**
Instead of adding a fixed amount to the angle each frame, we multiply the rotation speed by `delta_time`:
```python
    angle += rotation_speed * delta_time
```
If the game runs slower, `delta_time` is larger, ensuring the square still rotates at the correct speed.

#### **Example of Different `delta_time` Values but Same Rotation**

Let's assume our square rotates at **90 degrees per second**.

- **At 60 FPS**:
  - `delta_time = 1/60 = 0.0167 seconds`
  - `angle increase = 90 * 0.0167 = 1.5 degrees`

- **At 30 FPS**:
  - `delta_time = 1/30 = 0.0333 seconds`
  - `angle increase = 90 * 0.0333 = 3 degrees`

Even though the time per frame is different, the total rotation per second remains 90 degrees!

Another example:
- **At 15 FPS (`delta_time = 1/15 = 0.0667 seconds`)** → `angle increase = 90 * 0.0667 = 6 degrees`
- **At 10 FPS (`delta_time = 1/10 = 0.1 seconds`)** → `angle increase = 90 * 0.1 = 9 degrees`

This proves that no matter how fast or slow the game runs, the square **always rotates at 90 degrees per second**.

## Try It in Your Own Projects!
If you’re making a game where objects move, always make sure your movement is based on time, not frames. Use `delta_time` for:
- **Character movement**
- **Animations**
- **Physics calculations**
- **Rotations (like our square!)**

By making games frame rate-independent, you ensure a smooth and fair experience for all players! 🚀

---

## **Walkthrough of `game_loop.py`**

#### 1. **Initializing Pygame and Creating the Window**
```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spinning Square with FPS Counter")
```
This sets up Pygame and creates a window that is 800x600 pixels.

#### 2. **Defining the Square and Frame Rate Settings**
```python
TARGET_FPS = 30
square_size = 100
square_center = (400, 300)
angle = 0
rotation_speed = 90  # Degrees per second
```
We set the square size, its center, and rotation speed. The FPS starts at 30 but can be changed.

#### 3. **Using `delta_time` for Frame Rate Independence**
```python
delta_time = clock.get_time() / 1000.0
angle += rotation_speed * delta_time
```
Instead of increasing `angle` by a fixed amount per frame, we scale it by `delta_time`, ensuring smooth rotation at any FPS.

#### 4. **Handling User Input to Adjust FPS and Rotation Speed**
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

#### 5. **Drawing the Rotating Square**
```python
square_surface = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
pygame.draw.rect(square_surface, (0, 255, 0), (0, 0, square_size, square_size))
rotated_square = pygame.transform.rotate(square_surface, angle)
rect = rotated_square.get_rect(center=square_center)
screen.blit(rotated_square, rect.topleft)
```
We create a square surface, rotate it, and draw it at the center of the screen.

#### 6. **Displaying FPS and Rotation Speed**
```python
fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (255, 255, 255))
screen.blit(fps_text, (700, 10))
```
The FPS is displayed in the top-right corner.

#### 7. **Updating the Screen and Controlling FPS**
```python
pygame.display.flip()
clock.tick(TARGET_FPS)
```
The display is updated each frame, and the frame rate is capped at `TARGET_FPS`.