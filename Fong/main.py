from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

##making screen of 600x800
screen =  Screen()
screen.bgcolor("black")
screen.setup(height= 600, width= 800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #collision with the wall
    if ball.ycor()>280 or ball.xcor()<-280:
        ball.bounce_y()

    #collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_position()

    if ball.xcor()<-380:
        ball.reset_position()

screen.exitonclick()