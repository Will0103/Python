import turtle
turtle.reset()
turtle.showturtle()
turtle.speed('fastest')
turtle.up()
turtle.setx(-400)
turtle.down()
turtle.fd(800)
turtle.up()
turtle.goto(0,-400)
turtle.down()
turtle.sety(400)
turtle.up()

x=-400
y=(1/200)*x**2
turtle.goto(x,y)
turtle.down()
for i in range(0,800,1):
    x=x+i
    y=(1/200)*x**2
    turtle.goto(x,y)