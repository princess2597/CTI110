#CTI - 110
#P4LAB: Nested Loop 
#Toneshia Ried
#March 24, 2018

import turtle
win = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.pensize(5)
t.pencolor("purple")

for i in range(0,12):
    t.left (90)
    t.forward(150)
    t.forward(-50)
    t.left(50)
    t.forward(40)
    t.forward(-40)
    t.right(100)
    t.forward(40)
    t.forward(-40)
    t.left(50)
    t.forward(-100)
    t.right(60)

win.mainloop()
