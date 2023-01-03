# Le BOT  pour minage computercraft



## Determininer du shémat de mache

Sheama en moitier parcour 

parcour 11  block dans un sens puis retourne au milieu puis 10 block dans el sens suivant :

![paterne1.PNG](E:\Porgrammation\git\botTurtle\paterne1.PNG)



vue le cicle il y aura une boucle 

![paterne2](E:\Porgrammation\git\botTurtle\paterne2.PNG)

Bon j'ai fais une représentation pour en déduire une shemas et ce'est celui au dessus 

on va dire que une case c'est 20 px 

bon pour voir le shemas en code python et turtle 

```python
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

```

résultat :

![res2](E:\Porgrammation\git\botTurtle\res2.PNG)

![paterne3](E:\Porgrammation\git\botTurtle\paterne3.PNG)

```python
marche = 3 
for i in range(1,100):
    marche*=i
    print(marche,marche//2)
```

```python
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

```

![res3](E:\Porgrammation\git\botTurtle\res3.PNG)

![paterne4](E:\Porgrammation\git\botTurtle\paterne4.png)

![paterne4-1](E:\Porgrammation\git\botTurtle\paterne4-1.PNG)

Base sur se patener j'ia crér un foli avec l'aide gpt chat :

```py


from random import randint



import wx

class ProgressFrame(wx.Frame):
    def __init__(self, parent, title, max_value):
        wx.Frame.__init__(self, parent, title=title)

        # Créer la barre de progression
        self.gauge = wx.Gauge(self, range=max_value)



        # Créer le gestionnaire de disposition
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.gauge, 0, wx.EXPAND)
      

        self.SetSizer(sizer)
        self.Fit()

    def update_progress(self,value):
         frame.gauge.SetValue(value)


import datetime


import turtle
turtle.bgcolor("black")
# 0
x=0
y= 0
turtle.goto(x, y)



def shemat41(color, marche):

    turtle.color(color)
    for i in range(1, 5):

        turtle.forward(marche)
        turtle.backward(marche//2)
        # Returns true if the request was successful.
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


# def goBottomToTop(marche):
#     turtle.right(90)
#     turtle.forward(marche//2)
#     turtle.right(180)
#     turtle.forward(marche)
#     turtle.right(90)
#     turtle.forward(marche//2)
#     turtle.left(90)
#     turtle.forward(marche//2)

# def goBottomToRight(marche):
#     turtle.right(90)
#     turtle.forward(marche//2)
#     turtle.right(180)
#     turtle.forward(marche)
#     turtle.right(90)
#     turtle.forward(marche//2)
#     turtle.right(90)
#     turtle.forward(marche//2)
#     turtle.left(90)
#     turtle.forward(marche//2)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "purple", "pink", "brown", "gray"]


shemat41("red", 100)

lst = [goBottomToLeft(100), goLeftToTop(
    100), goTopToRight(100), goRightToBottom(100)]
# Créer l'application
app = wx.App()
frame = ProgressFrame(None, "Opération en cours", 100)
frame.Show()

for i in range(1,100):
    # goBottomToRight(100)
    choix = randint(1, len(lst)-1)


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
  

    c = colors[randint(0,len(colors)-1)]

    frame.update_progress(i)  


    turtle.color(c)

# Obtenir la date et l'heure actuelles
now = datetime.datetime.now()

# Générer le nom de fichier
filename = f"Resultat de turtle_{now.year}_{now.month}_{ now.day}_{now.hour}_{ now.minute}.eps"

turtle.getscreen().getcanvas().postscript(file=filename)



import tkinter.messagebox

# Afficher une boîte de dialogue avec un message
tkinter.messagebox.showinfo("ETAT DU TRASAGE", "FIN")




```



![res4-1](E:\Porgrammation\git\botTurtle\res4-1.PNG)

bon vue la folie tu turc  j'ai fait une code de base :

```python
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






```

conversion 

```lua

local shemat41 = function(marche) 
    for i = 1,5  do
        turtle.forward(marche)
        turtle.backward(marche//2)
        turtle.turnLeft(90)
    end
end

local goBottomToLeft = function(marche)
    turtle.turnRight(90)
    turtle.forward(marche//2)
    turtle.turnRight(180)
    turtle.forward(marche)
    turtle.turnLeft(90)
    turtle.forward(marche//2)
end



local goLeftToTop = function(marche)
    turtle.turnRight(180)
    turtle.forward(marche)
    turtle.turnLeft(90)
    turtle.forward(marche//2)
end


local goTopToRight = function(marche)

    turtle.turnRight(180)
    turtle.forward(marche)
    turtle.turnLeft(90)
    turtle.forward(marche//2)

end



local goRightToBottom = function(marche)
    turtle.turnRight(180)
    turtle.forward(marche)
    turtle.turnLeft(90)
    turtle.forward(marche//2)
end



shemat41(100)

for i=1,100 do
    choix = math.random(1, 4)

    if choix == 1 then
        goBottomToLeft(100)
    elseif choix == 2 then
        goBottomToLeft(100)
        goLeftToTop(100)
    elseif choix == 3 then
        goBottomToLeft(100)
        goLeftToTop(100)
        goTopToRight(100)
    elseif choix == 4 then
        goBottomToLeft(100)
        goLeftToTop(100)
        goTopToRight(100)
        goRightToBottom(100)
    end

end

```

bon vue les proof que j'ai fait et mes discution chatGPT je pesnse que j ai eu d'autre possiibliter 

base sur x y z

