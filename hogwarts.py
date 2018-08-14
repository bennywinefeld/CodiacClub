# Hogwarts and Harry Potter 

import turtle
wn = turtle.Screen()
wn.bgcolor("light blue")
harry = turtle.Turtle()
harry.speed(8)

# Move to bottom left corner of window
harry.penup()
harry.backward(300)
harry.right(90)
harry.forward(300)
harry.left(180) 

# 2 towers
for i in range(2):
    # brown rectangular base of tower
    harry.pendown()
    harry.fillcolor("brown")
    harry.begin_fill()
    for m in range(2):
        harry.forward(400)
        harry.right(90)
        harry.forward(150)
        harry.right(90)
    harry.end_fill()

    # move into position to draw tip of tower
    harry.penup()
    harry.forward(400)
    harry.left(90)
    harry.pendown()

    # blue triangular tip of tower
    harry.fillcolor("blue")
    harry.begin_fill()
    harry.forward(50)
    harry.right(120)
    for v in range (3):
        harry.forward(250)
        harry.right(120)
    harry.end_fill()

    # move into position to draw windows
    harry.penup()
    harry.right(60)
    harry.forward(90)
    harry.right(90)
    harry.forward(50)

    # 6 blue windows on each tower
    for o in range(3):
        for l in range(2):
            harry.pendown()
            harry.begin_fill()
            # make one window
            for d in range(2):
                harry.forward(50)
                harry.left(90)
                harry.forward(20)
                harry.left(90)
            harry.end_fill()
            harry.penup()
            # move to the right to make another window
            harry.left(90)
            harry.forward(50)
            harry.right(90)
        # move down to make next row of windows
        harry.left(90)
        harry.backward(100)
        harry.right(90)
        harry.forward(75)

    # move in position to draw second tower
    harry.penup()
    harry.forward(125)
    harry.left(90)
    harry.forward(420)
    harry.left(90)

# move into position to draw middle of castle
harry.left(90)
harry.forward(460)
harry.right(90)

# middle of castle
harry.pendown()
harry.fillcolor("gray")
harry.begin_fill()
harry.forward(310)
harry.left(90)
# battlements
harry.forward(34.4444)
harry.left(90)
for e in range(4):
    for m in range(2):
        harry.forward(34.4444)
        harry.right(90)
    for o in range(2):
        harry.forward(34.4444)
        harry.left(90)
# rest of middle of castle
harry.forward(310)
harry.left(90)
harry.forward(120)
harry.left(90)
harry.forward(120)
harry.right(90)
harry.forward(70)
harry.right(90)
harry.forward(120)
harry.left(90)
harry.forward(120)
harry.left(90)
harry.forward(310)
harry.end_fill()
harry.penup()

# move into position for Hogwarts sign
harry.left(135)
harry.forward(219.2031)
harry.right(135)
harry.forward(50)
# Hogwarts sign
harry.color("black")
harry.write("Hogwarts", False, "center", ("Verdana", 25, "normal"))
harry.backward(50)
harry.write("School of Witchcraft & Wizardry", False, "center", ("Arial", 16, "normal"))

# move into position for broomstick
harry.forward(400)
harry.right(90)
harry.forward(100)
# stick part of broomstick
harry.pensize(10)
harry.color("brown")
harry.pendown()
harry.backward(200)
# hairs of broomstick
harry.pensize(2)
harry.color("black")
harry.right(30)
for r in range(12):
    harry.backward(50)
    harry.penup()
    harry.forward(50)
    harry.left(5)
    harry.pendown()
harry.penup()


# Harry's head
harry.forward(125)
harry.pendown()
harry.color("gray")
harry.fillcolor("gray")
harry.begin_fill()
harry.circle(30)
harry.end_fill()
harry.penup()


# Harry's body
harry.backward(10)
harry.color("red")
harry.fillcolor("black")
harry.pendown()
harry.begin_fill()
harry.right(145)
harry.forward(150)
harry.left(110)
harry.forward(100)
harry.left(110)
harry.forward(150)
harry.end_fill()

# Harry's glasses
harry.penup()
harry.forward(40)
harry.left(50)
harry.pendown()
harry.color("black")
harry.circle(10)
harry.penup()
harry.right(30)
harry.backward(25)
harry.right(180)
harry.pendown()
harry.circle(10)
harry.left(135)
harry.penup()
harry.forward(5)
harry.left(90)
harry.forward(4)
harry.pendown()
harry.forward(7)
harry.penup()

# Harry's eyes
harry.forward(5)
harry.pendown()
harry.dot(10,"dark green")
harry.penup()
harry.backward(25)
harry.pendown()
harry.dot(10,"dark green")
harry.penup()

# Harry's scar
harry.right(45)
harry.forward(15)
harry.pendown()
harry.color("yellow")
harry.pensize(4)
harry.forward(10)
harry.right(135)
harry.forward(8)
harry.left(135)
harry.forward(10)
harry.penup()

# Harry's arms
harry.backward(100)
harry.color("red")
harry.fillcolor("red")
harry.begin_fill()
harry.pendown()
harry.left(60)
harry.forward(60)
harry.right(40)
harry.backward(60)
harry.right(90)
harry.forward(30)
harry.end_fill()
harry.right(135)
harry.color("gray")
harry.fillcolor("gray")
harry.begin_fill()
harry.circle(10)
harry.end_fill()
harry.penup()

# golden snitch
harry.left(90)
harry.forward(100)
harry.color("gold")
harry.fillcolor("gold")
harry.begin_fill()
harry.pendown()
harry.circle(7)
harry.end_fill()
harry.penup()
harry.forward(7)
harry.pensize(7)
harry.color("white")
for t in range(2):
    harry.pendown()
    harry.forward(25)
    harry.penup()
    harry.backward(25)
    harry.left(135)
    harry.forward(20)
    harry.right(45)


harry.forward(1000)
wn.mainloop()