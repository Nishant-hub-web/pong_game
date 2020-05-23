from turtle import Screen
import elements
import os

# Windows settings

window = Screen()
window.title("Pong game")
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

paletka_1 = elements.Objects()

window.onkeypress(paletka_1.paddle_a_up, "Up")
window.onkeypress(paletka_1.paddle_a_down, "Down")
window.onkeypress(paletka_1.paddle_b_up, "Left")
window.onkeypress(paletka_1.paddle_b_down, "Right")
window.listen()

while True:
    window.update()

    paletka_1.ball.setx(paletka_1.ball.xcor()+paletka_1.ball.dx)
    paletka_1.ball.sety(paletka_1.ball.ycor() + paletka_1.ball.dy)

    if paletka_1.ball.ycor() > 290:
        paletka_1.ball.sety(290)
        paletka_1.ball.dy += -0.18
        os.system("aplay bounce.wav&")

    if paletka_1.ball.ycor() < -290:
        paletka_1.ball.sety(-290)
        paletka_1.ball.dy += 0.18
        os.system("aplay bounce.wav&")

    if paletka_1.ball.xcor() > 390:
        paletka_1.ball.goto(0,0)
        paletka_1.ball.dx += -0.18
        paletka_1.score_a+=1
        paletka_1.pen.clear()
        os.system("aplay bounce.wav&")
        paletka_1.pen.write(f"Player A:{paletka_1.score_a}  |  Player B:{paletka_1.score_b}",align="center",font=("Courier",24,"normal"))


    if paletka_1.ball.xcor() < -390:
        paletka_1.ball.goto(0,0)
        paletka_1.ball.dx += 0.18
        paletka_1.score_b += 1
        paletka_1.pen.clear()
        os.system("aplay bounce.wav&")
        paletka_1.pen.write(f"Player A:{paletka_1.score_a}  |  Player B:{paletka_1.score_b}",align="center",font=("Courier",24,"normal"))


    #stop the paddles
    if paletka_1.paddle_a.ycor()+50 > 290:
        paletka_1.paddle_a.sety(247)

    if paletka_1.paddle_a.ycor()-50 < -290:
        paletka_1.paddle_a.sety(-245)

    if paletka_1.paddle_b.ycor()+50 > 290:
        paletka_1.paddle_b.sety(247)

    if paletka_1.paddle_b.ycor()-50 < -290:
        paletka_1.paddle_b.sety(-245)


    #collision
    if (paletka_1.ball.xcor() >330 and paletka_1.ball.xcor() <350 ) and (paletka_1.ball.ycor() < paletka_1.paddle_b.ycor()+50 and paletka_1.ball.ycor() > paletka_1.paddle_b.ycor()-50):
        paletka_1.ball.setx(330)
        paletka_1.ball.dx *= -1
        os.system("aplay bounce.wav&")

    if (paletka_1.ball.xcor() < -330 and paletka_1.ball.xcor() > -350) and (
            paletka_1.ball.ycor() < paletka_1.paddle_a.ycor() + 50 and paletka_1.ball.ycor() > paletka_1.paddle_a.ycor() - 50):
        paletka_1.ball.setx(-330)
        paletka_1.ball.dx *= -1
        os.system("aplay bounce.wav&")