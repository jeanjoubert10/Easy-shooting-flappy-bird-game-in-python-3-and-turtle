# Jean & Marcel Joubert 3 Jan 2020 
# Written in osX and IDLE
# os.system afplay for sound
# Winsound for windows
# Speed may need adjustment in windows (import time, time.sleep(0.01) etc)

import turtle
import os
import random
import time

win = turtle.Screen()
win.setup(800,600)
win.bgpic('forest.gif')
win.title('Shooting flappy')
win.tracer(0) 
win.listen()

win.register_shape('b1.gif')
win.register_shape('b2.gif')
win.register_shape('gun.gif')


bird = turtle.Turtle()
bird.s = 'b1.gif'
bird.shape(bird.s)
bird.up()
bird.color('red')
bird.speed(0)
bird.goto(-400,250)
bird.dx = 3 # Windows ?0.02
bird.dy = 0
bird.state = 'flying'


cannon = turtle.Turtle()
cannon.shape('gun.gif')
cannon.shapesize(3,1)
cannon.color('blue')
cannon.up()
cannon.goto(0,-250)

bullet = turtle.Turtle()
bullet.shape('circle')
bullet.shapesize(0.5,0.5)
bullet.color('black')
bullet.up()
bullet.goto(1000,1000)
bullet.state = 'ready'

pen = turtle.Turtle()
pen.up()
pen.hideturtle()
pen.color('red')
pen.goto(200,260)
pen.write('Score: 0', align='center', font=('Courier', 24, 'normal'))

def shoot():
    if bullet.state == 'ready':
        bullet.goto(cannon.xcor()+25,-210)
        bullet.state = 'fire'
        os.system('afplay shotgun.wav&') # winsound in windows

def move_right():
    if cannon.xcor()<=350:
        cannon.goto(cannon.xcor()+40,cannon.ycor())

def move_left():
    if cannon.xcor()>=-350:
        cannon.goto(cannon.xcor()-40, cannon.ycor())

def animate():
    
    if bird.s == 'b1.gif' and counter%10==0:
        bird.s = 'b2.gif'
        bird.shape(bird.s)
    elif bird.s == 'b2.gif' and counter%10 == 0:
        bird.s = 'b1.gif'
        bird.shape(bird.s)

def flying():
    global gravity
    fly_list = [4, 5, 6,7, 8, 9, 10, 11, 12]
    bird.dy -= gravity
    
    if bird.ycor()<50:
        bird.dy = random.choice(fly_list)
    


win.onkey(shoot, 'space')
win.onkey(move_right, 'Right')
win.onkey(move_left, 'Left')

counter = 0
gravity = 0.2
score = 0

while True:
    
    counter += 1
    win.update()
    animate()

    if bird.state == 'flying':
        flying()

    bird.goto(bird.xcor()+bird.dx,bird.ycor()+bird.dy)

        
    if bird.xcor()>=400:
        bird.goto(-400,bird.ycor())

    if bullet.state == 'fire':
        bullet.goto(bullet.xcor()-1.8,bullet.ycor()+7) # 0.05 windows??
        if bullet.ycor() > 310:
            bullet.state = 'ready'

    if bullet.distance(bird) <= 30:
        os.system('afplay bird.wav&') # winsound in windows
        bird.dy = -5 # 0.03??windows
        bullet.goto(1000,1000)
        bullet.state = 'ready'
        bird.state = 'falling'
        score += 1
        pen.clear()
        pen.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))
        

    if bird.ycor() <=-320:
        bird.dy = 0
        bird.goto(-400, 250)
        bird.state = 'flying'

    #time.sleep(0.01)

    

    
