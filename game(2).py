# Nokia-style Snake Game using turtle (works in IDLE)
# Controls: Arrow keys (Up, Down, Left, Right)

import turtle
import time
import random

# Game settings
DELAY = 0.10         # lower = faster snake
STEP = 20            # grid step size (snake block size)
WIDTH = 600          # window width
HEIGHT = 600         # window height
MARGIN = 20          # inner margin from wall

# Setup screen
wn = turtle.Screen()
wn.title("Nokia Snake")
wn.bgcolor("black")
wn.setup(width=WIDTH, height=HEIGHT)
wn.tracer(0)  # manual updates for smooth animation

# Draw border
border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.color("gray")
border.pensize(3)
border.penup()
left = -WIDTH // 2 + MARGIN
right = WIDTH // 2 - MARGIN
bottom = -HEIGHT // 2 + MARGIN
top = HEIGHT // 2 - MARGIN

border.goto(left, top)
border.pendown()
border.goto(right, top)
border.goto(right, bottom)
border.goto(left, bottom)
border.goto(left, top)
border.penup()

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake body list
segments = []

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)

def random_food_position():
    # Place food aligned to the STEP grid within bounds
    x = random.randrange(left + STEP, right - STEP + 1, STEP)
    y = random.randrange(bottom + STEP, top - STEP + 1, STEP)
    return x, y

food.goto(*random_food_position())

# Score display
score = 0
high_score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, top - 30)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 16, "normal"))

def update_score():
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 16, "normal"))

# Controls
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

def move():
    x, y = head.xcor(), head.ycor()
    if head.direction == "up":
        head.sety(y + STEP)
    elif head.direction == "down":
        head.sety(y - STEP)
    elif head.direction == "left":
        head.setx(x - STEP)
    elif head.direction == "right":
        head.setx(x + STEP)

def reset_game():
    global score, segments
    time.sleep(0.8)
    head.goto(0, 0)
    head.direction = "stop"
    # Hide segments off-screen and clear
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    score = 0
    update_score()
    food.goto(*random_food_position())

def is_wall_collision(x, y):
    return x < left or x > right or y < bottom or y > top

def is_self_collision():
    for segment in segments:
        if segment.distance(head) < STEP / 2:
            return True
    return False

# Main game loop
while True:
    wn.update()

    # Check wall collision
    if is_wall_collision(head.xcor(), head.ycor()):
        reset_game()

    # Check self collision
    if is_self_collision():
        reset_game()

    # Check food collision
    if head.distance(food) < STEP / 2:
        # Move food to new position
        food.goto(*random_food_position())

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("lime green")
        new_segment.penup()
        segments.append(new_segment)

        # Update score
        score += 10
        if score > high_score:
            high_score = score
        update_score()

    # Move body segments from tail to head
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # First segment follows head
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    # Move head
    move()

    time.sleep(DELAY)
