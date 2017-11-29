import turtle

#import random

#class Square(turtle):
    #def __init__(self,color,size):
        
        #turtle.__init__(self)
        
        #self.color(color)
        #self.shapesize(size)
        #self.shape("square")

    #def pick_color():
        #colors = ["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink"]
        #random.shuffle(colors)
        #return colors[0]
        #random_color = pick_color()
        #print(random_color)


class Rectangle:

    def __init__(self):
        self.set_length = 1
        self.set_width = 1
        self.get_length = 1
        self.get_width = 1
        self.get_area = 1

    def get_area(self):
        self.get_area = self.get_width * self.get_length
        return self.get_area


    def main():

        my_rect = Rectangle()

        my_rect.set_length(4)
        my_rect.set_width(2)

        print('The length is',my_rect.get_length())
        print('The width is', my_rect.get_width())

        print('The area is',my_rect.get_area())
        print(my_rect)

        input('press enter to continue')       
        
    


    
