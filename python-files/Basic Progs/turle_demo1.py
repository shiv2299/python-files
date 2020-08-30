import turtle, time
turtle_screen = turtle.Turtle()
turtle_screen.shape('turtle')
colors = ['red', 'orange', 'blue', 'green', 'magenta', 'purple', 'black']

for each_color in colors:
    angle = 360 / len(colors)
    turtle_screen.color(each_color)
    turtle_screen.circle(50)
    turtle_screen.right(angle)
    turtle_screen.forward(40)


time.sleep(10)