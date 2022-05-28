import turtle
wn = turtle.Screen()
wn.bgcolor("maroon")
tess = turtle.Turtle()
tess.color("turquoise")
tess.shape("circle")       #boleh tukar shape turtle
tess.speed(0)              #adjust speed 1-10
tess.pensize(6)              

dist = 5
tess.up()                     # pen up. kalau pen down, tess.down()
for _ in range(100):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(dist)          # move tess along
    tess.right(24)              # and turn her
    dist = dist + 2
wn.exitonclick()
