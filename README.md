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
