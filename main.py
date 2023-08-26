
import time
import turtle
import os
import random
import cmath
import numpy as np
from sys import platform



def each(lt):
    for k in lt:
        return k

def clear():
    if platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
clear()
board = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

def randomchoose():
    x = random.randint(0,3)
    y = random.randint(0,3)
    while not (board[x])[y] == 0:
        x = random.randint(0,3)
        y = random.randint(0,3)
    if random.randint(0,4) == 4:
        (board[x])[y] = 4
    else:
        (board[x])[y] = 2




pos = complex(0,0)

def rotate(direction):
    global board
    if direction == 'right':
        board = board
    if direction == 'left':
        for each in board:
            each = each.reverse()
    if direction == 'up':
        board = ((np.array(board)).transpose()).tolist()
        for each in board:
            each = each.reverse()
    if direction == 'down':
        board = ((np.array(board)).transpose()).tolist()
def rerotate(direction):
    global board
    if direction == 'right':
        board = board
    if direction == 'left':
        for each in board:
            each = each.reverse()
    if direction == 'up':
        for each in board:
            each = each.reverse()
        board = ((np.array(board)).transpose()).tolist()
    if direction == 'down':
        board = ((np.array(board)).transpose()).tolist()

def move(direction):
    def square(x,y):
        return (board[int(pos.real+x)])[int(pos.imag+y)]
    def setsquare(x,y,z):
        (board[int(pos.real+x)])[int(pos.imag+y)] = z
    global board
    rotate(direction)
    pos = complex(0,0)
    for i in board:
        for j in i:
            if not j == 0:
                if pos.imag <= 2:
                    if square(0,1) == 0:
                        setsquare(0,1,j)
                        setsquare(0,0,0)
            pos += complex(0,1)
        r = pos.real
        pos = complex(r+1,0)
    rerotate(direction)

def add(direction):
    def square(x,y):
        return (board[int(pos.real+x)])[int(pos.imag+y)]
    def setsquare(x,y,z):
        (board[int(pos.real+x)])[int(pos.imag+y)] = z
    rotate(direction)
    pos = complex(0,0)
    for i in board:
        i.reverse()
        i2 = []
        for r in i:
            i2.append(r)
        for j in i:
            if pos.imag <= 2:
                if square(0,1) == square(0,0) and square(0,0) == (i2[int(pos.imag)]):
                    setsquare(0,0,0)
                    setsquare(0,1,2*j)
            pos += complex(0,1)
        for k in i:
            k = int(k)
        i.reverse()
        r = pos.real
        pos = complex(r+1,0)
    rerotate(direction)

def turn(direction):
    for t in range(0,4):               
        move(direction)
    add(direction)
    for t in range(0,4):
        move(direction)

wn = turtle.Screen()
wn.setup(height = 500,width = 500)
wn.bgcolor('white')
for i in range(1,17):
    turtle.addshape(str('assets/2048_'+str(2**i)+'.gif'))
turtlelist = []
def display(b):
    global turtlelist
    for each in turtlelist:
        each.hideturtle()
    y1 = 0
    for y in b:
        x1 = 0
        for x in y:
            xc = -250+62.5 + 125*x1
            yc = 250 - 62.5 - 125*y1
            new = turtle.Turtle()
            if not x == 0:
                new.shape(str('assets/2048_'+str(x)+'.gif'))
            elif x == 0:
                new.shape('square')
                new.color('grey')
            new.shapesize(4,4)
            new.speed(0)
            new.penup()
            new.setpos(xc,yc)
            new.forward(0)
            turtlelist.append(new)
            x1 += 1
        y1 += 1


def setequal(one):
    k = []
    for each in one:
        k2 = []
        for e in each:
            k2.append(e)
        k.append(k2)
    return(k)


def turnright():
    oldboard = setequal(board)
    turn('right')
    if not oldboard == board:
        randomchoose()
        time.sleep(0.1)
        display(board)
def turnleft():
    oldboard = setequal(board)
    turn('left')
    if not oldboard == board:
        randomchoose()
        time.sleep(0.1)
        display(board)
def turndown():
    oldboard = setequal(board)
    turn('down')
    if not oldboard == board:
        randomchoose()
        time.sleep(0.1)
        display(board)
def turnup(): #Functions used in the onkeypress method cannot have arguments, so function must be made 4 times
    oldboard = setequal(board)
    turn('up')
    if not oldboard == board:
        randomchoose()
        time.sleep(0.1)
        display(board)
        print(each(board))


wn.onkeypress(turnright,'Right')
wn.onkeypress(turnleft,'Left')
wn.onkeypress(turndown,'Down')
wn.onkeypress(turnup,'Up')
wn.listen()



wn.tracer(0)

tocontinue = True
randomchoose()
randomchoose()
display(board)
clear()
while tocontinue:
    wn.update()
    tocontinue = False
    for each in board:
        if 0 in each:
            tocontinue = True