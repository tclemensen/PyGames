# Pong for Python
# Very simple PONG like game. This is NOT my original idea, but I have made a few subtle changes.

import turtle
import os
import sys
from soundFX import playSFX


# Doing some initialisation
wn = turtle.Screen()
wn.title("Pong for Py")
wn.bgcolor("black")

# Creates a window (canvas) of 800x600 and places it in the upper left corner of the screen
wn.setup(width=800, height=600, startx=100, starty=100)
wn.tracer(0)

# Scoring - Sets initial scores to 0
score_a = 0
score_b = 0

# Creating Paddle A
paddle_a = turtle.Turtle()  # Creates a new turtle for the paddle
paddle_a.speed(0)  # Sets animation speed (0=fastest)
paddle_a.shape("square")  # Defines the general shape
paddle_a.color("white")  # Sets the color

# Sets the size (5 units tall and 1 across)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

paddle_a.penup()  # Raises the "pen" so the turtle doesn't draw on the screen
paddle_a.goto(-350, 0)  # Sets the paddle in the right location

# Creating Paddle B -- Basically exactly the same as above, so I don't bother to comment every single line...
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Creating the ball -- Also basically the same as creating the paddles, with a couple of minor differences.
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Defines at what speed the ball moves across the screen. This value might have to adjust for your computer
ball.dx = .1
ball.dy = .1

# Placing the score table
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()  # Hiding the turtle, as we don't need to see it in this case
pen.goto(0, 260)  # Defines the position
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))  # Lets the turtle write text

# Functions

# Moves paddle A up


def paddle_a_up():
    y = paddle_a.ycor()  # Finds the current Y position
    y += 20  # Adds 20 to the current position, i.e. moves the paddle by 20 pixels
    paddle_a.sety(y)  # Reposition the paddle to the new position

    # Checks if your paddle is off screen. If so, put it back where it belongs
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)


# Moves paddle A down -- Basically exactly the same as above, just in the opposite direction.
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)


def paddle_b_up():  # Moves paddle B up
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)


def paddle_b_down():  # Moves paddle B down
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)


# Keyboard Binding
# Tells the window to listen for keyboard inputs
wn.listen()
# Tells the window what keys to look for, and calls the appropriate function
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    wn.update()  # Updates the window

    # Moving the ball

    # Moves the ball in the X and Y coorinate plane, according to values defined earlier
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border checking

    if ball.ycor() > 290:  # If the ball hits the top edge of the window, reverse Y direction of movement
        ball.sety(290)
        ball.dy *= -1
        # Should play a sound and kind of does, but not quite. I don't know....
        playSFX()

    if ball.ycor() < -280:  # If the ball hits the bottom edge, reverse Y direction of movement
        ball.sety(-280)
        ball.dy *= -1
        playSFX()

    # Checks to see if the ball exits the screen. If so, add point and reset.
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()  # Clears the screen momentarily to delete previous score
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))  # Updates the score for player A

    if ball.xcor() < -390:  # Same as above, just the other side.
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))  # Updates the score for player B

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50):
        ball.setx(340)  # Checks to see if the ball hits the paddle
        ball.dx *= -1  # If so, reverse x direction.
        playSFX()

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50):
        ball.setx(-340)  # See comments above...
        ball.dx *= -1
        playSFX()
