import turtle
from tkinter import *

t = turtle.Turtle()
t.shape("turtle")
t.speed(5)

# Torso and Right Arm-----

t.left(90)
t.forward(50)
t.right(95)
t.forward(50)

# Ball Right Hand---------

t.color("red")
t.begin_fill()
t.circle(10)
t.end_fill()

# Left Hand---------------

t.color("black")
t.backward(50)
t.left(210)
t.forward(50)
t.backward(50)
t.seth(90)

# Head-------------------

t.forward(20)
t.right(90)
t.color("yellow")
t.begin_fill()
t.circle(30)
t.end_fill()
t.color("black")
t.circle(30)

# Right Eye--------------

t.penup()      #
t.left(90)
t.forward(30)
t.right(90)
t.forward(15)
t.pendown()    ##
t.circle(6)
t.penup()      #
t.left(90)
t.forward(4)
t.right(90)
t.pendown()    ##
t.color("orange")
t.begin_fill()
t.circle(2)
t.end_fill()
t.color("black")
t.penup()      #
t.left(90)
t.backward(4)
t.right(90)
t.right(90)
t.left(90)

# Left Eye---------------

t.backward(30)
t.pendown()    ##
t.circle(6)
t.penup()      #
t.left(90)
t.forward(4)
t.right(90)
t.pendown()    ##
t.color("orange")
t.begin_fill()
t.circle(2)
t.end_fill()
t.color("black")
t.penup()      #
t.left(90)
t.backward(5)
t.right(90)
t.penup()      #
t.forward(15)
t.left(90)
t.forward(25)
t.left(90)

# Hat--------------------

t.pendown()    ##
t.pensize(10)
t.circle(150, -10)
t.circle(150, 10)
t.circle(150, 10)
t.circle(150, -10)
t.pensize(1)
t.right(180)

t.color("blue")
t.begin_fill()
t.circle(20)
t.end_fill()

t.forward(15)

t.begin_fill()
t.circle(10)
t.end_fill()

t.backward(30)

t.begin_fill()
t.circle(10)
t.end_fill()

t.forward(15)

t.color("black")
t.penup()      #
t.right(90)
t.forward(40)
t.left(90)

# Smile------------------

t.pendown()    ##

for i in range(3):
    t.right(90)
    t.forward(3)

t.penup()      #
t.right(90)
t.forward(3)
t.pendown()    ##
t.circle(30, 30)
t.circle(30, -60)
t.circle(30, 30)
t.penup()      #

# Legs--------------------

t.right(90)
t.forward(85)
t.left(30)
t.pendown()    ##
t.forward(50)
t.penup()      #
t.backward(50)
t.seth(90)
t.pendown()    ##
t.left(150)
t.forward(50)
t.penup()      #

# Save image---------------

ts = turtle.getscreen()

ts.getcanvas().postscript(file="turtleStick.eps")
