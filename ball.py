from turtle import *
class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.pu()
        self.goto(x,y)
        self.color(color)
        self.shapesize(r/10)
        self.shape("circle")
        

    def Move(self,screen_width,screen_height):
        current_x = self.xcor()
        current_y = self.ycor()
        current_dx = self.dx
        current_dy = self.dy
        new_r = self.r
        new_x = current_x+current_dx
        new_y = current_y+current_dy

        self.goto(new_x, new_y)
        
        ball_right_side = new_x+new_r
        ball_left_side = new_x-new_r
        ball_up_side = new_y+new_r
        ball_down_side =new_y-new_r
        
        if ball_right_side>screen_width/2 or ball_left_side<-screen_width/2:
            self.dx = (-1)*self.dx

        if ball_up_side>screen_height/2 or ball_down_side<-screen_height/2:
            self.dy = (-1)*self.dy


















