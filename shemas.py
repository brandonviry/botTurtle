import turtle
import time 

# teste turtle 
turtle.reset()

turtle.goto(0, 0)
turtle.forward(100)



turtle.reset()

#trasage de shamas 2 

cases = 1
turtle.left(90)
for i in range(100) :
    turtle.forward(cases)
    turtle.left(90)
    cases+= 1
pause = input('PAUSE')