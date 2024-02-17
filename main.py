import turtle
import random
import time

delay = 0.1
score = 0
highestscore = 0

# Snake Body
bodies = []

# Getting a screen canvas
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=600, height=600)

# Create Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.goto(0, 200)
food.st()

# Score Board
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("green")
sb.penup()
sb.goto(-250, -250)
sb.ht()
sb.write("Score: 0  | Highest Score: 0")

def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def movestop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event Handling --Key Mapping
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

# Main loop
while True:
    s.update()  # Update the screen

    # check collision with border
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    # Check collision with food
    if head.distance(food) < 20:
        # move the food to a new random place
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase the Length of the Snake
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("red")
        body.penup()
        bodies.append(body)  # append new body

        # Increase the Score
        score += 10

        # Change delay
        delay -= 0.001

        # Update the Highest Score
        if score > highestscore:
            highestscore = score

        sb.clear()
        sb.write("Score: {}  |  Highest Score: {}".format(score, highestscore))

    # move the snake bodies
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide bodies
            for b in bodies:
                b.hideturtle()
            bodies.clear()

            score = 0
            delay = 0.1

            # Update Score Board
            sb.clear()
            sb.write("Score: {}  |  Highest Score: {}".format(score, highestscore))

    time.sleep(delay)

turtle.mainloop()
