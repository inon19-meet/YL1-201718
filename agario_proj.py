import turtle
import math
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
turtle.update()
def move_all_balls():
    for ball in BALLS:
        ball.Move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball1,ball2):
    if ball1==ball2:
        return False
    D = math.sqrt(math.pow(ball2.xcor()-ball1.xcor(),2)+math.pow(ball2.ycor()-ball1.ycor(),2))
    summ = ball1.r+ball2.r
    if(D>summ):
        return False
    if(D<summ):
        return True
        
    
def check_collision():
    for ball1 in BALLS:
        for ball2 in BALLS:
            if collide(ball1,ball2):
                br1 = ball1.r
                br2 = ball2.r
                x_cor = random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS,int(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
                y_cor = random.randint(int(-SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS,int(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS)
                dx_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                dy_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                redius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                color =(random.random(),random.random(),random.random())
                if br1<br2:
                    ball1.x = x_cor
                    ball1.y = y_cor
                    ball1.dx = dx_speed
                    ball1.dy = dy_speed
                    ball1.r = redius
                    ball1.color = color
                if br1>br2:
                     ball1.r=br1+1
def check_myball_collision():
    for MY_Ball in BALLS:
        for ball in BALLS:
            if collide(MY_BALL,ball):
                br11 = ball.r
                brMB =  MY_BALL.r
                x_cor = random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS,int(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
                y_cor = random.randint(int(-SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS,int(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS)
                dx_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                dy_speed = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                redius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                color =(random.random(),random.random(),random.random())
                if brMB<br11:
                    ball.x = x_cor
                    ball.y = y_cor
                    ball.dx = dx_speed
                    ball.dy = dy_speed
                    ball.r = redius
                    ball.color = color
                if brMB>br11:
                     brMB=brMB+1
                if(MY_BALL<ball):
                    return False

    return True

def movearound(event):
    MY_BALL.goto(event.x-SCREEN_WIDTH,event.y-SCREEN_HEIGHT)


turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while RUNNING == True:
    if SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:
        SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
        SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
    move_all_balls()
    check_collision()
    MY_BALL.Move(SCREEN_WIDTH, SCREEN_HEIGHT)
    #check_myball_collision()
    
    turtle.update()
    time.sleep(SLEEP)
    

                     




















    
    
                








    
    

        
    







