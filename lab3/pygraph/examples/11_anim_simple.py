# coding: utf-8
"""
Использование графического модуля graph.py.
GR_ANIM_SIMPLE - простая анимация
  (C) К. Поляков, 2017-2018
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *

def update():
  moveObjectBy(obj, 5, 0)
  if xCoord(obj) >= 400-20:

    moveObjectBy(obj, -50, 0)
def keyPressed(event):
  if event.keycode == VK_ESCAPE:
    close()

def smail(x, y):
  penColor("black")
  brushColor("yellow")
  circle(x, y, 20)
  brushColor("black")
  circle(x+8, y-5, 20/6)
  circle(x-8, y-5, 20/6)
 
brushColor("blue")
rectangle(0, 0, 400, 400)
x = 100
y = 100
penColor("yellow")
brushColor("yellow")
#obj = rectangle(x, y, x+20, y+20)
obj = smail(x, y)
onKey(keyPressed)
onTimer(update, 50)

run()
