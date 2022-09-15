import turtle as t
import random as r

yanSeBiao = ('red', 'yellow', 'green', 'orange', 'blue',)
t.pensize(10)

# 方法1 不用循环
# t.begin_fill()
# t.pencolor(yanSeBiao[r.randint(0,4)])
# t.fd(100)
# t.left(120)
# t.pencolor(yanSeBiao[r.randint(0,4)])
# t.fd(100)
# t.left(120)
# t.pencolor(yanSeBiao[r.randint(0,4)])
# t.fd(100)
# t.end_fill()
# t.hideturtle()

# 方法2 使用循环
t.fillcolor(yanSeBiao[r.randint(0, 4)])
t.begin_fill()
for i in range(3):
    t.pencolor(yanSeBiao[r.randint(0, 4)])
    t.fd(100)
    t.left(120)
t.end_fill()
t.hideturtle()
