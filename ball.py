from turtle import *
class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.color(color)
        self.shapesize(r/10)
        self.shape("circle")

    def Move(self,screen_width,screen_height):
        current_x = self.x
        current_y = self.y
        current_dx = self.dx
        current_dy = self.dy
        new_x = current_x+current_dx
        new_y = current_y+current_dy

    def ball_right_side(self,right_side):
        self.right_side = (x+r,y)
    def ball_left_side(self,right_side):
        self.left_side = (x-r,y)
    def ball_up_side(self,up_side):
        self.up_side = (x,y+r)
    def ball_down_side(self,down_side):
        self.down_side = (x,y-r)
        




















