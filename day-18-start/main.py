import turtle
import random

colors=["#0000FF","#FF0000","#800080","#00FA9A"]

tim=turtle.Turtle()
turtle.colormode(255)

tim.speed("fastest")

def rand_color():
    r= random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tup_of_col= (r,g,b)
    return tup_of_col



for i in range(100):
    tim.color(rand_color())
    tim.circle(100)
    tim.left(10)
    tim.circle(100)
    tim.tilt(30)
    tim.circle(100)


















screen=Screen()
screen.exitonclick()