# **Handling Keyboard Input in Pygame**


<style>
    .container {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: center;
        gap: 20px;
        text-align: center;
    }

    .image-container, .button-container {
        flex: 1 1 100%; /* Default: Full width */
    }

    .image-container img {
        max-width: 100%;
        height: auto;
    }

    @media (min-width: 768px) { /* Side-by-side on larger screens */
        .container {
            flex-wrap: nowrap; /* Prevent wrapping */
            text-align: left; /* Align text properly */
        }
        .image-container, .button-container {
            flex: 0 1 auto; /* Side by side */
        }
    }
</style>

<div class="container">
    <!-- Image -->
    <div class="image-container">
        <img src="../keyboard_input.png" alt="All Shapes" width="350">
    </div>

    <!-- Download Button -->
    <div class="button-container">
        <a href="../keyboard_input.py" download class="md-button md-button--primary">
            ⬇ Download keyboard_input.py
        </a>
    </div>
</div>

In this example:

- The square's speed can be adjusted by **pressing** the + and - keys.
- The square can move in any direction by **holding down** the arrow keys.
- The square is kept within screen boundaries.

## **Understanding Keyboard Events**
Pygame detects user input through events. An **event** is an action that occurs during the game, like pressing a key, moving the mouse, or clicking a button. Pygame keeps track of these events in an **event queue**, which we check every frame of our game loop.

### **Types of Key Press Events**
There are two primary keyboard events in Pygame:

1. **`pygame.KEYDOWN`** – Fired when a key is pressed down.
2. **`pygame.KEYUP`** – Fired when a key is released.

Each key on the keyboard has a unique constant, such as:

- `pygame.K_LEFT` → Left Arrow Key
- `pygame.K_RIGHT` → Right Arrow Key
- `pygame.K_UP` → Up Arrow Key
- `pygame.K_DOWN` → Down Arrow Key

We capture these events in Pygame using `pygame.event.get()` inside our game loop.

### **Detecting a Key Press**

We use the event loop to detect when a key is pressed or released. Because multiple keys can be pressed durning any given frame, we always get a **list** of events.  Notice, we use a `for` loop to iterate through each event allowing for us to react to multiple keys being pressed durning the same frame.

#### **Using `pygame.event.get()`**

The following code detects if the `+` or =`-` key was pressed down.  It only fires once.

```python
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:  # Increase speed
                player_speed += 1
            elif event.key == pygame.K_MINUS or event.key == pygame.K_UNDERSCORE:  # Decrease speed
                player_speed = max(1, player_speed - 1)
```

For every `event`:

- The `event.type` tells us whether a key was just pressed down (`KEYDOWN`) or released (`KEYUP`).
- The `event.key` tells us which key was pressed or released.

When you create your own game, think clearly about if you want to respond to the `KEYDOWN` or `KEYUP` event.

### **Detecting Held Keys**

In many games, we need to check if a key is **being held down** rather than just detecting the moment it is pressed. This is especially useful for **continuous movement**, such as keeping a character moving while holding the arrow key.

#### **Using `pygame.key.get_pressed()`**
Pygame provides `pygame.key.get_pressed()`, which returns a **list** where each index corresponds to a key on the keyboard. The value is `True` if the key is currently being held, and `False` otherwise.

#### **Example: Detecting Held Keys**
```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    print("Left arrow key is being held down")
```

