# Drawing Shapes in Pygame

<a href="../draw_shapes.py" download class="md-button md-button--primary">
    ⬇ Download draw_shapes.py
</a>

## Understanding Coordinates in Pygame
In Pygame, every object is placed using **coordinates**. A coordinate is a pair of numbers **(x, y)** that tells us where something is on the screen.

- The **x-value** represents the **horizontal position** (left to right).
- The **y-value** represents the **vertical position** (top to bottom).
- Coordinates are always written as **(x, y)** in parentheses.

### The Pygame Coordinate System
Pygame’s screen follows this coordinate system:
- **(0,0) is in the top-left corner** of the screen.
- As **x increases**, the position moves **to the right**.
- As **y increases**, the position moves **downward**.

To help visualize this, a **grid** is drawn in 50-pixel increments, with labels marking x and y positions.

## Drawing Shapes in Pygame
Pygame provides built-in functions to draw various shapes. The general format for these functions is:

```python
pygame.draw.shape(SCREEN, COLOR, DETAILS)
```

Each function follows this order:
1. **SCREEN** – The surface to draw on (usually the game screen).
2. **COLOR** – The color of the shape (defined as an RGB tuple like `(255, 0, 0)` for red).
3. **DETAILS** – The parameters specific to the shape being drawn, including **coordinates**.

### Available Shapes:
1. **Rectangle (`pygame.draw.rect`)**
   ```python
   pygame.draw.rect(SCREEN, RED, (50, 50, 200, 100))
   ```
   - Draws a rectangle at **(50,50)**
   - Width = **200**, Height = **100**

2. **Circle (`pygame.draw.circle`)**
   ```python
   pygame.draw.circle(SCREEN, GREEN, (400, 300), 50)
   ```
   - Center = **(400,300)**
   - Radius = **50**

3. **Line (`pygame.draw.line`)**
   ```python
   pygame.draw.line(SCREEN, BLUE, (100, 500), (700, 500), 5)
   ```
   - Starts at **(100,500)**, ends at **(700,500)**
   - Line thickness = **5 pixels**

4. **Polygon (`pygame.draw.polygon`)**
   ```python
   pygame.draw.polygon(SCREEN, BLACK, [(600, 100), (650, 200), (550, 200)])
   ```
   - Connects points **(600,100)**, **(650,200)**, and **(550,200)** to form a triangle.

5. **Ellipse (`pygame.draw.ellipse`)**
   ```python
   pygame.draw.ellipse(SCREEN, RED, (300, 400, 150, 80))
   ```
   - Fits inside a bounding box at **(300,400)**
   - Width = **150**, Height = **80**

## The Purpose of the Grid
The **grid** helps students see how the coordinate system works and where objects are placed. The numbers make it easier to position objects accurately.

---

## Challenges
Try modifying the code to place the shapes in different locations:
1. Move the **rectangle** to **(100,100)** and double its size.
2. Change the **circle’s position** so it appears in the **bottom-right corner**.
3. Make the **line diagonal**, starting from **(0,0)** to **(800,600)**.
4. Adjust the **triangle** to form a different shape by modifying the points.