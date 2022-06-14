# Basic pong game using python

import turtle
import winsound # Import to play sounds on windows

window =turtle.Screen()
window.title("Pong by Carl Nelson")
window.bgcolor("black")
window.setup(width=800, height=600)
# tracer stops update allows for faster loading
# requires manual update.
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square") # 20px by 20px
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square") # 20px by 20px
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle") # 20px by 20px
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Pen to mark score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Functions to move paddles


def paddle_1_up():
    y = paddle_1.ycor() # returns the y coordinates
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor() # returns the y coordinates
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor() # returns the y coordinates
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor() # returns the y coordinates
    y -= 20
    paddle_2.sety(y)


# Keyboard binding


window.listen()
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")


# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border control
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    # Paddle and ball collision
    if 340 < ball.xcor() < 350 and (paddle_2.ycor() + 40 > ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("thunk.wav", winsound.SND_ASYNC) # Code to play sound file

    if -340 > ball.xcor() > -350 and (paddle_1.ycor() + 40 > ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("thunk.wav", winsound.SND_ASYNC) # Code to play sound file
