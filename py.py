import turtle as t
import colorsys

# Setup
t.bgcolor("black")
t.tracer(100)
t.pensize(1)
h = 0.0  # Start hue from 0

# Drawing loop
for i in range(250):
    # Update color using HSV model
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.005  # Increment hue to cycle colors

    t.fillcolor(c)
    t.begin_fill()

    t.forward(i)
    t.left(100)
    t.circle(30)

    for j in range(2):
        t.forward(i * (j + 1))  # Avoid zero multiplication
        t.right(109)

    t.end_fill()

t.done()
