import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Green Design")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")

# Draw a pattern
for i in range(72):   # 72 repetitions makes a circular design
    pen.circle(100)   # draw a circle of radius 100
    pen.left(5)       # rotate a little before drawing the next circle

# Keep the window open until clicked
screen.mainloop()
