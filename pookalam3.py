import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Changed background color
screen.title("Pookalam Design - Pixels & Petals")

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

# Named color palette
color_palette = [
    "red", "orange", "yellow", "green", "blue", "purple",
    "pink", "cyan", "magenta", "lime", "turquoise", "gold"
]

def draw_petal(radius, color, num_petals):
    """Draws one circular ring of petals"""
    t.color(color)
    for i in range(num_petals):
        t.begin_fill()
        t.circle(radius, 60)
        t.left(120)
        t.circle(radius, 60)
        t.end_fill()
        t.left(360 / num_petals)

def draw_circle(radius, color):
    """Draws filled circle in the center"""
    t.up()
    t.goto(0, -radius)
    t.down()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# === Draw multiple layers ===
layers = [
    (150, 36),  # Outer big petals
    (100, 24),  # Second layer
    (70,  18),  # Third layer
    (40,  12)   # Inner layer
]

for radius, petals in layers:
    for i in range(petals):
        color = random.choice(color_palette)
        t.color(color)
        t.begin_fill()
        t.circle(radius, 60)
        t.left(120)
        t.circle(radius, 60)
        t.end_fill()
        t.left(360 / petals)

# === Center decoration circles ===
draw_circle(30, "yellow")
draw_circle(20, "orange")
draw_circle(10, "red")

# === Outer decorative rings ===
def draw_outer_ring(radius, color,thickness):
    t.up()
    t.goto(0, -radius)
    t.down()
    t.pensize(thickness)
    t.color(color)
    t.circle(radius)
    t.pensize(1)

draw_outer_ring(160, "yellow",16)
draw_outer_ring(190, "gold",18)
draw_outer_ring(200, "violet",20)
draw_outer_ring(210,"pink",25)
draw_outer_ring(240,"red",30)

t.hideturtle()
turtle.done()