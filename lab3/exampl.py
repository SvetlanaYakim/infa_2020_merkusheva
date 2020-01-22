from graph import *
import math  
windowSize(550, 650)

penColor(0,115,11)
penSize(2)
brushColor("green")
polygon([(50, 300), (550, 300), #стол
         (550, 900), (50, 900)])

penColor(153,34,34)
penSize(2)
x1 = 50; y1 = 300
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
polygon([(50, 10), (550, 10),
         (550, 300), (50, 300)])
penColor(255,255,255)
penSize(1)
brushColor("white") #window
polygon([(310, 20), (490, 20),
         (490, 280), (310, 280)])

penColor(2,145,217)
penSize(1)
brushColor(2,145,217)
polygon([(330, 40), (470, 40),
         (470, 260), (330, 260)])

penColor('white')
penSize(1)
brushColor('white') #вертикальный переплет
polygon([(395, 40), (405, 40),
         (405, 260), (395, 260)])

penColor('white')
penSize(1)
brushColor('white') #горизонтальный переплет
polygon([(330, 110), (470, 110),
         (470, 120), (330, 120)])

penColor('black')
penSize(1)
brushColor(255,128,0)

oval(350, 390, 500, 430)#tail

oval(150, 350, 400, 470)#body
oval(140, 400, 175, 455)#paw_left
oval(175, 440, 230, 470)#paw_right
circle(170, 400, 45)#head
circle(360, 440, 38) #paw
oval(375, 450, 395, 505)#paw
polygon([(185, 365), (210, 350),#head ears
         (205, 385), (185, 365)])
polygon([(155, 365), (130, 350),#head ears
         (135, 385), (155, 365)])
line(170, 422, 170, 428)#moustache
arc(170, 426, 180, 431, start = 180, end = 360, style = ARC)
arc(170, 426, 160, 431, start = 180, end = 360, style = ARC)

penSize(1)
brushColor('grey')
def moustache(x1, y1, x2, y2):
    for i in range(3):
        arc(x1, y1, x2, y2, start = 160, end = 70, style = ARC)#
        arc(x1-20, y1, x2-180, y2, start = 20, end = 110, style = ARC)#
        y1 += 0; y2 += 5;       
moustache(180, 435, 260, 412)
circle(280, 520, 35) #ball of wool
penColor('grey')
arc(225, 545, 265, 558, start = 180, end = 360, style = ARC)#
arc(195, 548, 225, 555, start = 0, end = 180, style = ARC)#
arc(170, 548, 195, 553, start = 180, end = 360, style = ARC)#

penSize(2)
penColor(64, 64, 64)
def ball_of_wool_1(x1, y1, x2, y2, s, e):
    for i in range(3):
        arc(x1, y1, x2, y2, start = s, end = e, style = ARC)#
        x1 += 5; y1 -= 5; x2 += 3; y2 -= 4; s += 10; e -= 10;
ball_of_wool_1(225, 499, 305, 585, 0, 100)

def ball_of_wool_2(x1, y1, x2, y2, s, e):
    for i in range(3):
        arc(x1, y1, x2, y2, start = s, end = e, style = ARC)#
        x1 -= 9; y1 -= 7; x2 -= 5; y2 -= 6; s += 10; e -= 10;
ball_of_wool_2(275, 578, 320, 521, 180, 100)


penColor('black')
penSize(1)
brushColor(189,91,91)
polygon([(190, 365), (206, 356),#head ears
         (203, 378), (190, 365)])

polygon([(150, 365), (134, 356),#head ears
         (137, 378), (150, 365)])

polygon([(165, 415), (175, 415),#nose
         (170, 422), (165, 415)])

    
brushColor(95,212,32)
circle(150, 400, 13) #eyes_left
circle(190, 400, 13) #eyes_right

penColor(0,0,0)
penSize(1)
brushColor(0,0,0)
oval(154, 388, 157, 412)#eye pupil
oval(194, 388, 197, 412)#eye pupil

penSize(2)
brushColor(250,250,250)
penColor(250,250,250)

arc(141, 360, 165, 402, start = 210, end = 270, style = CHORD)#eye flare_left
arc(181, 360, 205, 402, start = 210, end = 270, style = CHORD)#eye flare_right




run()
