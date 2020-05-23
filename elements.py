from turtle import Turtle

class Objects:

    def __init__(self):
        # Paddle A
        self.paddle_a = Turtle("square")
        self.init_paddle_a()

        self.pen= Turtle()
        self.init_pen()

        self.score_a = 0
        self.score_b = 0

        # Paddle B
        self.paddle_b = Turtle("square")
        self.init_paddle_b()

        # Ball
        self.ball = Turtle("circle")
        self.init_ball()

    def init_paddle_a(self):

        paddle_a_x = -350

        self.paddle_a.speed(0)
        self.paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_a.color('green')
        self.paddle_a.penup()
        self.paddle_a.setx(paddle_a_x)

    def init_paddle_b(self):
        paddle_b_x = 350

        self.paddle_b.speed(0)
        self.paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_b.color('red')
        self.paddle_b.penup()
        self.paddle_b.setx(paddle_b_x)

    def init_ball(self):
        self.ball.speed(0)
        self.ball.color('cyan')
        self.ball.penup()
        self.ball.home()
        self.ball.dx=0.08
        self.ball.dy=-0.08

    def init_pen(self):
        self.pen.speed(0)
        self.pen.color("blue")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0,260)
        self.pen.write("Player A:0  |  Player B:0",align="center",font=("Courier",24,"normal"))

    def paddle_a_up(self):
        y = self.paddle_a.ycor() + 20
        self.paddle_a.sety(y)

    def paddle_a_down(self):
        y = self.paddle_a.ycor() - 20
        self.paddle_a.sety(y)

    def paddle_b_up(self):
        y = self.paddle_b.ycor() + 20
        self.paddle_b.sety(y)

    def paddle_b_down(self):
        y = self.paddle_b.ycor() - 20
        self.paddle_b.sety(y)