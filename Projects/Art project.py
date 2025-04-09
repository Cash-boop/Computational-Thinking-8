import turtle
#keep this here for turtle code

t = turtle.Turtle()
t.speed(10)
#turtle speed and 0 makes it go fast 
t.penup()
t.goto(-50, -50)
t.color("black")
t.pendown()
#this is where the colors are

colors = ["purple","gray","black"]


for i in range( 125 ):
    t.color( colors[ 2 ] )
    t.forward( 100 )
    t.left( 120 + 1)

for i in range( 125 ):
    t.color( colors[ 1 ] )
    t.forward( 200 )
    t.left( 120 + 1)

for i in range( 125 ):
    t.color( colors[ 0 ] )
    t.forward( 300 )
    t.left( 120 + 1)

for i in range( 125 ):
    t.color( colors[ 2 ] )
    t.forward( 400 )
    t.left( 120 + 1)

for i in range( 125 ):
    t.color( colors[ 1 ] )
    t.forward( 400 )
    t.left( 120 + 1)

turtle.exitonclick()

