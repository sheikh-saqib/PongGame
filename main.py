import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.title("The Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with both Paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when r paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        r_paddle.paddle_reset()
        l_paddle.paddle_reset()
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()

    # Detect when l paddle misses
    if ball.xcor() < -340:
        ball.reset_pos()
        r_paddle.paddle_reset()
        l_paddle.paddle_reset()

        scoreboard.r_score += 1
        scoreboard.update_scoreboard()
screen.exitonclick()
