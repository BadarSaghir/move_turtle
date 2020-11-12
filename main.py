# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import Turtle as T, Screen

turtle = T()
screen = Screen()


def move():

    turtle.forward(20)


screen.listen()
screen.onkey(key='w', fun=lambda: move())
screen.onkey(key='s', fun=lambda: turtle.backward(20))
screen.onkey(key='a', fun=lambda:  turtle.left(20))
screen.onkey(key='d', fun=lambda: turtle.right(20))
screen.onkey(key='c', fun=lambda: [turtle.clear(), turtle.reset()]
           )
screen.exitonclick()
