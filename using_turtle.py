import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("#111111")
	abdo = turtle.Turtle()
	abdo.shape("turtle")
	abdo.color("#FFFFFF")
	abdo.speed(1)
	abdo.pensize(3)
	abdo.shapesize(4)
	abdo.forward(150)
	abdo.right(90)
	abdo.forward(150)
	abdo.right(90)
	abdo.forward(150)
	abdo.right(90)
	abdo.forward(150)
	abdo.right(90)
	window.exitonclick()

draw_square()
