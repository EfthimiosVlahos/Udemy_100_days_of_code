from turtle import Turtle, Screen
import random


screen=Screen()
screen.setup(width=500,height=400)
user_bet= screen.textinput(title="Make your bet: ", prompt="Which turtle will win the race? Enter a color: ")
colors= ["red", "orange", "yellow", "green", "blue", "purple"]
names=["tim","tom","jim","bob","nick","pook"]

for name in names:
    for color in colors:
        name=Turtle(shape="turtle")
        name.color(colors[random.randint(0,5)])
        name.penup()

tim.goto()
tom.goto(x=200,y=20)
jim.goto(x=200,y=-20)
bob.goto(x=200,y=40)
nick.goto(x=200,y=-40)
pook.goto(x=200,y=60)

















screen.exitonclick()