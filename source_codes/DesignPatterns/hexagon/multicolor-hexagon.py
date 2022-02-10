# @KhomZ
# Today I'm gonna show you 
# How to Design a Multicolored hexagon

import turtle
# ikhomkodes

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)

for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)


# Let's see how this code designs the multicolored hexagon

# let's run it ............

# Amazing isn't it??????????

# ikhomkodes
# @author: Khom 

# hope you enjoy it!!!!!
# have a great day ahead
# seeyaaaaa!!!!!!