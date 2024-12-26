from turtle import *
import time

pendown()
speed(2)
hideturtle()
pensize(5)
color("green")
bgcolor("black")


for n in range(11):
    forward(24)
    bgcolor("#CC7264")
    color("blue")
    right(25)
    bgcolor("yellow")
    color("black")
    forward(32)
    bgcolor("#EED2CC")
    color("brown")
    left(61)
    bgcolor("blue")

time.sleep(2)
bgcolor("black")

done()