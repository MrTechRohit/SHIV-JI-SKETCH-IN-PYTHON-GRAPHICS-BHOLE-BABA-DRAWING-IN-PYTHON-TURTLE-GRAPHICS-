#___________ WELCOME ALL OF YOU ON COMPUTER SOFT SKILLS CHANEEL __________
#......................... PYTHON PROGRAM TO DRAW SKETCH OF LORD ADIYOGI .........................

import turtle
from sketchpy import canvas
turtle.bgcolor('CORAL')
wn = turtle.Screen()
wn.setup(width=1350, height=750)

t=turtle.Turtle()

t.penup()
t.goto(-50,10)
t.pendown()
t.color('Aqua')
style = ('Bradley Hand ITC',50,'bold')
t.write('"Shiva is not a God.', font=style, align='right',move=True)
t.hideturtle()

t.penup()
t.goto(-40,-80)
t.pendown()
t.color('Aqua')
style = ('Bradley Hand ITC',55,'bold')
t.color('Lime')
t.write('He is the Universe."', font=style, align='right',move=True)
t.hideturtle()

t.penup()
t.goto(-200,-350)
t.pendown()
t.color('Black')
style = ('courier',30,'italic')
t.write('COMPUTER SOFT SKILLS', font=style, align='right', move=True)
t.hideturtle()

t.penup()
t.goto(-350,-400)
t.pendown()
style = ('Bradley Hand ITC',40,'bold')
t.write('"-ROHIT-"', font=style, align='right',move=True)
t.hideturtle()

ab = canvas.sketch_from_svg("D:\\python\\adiyogi.svg",scale=25)
ab.draw()



#______________ I HOPE YOU LIKE THIS PROGRAMMING _______________

#________________LIKE _________________SHARE _________________SUBSCRIBE ________________

