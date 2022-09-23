from turtle import *
# import random

colors = ("blue", "orange2", "dark blue", "red")


t = Turtle()
t.shape("turtle")
# t.shapesize(stretch_len=1, stretch_wid=2)
# t.color("blue")

def draw_shape(side_nums):
    angle = 360 / side_nums
    for _ in range(side_nums):
        t.forward(100)
        t.left(angle)

for shape_sides in range(3, 9):
    draw_shape(shape_sides)
    t.color(random.choice(colors))


