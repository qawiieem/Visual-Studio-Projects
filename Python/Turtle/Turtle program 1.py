import turtle

background_colour=input("What colour do you want to set as your background?")
pen_colour=input("What colour do you want to set for your pen?")
pen_size=input("What size of pen do you want?")
pen_size=int(pen_size)

wn = turtle.Screen()            #create window utk turtle lukis
wn.bgcolor(background_colour)        # set the window background color

tess = turtle.Turtle()          #set nama turtle as tess
tess.color(pen_colour)              # make tess blue
tess.pensize(pen_size)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas
