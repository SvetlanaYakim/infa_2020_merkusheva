from graph import *
import math  
windowSize(550, 650)

penColor(0,115,11)
penSize(2)
brushColor("green")
polygon([(0, 300), (550, 300), #стол
         (550, 900), (0, 900)])

penColor(153,34,34)
penSize(2)
x1 = 0; y1 = 300
x2 = 550; y2 = 900
N = 10
h = (y2 - y1)/(N + 1)
y = y1 + h
for i in range(N):
    line(x1, y, x2, y)
    y += h
    
penColor(71,47,1)
penSize(2)
brushColor(171,100,29)
rectangle(0, 0, 550, 300)
    
def window(x, y, s):
    penColor(255,255,255)
    brushColor("white") #window
    rectangle(x, y, x+180/s, y+260/s)

    brushColor(2,145,217)
    rectangle(x+20/s, y+20/s, x+160/s, y+240/s)

    penColor('white')
    brushColor('white') 
    rectangle(x+85/s, y+20/s, x+95/s, y+240/s)#вертикальный переплет
    rectangle(x+18/s, y+90/s, x+160/s, y+100/s)#горизонтальный переплет


def body(x, y, s):
    penColor('black')
    penSize(1)
    oval(x+200/s, y+40/s, x+350/s, y+80/s)#tail
    oval(x, y, x+250/s, y+120/s)#body
    oval(x-10/s, y+50/s, x+25/s, y+105/s)#paw_left
    oval(x+25/s, y+90/s, x+80/s, y+120/s)#paw_right
    circle(x+210/s, y+90/s, 38/s) #paw
    oval(x+225/s, y+100/s, x+245/s, y+155/s)#paw

def head(x, y, s):
    circle(x, y, 45/s)#head
    polygon([(x+15/s, y-35/s), (x+40/s, y-50/s),#head ears
             (x+35/s, y-15/s), (x+15/s, y-35/s)])
    polygon([(x-15/s, y-35/s), (x-40/s, y-50/s),#head ears
             (x-35/s, y-15/s), (x-15/s, y-35/s)])
    
    line(x, y+22/s, x, y+28/s)#moustache
    arc(x, y+26/s, x+10/s, y+31/s, start = 180, end = 360, style = ARC)
    arc(x, y+26/s, x-10/s, y+31/s, start = 180, end = 360, style = ARC)
    
    brushColor(189,91,91)
    polygon([(x+20/s, y-35/s), (x+36/s, y-44/s),#head ears
             (x+33/s, y-22/s), (x+20/s, y-35/s)])
    polygon([(x-20/s, y-35/s), (x-36/s, y-44/s),#head ears
             (x-33/s, y-22/s), (x-20/s, y-35/s)])
    polygon([(x-5/s, y+15/s), (x+5/s, y+15/s),#nose
             (x, y+22/s), (x-5/s, y+15/s)])

def eyes(x, y, s):
    circle(x, y, 13/s) #eyes_left
    circle(x+40/s, y, 13/s) #eyes_right

    brushColor(0,0,0)
    oval(x+4/s, y-12/s, x+7/s, y+12/s)#eye pupil
    oval(x+44/s, y-12/s, x+47/s, y+12/s)#eye pupil

def eyes_flare(x, y, s):
    penSize(2)
    brushColor(250,250,250)
    penColor(250,250,250)

    arc(x, y, x+24/s, y+42/s, start = 210, end = 270, style = CHORD)#eye flare_left
    arc(x+40/s, y, x+64/s, y+42/s, start = 210, end = 270, style = CHORD)#eye flare_right 

def moustache(x, y, s):
    penColor('black')
    penSize(1)
    
    arc(x, y+5/s, x+80/s, y-15/s, start = 160, end = 70, style = ARC)#
    arc(x-20/s, y+5/s, x-100/s, y-15/s, start = 20, end = 110, style = ARC)#
     
    arc(x, y+10/s, x+80/s, y-20/s, start = 160, end = 70, style = ARC)#
    arc(x-20/s, y+10/s, x-100/s, y-20/s, start = 20, end = 110, style = ARC)#
     
    arc(x, y+12/s, x+80/s, y-25/s, start = 160, end = 70, style = ARC)#
    arc(x-20/s, y+15/s, x-100/s, y-25/s, start = 20, end = 110, style = ARC)#
       
def ball(x, y, s):
    brushColor('grey')
    circle(x, y, 35/s) #ball of wool
    penColor('grey')
    arc(x-55/s, y+25/s, x-15/s, y+38/s, start = 180, end = 360, style = ARC)#
    arc(x-85/s, y+28/s, x-55/s, y+35/s, start = 0, end = 180, style = ARC)#
    arc(x-110/s, y+28/s, x-85/s, y+33/s, start = 180, end = 360, style = ARC)#

    penSize(2)
    penColor(64, 64, 64)
    def ball_of_wool_1(x, y, s):
        m = 0 
        e = 100
        for i in range(3):
            arc(x-55/s, y-21/s, x+25/s, y+65/s, start = m, end = e, style = ARC)#
            x += 5/s; y -= 5/s; m += 10/s; e -= 10/s;
    ball_of_wool_1(x, y, s)

    def ball_of_wool_2(x, y, s):
        m = 180 
        e = 100
        for i in range(3):
            arc(x-5/s, y+58/s, x+40/s, y+1/s, start = m, end = e, style = ARC)#
            x -= 9/s; y -= 7/s; m += 10/s; e -= 10/s;
    ball_of_wool_2(x, y, s)

def cat(x, y, s):
    brushColor(255,128,0)    
    body(x-20/s, y-50/s, s)
    head(x, y, s)
    brushColor(95,212,32)
    eyes(x-20/s, y, s)
    eyes_flare(x-29/s, y-40/s, s)
    moustache(x+10/s, y+35/s, s)

window(310, 20, 1)
window(150, 20, 1.5)
window(20, 20, 2)
cat(270, 350, 1.5)
cat(50, 450, 2)
cat(270, 500, 2.5)
ball(320, 420, 1.5)
ball(120, 510, 2)
ball(320, 550, 2.5)

run()
