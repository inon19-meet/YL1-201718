import turtle
#draw a pantegram
#num_pts = 5 #number sides to your drawing!
#for i in range(num_pts):
  #  turtle.left(720/num_pts) #720 pentegram
   # turtle.forward(100)

#turtle.mainloop()
######################################################################################
#print(turtle.getshapes())
#turtle.left(90)
#turtle.register_shape("inon", ((50,0), (50,50), (0,50), (0,0), (25,-50), (50,0)))
#turtle.shape("inon")
########################################################################################
turtle.tracer(1,0)
for i in range(1000):
    turtle.pendown()
    turtle.forward(200)
    turtle.right(50)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.penup()
    turtle.goto(0,0)
    turtle.right(0.09)

