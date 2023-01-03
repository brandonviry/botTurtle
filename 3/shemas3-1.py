# Returns true if the request was successful.
import turtle
marche = 3
turtle.goto(0, 0)
for i in range(1,100) :
    marche*= 2
    turtle.forward(marche)
    turtle.backward(marche//2)
    # Returns true if the request was successful.
    turtle.left(90)
pause = input('PAUSE')

