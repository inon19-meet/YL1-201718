
import turtle

from turtle import *
for i in range(250): # this "for" loop will repeat these functions 500 times
    forward(i)
    left(91)
from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(59)
turtle.goto(100,100)
ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)

seurat = turtle.Turtle()

dot_distance = 25
width = 5
height = 7

seurat.penup()
turtle.goto(-100,-100)
for y in range(height):
    for i in range(width):
        seurat.dot()
        seurat.forward(dot_distance)
    seurat.backward(dot_distance * width)
    seurat.right(90)
    seurat.forward(dot_distance)
    seurat.left(90)
turtle.goto(200,-200)
painter = turtle.Turtle()

painter.pencolor("blue")

for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)
    
spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 15)
    spiral.right(144)
    
turtle.done()
turtle.speed(10,0)
