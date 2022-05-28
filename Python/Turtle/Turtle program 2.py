#cara guna 'for' loop
import turtle
wn = turtle.Screen()

elan = turtle.Turtle()

distance = 5
for _ in range(50):
    elan.forward(distance)
    elan.right(24)
    distance = distance + 2
wn.exitonclick()
