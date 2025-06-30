import turtle as tu

# Setup turtle
roo = tu.Turtle()
wn = tu.Screen()
wn.bgcolor("black")
wn.title("Fractal Tree Pattern")
roo.left(90)
roo.speed(0)

# Unified draw function
def draw(l, color, pensize):
    if l < 10:
        return
    roo.pensize(pensize)
    roo.pencolor(color)
    roo.forward(l)
    roo.left(30)
    draw(0.75 * l, color, pensize)
    roo.right(60)
    draw(0.75 * l, color, pensize)
    roo.left(30)
    roo.backward(l)

# Draw from different angles and colors
patterns = [
    ("yellow", 20, 2, 90),
    ("magenta", 20, 2, 90),
    ("red", 20, 2, -90),
    ("white", 20, 2, 90),
    ("lightgreen", 40, 3, -90),
    ("red", 40, 3, 90),
    ("yellow", 40, 3, -90),
    ("white", 40, 3, 90),
    ("cyan", 60, 2, 0),
    ("yellow", 60, 2, -90),
    ("magenta", 60, 2, 90),
    ("white", 60, 2, 0)
]

for color, length, pensize, turn in patterns:
    roo.setheading(turn)
    draw(length, color, pensize)

# Click to exit
wn.exitonclick()
