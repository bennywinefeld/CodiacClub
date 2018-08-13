from turtle import *
import time
t = Turtle()

t.speed(10)
t.color('red', 'yellow')
t.begin_fill()
origPos = [int(xy) for xy in t.pos()]
print(origPos)
while True:
  t.forward(200)
  t.left(170)
  #print(t.pos())
  pos = [int(xy) for xy in t.pos()]
  if pos == origPos:
    break
t.end_fill()
