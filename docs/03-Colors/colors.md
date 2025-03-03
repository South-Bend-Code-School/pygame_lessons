# Understanding RGB Colors

## What is RGB?
RGB stands for **Red, Green, and Blue**. It is an additive color model used to represent colors on digital screens. Each color on a screen is created by combining different intensities of red, green, and blue light. The combination of these three primary colors can produce millions of different colors.

### Additive Color Mixing
Unlike paint mixing, where combining colors makes them darker, RGB is an **additive** system, meaning that the more light you add, the brighter the color becomes:

- **Red + Green = Yellow**
- **Red + Blue = Magenta**
- **Green + Blue = Cyan**
- **Red + Green + Blue = White**
- **No light (0,0,0) = Black**

## Why RGB Matters
RGB is used in nearly every digital display device, including:
- Computer screens
- TVs
- Phones
- Projectors
- LED lighting

By adjusting the values of red, green, and blue, we can create any color that our eyes can perceive. Each color channel can range from **0** (no intensity) to **255** (full intensity), meaning there are **16,777,216** possible colors (256 × 256 × 256).

## Representing Colors as Tuples
RGB colors are often represented as **tuples** in programming, such as:
```python
(255, 0, 0)  # Red
(0, 255, 0)  # Green
(0, 0, 255)  # Blue
(255, 255, 0)  # Yellow
(255, 255, 255)  # White
```
A tuple is a collection of values in a fixed order, just like **(x, y) coordinates**. Just as (x, y) represents a position on a 2D plane, **(R, G, B)** represents a color where:
- The first number is the intensity of red
- The second number is the intensity of green
- The third number is the intensity of blue

## Visualizing RGB
Below is a diagram showing how different RGB values combine to form colors:

![RGB Color Mixing](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/AdditiveColor.svg/300px-AdditiveColor.svg.png)

_Above: Red, Green, and Blue lights mix to create new colors._

## How Our Program Works
In our Pygame program:
1. We display **three circles** representing red, green, and blue.
2. A **final color circle** represents their combined value.
3. You can adjust each color component using the **R, G, and B keys**, with Shift to increase and lowercase to decrease.
4. The numbers inside the circles show the current intensity of each color.

By adjusting these values, you can see how **RGB color mixing** works in real-time!

## Experiment!
Try changing the values and see how different colors form. What happens when:
- All values are the same?
- One value is at max while the others are at zero?
- You mix two primary colors?

RGB is the foundation of digital color, and understanding it will help you in **game design, graphics programming, and web development**!

