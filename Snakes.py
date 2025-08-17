import turtle
import time
import random

delay = 0.1
segment = []
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snakes Game")
wn.bgcolor("green")
wn.setup(width=700,height=700)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,200)

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

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Your Score: 0   High Score: 0",align="center",font=("Arial", 20))

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

while True:
    if len(segment) == 0:
        first_segment = turtle.Turtle()
        first_segment.speed(0)
        first_segment.shape("square")
        first_segment.color("black")
        first_segment.penup()
        first_segment.goto(0,0)
        segment.append(first_segment)

    if head.xcor() > 330 or head.xcor() < -330 or head.ycor() > 330 or head.ycor() < -330:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for seg in segment:
            seg.hideturtle()
        segment.clear()
        score = 0
        pen.clear()
        pen.write("Your Score: {}   High Score: {}".format(score,high_score),align="center",font=("Arial", 20))
        delay = 0.1

    if head.distance(food) < 20:
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        food.goto(x,y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        new_segment.goto(0,0)
        segment.append(new_segment)
        score += 10
        if score >= high_score:
            high_score = score
        pen.clear()
        pen.write("Your Score: {}   High Score: {}".format(score,high_score),align="center",font=("Arial", 20))
        delay -= 0.001

    for i in range(len(segment) - 1, 0, -1):
        x = segment[i - 1].xcor()
        y = segment[i - 1].ycor()
        segment[i].goto(x, y)
    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x, y)
    wn.update()
    move()
    for seg in segment:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for seg in segment:
                seg.hideturtle()
            segment.clear()
            score = 0
            pen.clear()
            pen.write("Your Score: {}   High Score: {}".format(score,high_score),align="center",font=("Arial", 20))
            delay = 0.1
    time.sleep(delay)

wn.mainloop()
