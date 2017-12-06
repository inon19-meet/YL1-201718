from turtle import *
import random
import math

class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle. __init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)

ball1=Ball(10,"blue",5)
ball2=Ball(6,"red",2)
    
def check_colloision(ball1,ball2):
    D = math.sqrt(math.pow(ball2.xcor()-bal11.xcor(),2)+math.pow(ball2.ycor()-bal11.ycor(),2))
    sum = ball1.radius+ball2.radius
    if(Dr>sum):
        print("no collaide hear sr")
    if(D<sum):
        print("cooooollaiiiiide!!" "                 " "(wrote by math boy)")
        
        
