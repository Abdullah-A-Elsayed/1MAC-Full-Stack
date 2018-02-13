import turtle
window = turtle.Screen()
window.bgcolor("#111111")
abdo = turtle.Turtle()
def draw_square():
	abdo.shape("turtle")
	abdo.color("#FFFFFF")
	abdo.speed(6)
	abdo.pensize(3)
	abdo.shapesize(4)
	i=0
	while (i<4):
		abdo.forward(150)
		abdo.right(90)
		i+=1
i =0
while i<36:
	draw_square()
	abdo.right(10)
	i+=1
window.exitonclick()
