import turtle
import time
import random
from ball import Ball

turtle.tracer(0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(10,10,10,10,5,"red")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = []
for i in range(NUMBER_OF_BALLS):
    x = random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS,int(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
    y = random.randint(int(-SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS,int(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS)
    dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    redius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color =(random.random(),random.random(),random.random())
    d1 = Ball(x,y,dx,dy,redius,color)
    BALLS.append(d1)

def move_all_balls():
    for ball in BALLS:
        ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
        
    










