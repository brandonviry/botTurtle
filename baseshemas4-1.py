from random import randint
import turtle

turtle.bgcolor("black")

x=0
y= 0
turtle.goto(x, y)



def shemat41(color, marche):

    turtle.color(color)
    for i in range(1, 5):

        turtle.forward(marche)
        turtle.backward(marche//2)
        turtle.left(90)


def goBottomToLeft(marche):
    turtle.right(90)
    turtle.forward(marche//2)
    turtle.right(180)
    turtle.forward(marche)
    turtle.left(90)
    turtle.forward(marche//2)


def goLeftToTop(marche):
    turtle.right(180)
    turtle.forward(marche)
    turtle.left(90)
    turtle.forward(marche//2)


def goTopToRight(marche):
    turtle.right(180)
    turtle.forward(marche)
    turtle.left(90)
    turtle.forward(marche//2)


def goRightToBottom(marche):
    turtle.right(180)
    turtle.forward(marche)
    turtle.left(90)
    turtle.forward(marche//2)




shemat41("red", 100)

for i in range(1,100):
   
    choix = randint(1,4-1)


    if choix == 1:
        goBottomToLeft(100)


    if choix == 2:
        goBottomToLeft(100)
        goLeftToTop(100)


    if choix == 3:
        goBottomToLeft(100)
        goLeftToTop(100)
        goTopToRight(100)
 

    if choix == 4 :
        goBottomToLeft(100)
        goLeftToTop(100)
        goTopToRight(100)
        goRightToBottom(100)
  
input("Appuyer une touche pour arreter ........ ")





