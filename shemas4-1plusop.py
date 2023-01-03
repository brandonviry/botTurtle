

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



