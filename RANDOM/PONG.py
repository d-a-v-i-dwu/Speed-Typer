"""
PONG Following a tutorial
Author: David Wu
"""
import turtle

#Game window
win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)


#Paddle movement
def paddle_a_up():
    if paddle_a.ycor() < 225:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

win.listen()
win.onkeypress(paddle_a_up, "w")

def paddle_a_down():
    if paddle_a.ycor() > -225:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

win.listen()
win.onkeypress(paddle_a_down, "s")

def paddle_b_up():
    if paddle_b.ycor() < 225:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

win.listen()
win.onkeypress(paddle_b_up, "Up")

def paddle_b_down():
    if paddle_b.ycor() > -225:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

win.listen()
win.onkeypress(paddle_b_down, "Down")


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Georgia", 24, "normal"))

#Main game loop
while True:
    win.update()

    #Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Georgia", 24, "normal"))

    if ball.xcor() < -390:
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Georgia", 24, "normal"))


    #Paddle collision
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1