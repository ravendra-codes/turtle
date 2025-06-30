import turtle
import colorsys

# Screen setup
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.width(2)

# Colors
h = 0
n = 36  # Number of petals

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.color(c)
    t.circle(180)
    t.left(60)
    t.circle(180)
    t.left(60)
    t.circle(180)
    t.left(60)
    t.circle(180)
    t.left(60)
    t.circle(180)
    t.left(60)
    t.circle(180)
    t.left(60)
    t.left(1)
    h += 1/n

turtle.done()
