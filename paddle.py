from turtle import Turtle

MOVE_DIST = 70


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('steel blue')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(x=0, y=-280)

    def move_left(self):
        self.backward(MOVE_DIST)

    def move_right(self):
        self.forward(MOVE_DIST)

# from turtle import Turtle, Screen
# import turtle
# from ball import Ball
# from bricks import Brick
#
# wn = turtle.Screen()
# wn.setup(600, 600)
# screen = wn.getcanvas()
# # t = turtle.Turtle()
#
#
# class Paddle(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.color("dim gray")
#         self.shape("square")
#         self.shapesize(stretch_wid=0.5, stretch_len=6)
#         # self.t.goto(0, -280)
#         self.x = 300
#         self.y = 570
#         self.penup()
#         self.speed("fastest")
#         screen.bind('<Motion>', self.set_coords)
#         self.run()
#
#     def set_coords(self, event):
#         self.x = event.x
#         # x = event.x
#         # self.y = event.y
#
#     def run(self):
#         while True:
#             self.setposition(self.x - 300, (self.y * -1) + 300)
#
# m = Paddle()
# bl = Ball()
# br = Brick()
#
# # playing game = True
#
# # Define collision with paddle
#
# # while playing_game is True
