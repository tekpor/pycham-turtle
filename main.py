import random
import turtle


window = turtle.Screen()
window.tracer(0)
window.bgpic('wall.png')
window.setup(width=1100, height=800)
window.register_shape('ball.gif')
window.register_shape('bouncer.gif')
window.register_shape('dead.gif')
window.title('⚽️⚽️BOUNCING BALL⚽️⚽️')
ox = 0
oy = 0


def bl():
    bouncer.setx(bouncer.xcor()-20)


def br():
    bouncer.setx(bouncer.xcor()+20)


def sp():
    global ox, oy
    if ball.dx != 0 and ball.dy != 0:
        ox = ball.dx
        oy = ball.dy
        ball.dx *= 1.02
        ball.dy *= 1.02


def spr():
    ball.dx = ox
    ball.dy = oy


def en():
    if ball.dy == 0 and ball.dy == 0:
        ball.home()
        ball.shape('ball.gif')
        ball.dx = random.randint(-50, 50) / 100 * 3
        ball.dy = random.randint(-50, 50) / 100 * 5
        bouncer.goto(0, -window.window_height()/2+60)


window.listen()
window.onkeypress(bl, 'Left')
window.onkeypress(br, 'Right')
window.onkeypress(en, 'Up')
window.onkeypress(sp, 'Down')
window.onkeyrelease(spr, 'Down')

ball = turtle.Turtle()
ball.shape('ball.gif')
ball.shapesize(1.5)
ball.penup()
ball.speed(0)
ball.dx = random.randint(-50, 50)/100*5
ball.dy = random.randint(-50, 50)/100*3
ball.r = 5
bouncer = turtle.Turtle()
bouncer.shape('bouncer.gif')
bouncer.shapesize(stretch_len=15, stretch_wid=2)
bouncer.penup()
bouncer.goto(0, -window.window_height()/2+60)


dead = turtle.Turtle()
dead.shape('dead.gif')
dead.penup()
dead.goto(0, -window.window_height()/2+10)
dead.shapesize(stretch_len=window.window_width(), stretch_wid=5)
r = 20


while 1:
    window.update()
    ball.right(r)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.xcor() < -window.window_width()/2 or ball.xcor() > window.window_width()/2:
        ball.dx *= -1
    if ball.ycor()-50 < bouncer.ycor() and (bouncer.xcor()-150 < ball.xcor() < bouncer.xcor() + 150):
        ball.dy *= -1
    if ball.ycor() < -window.window_height()/2+10:
        ball.dx = 0
        ball.dy = 0
        ball.left(60)
        ball.shape('turtle')
    if ball.ycor() > window.window_height()/2:
        ball.dy *= -1
    r += 20
