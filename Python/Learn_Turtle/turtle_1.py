import imaplib
import turtle
t = turtle.Turtle()
turtle.bgcolor("yellow")

# turtle.bgpic(r"C:\Users\USER\Pictures\wallpaper\5.jpg")

# turtle.screensize(900, 300)
turtle.title("turtle program")

"""screen = turtle.getscreen()
turtle.forward(200)
turtle.backward(200)
turtle.right(90)
turtle.backward(100)
turtle.left(45)"""

"""# creating 'A'
turtle.right(90)
turtle.backward(100)
turtle.right(90)
turtle.backward(40)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.backward(40)
turtle.forward(40)
turtle.right(90)
turtle.forward(50)"""

"""# turtle.circle(70)
# turtle.dot(50)
turtle.pensize(2) # size of pen like how bold it is
turtle.pencolor("red") # what is the of the pen
turtle.forward(100)
turtle.fillcolor("red") # filling color in arrow
turtle.shapesize(2,3,5) # size of the arrow
turtle.color("blue", "grey") # changing coloir at once of outline of the color and filling inside it 

# changing turtle shape 
turtle.shape("turtle")
turtle.shape("circle")
# turtle.shape("dot")

# changing speed of pen

turtle.speed(3)
turtle.forward(50)
turtle.speed(7)
turtle.forward(100)"""

turtle.setposition(-100, 9)
turtle.shapesize(4,4,4)
turtle.shape("turtle")
turtle.begin_fill()
turtle.forward(200)
turtle.end_fill()

turtle.mainloop() 