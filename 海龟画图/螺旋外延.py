# 螺旋彩图
from turtle import *
import time
import os

# def huaZhengFangXing(gui,bianChang):
#     gui.pendown()
#     gui.begin_fill()
#     for i in range(4):
#         gui.fd(bianChang)
#         gui.right(90)
#     gui.end_fill()
#     gui.penup()
#
# yanSeBiao = ["red","yellow","orange","blue","green"]
# t = Turtle()
# t.speed(0)
# screen = t.getscreen()
# screen.bgcolor("black")
#
# xuHao = 0
# jiaodu = 5
# for i in range(150):
#     jiaodu -=1
#     t.pencolor(yanSeBiao[xuHao])
#     t.fillcolor(yanSeBiao[xuHao])
#     huaZhengFangXing(t,10)
#     t.fd(20)
#     t.right(jiaodu)
#     #数组越界
#     xuHao = xuHao + 1
#     if xuHao == 5:
#         xuHao = 0
t = Turtle()

# 图案1
# for i in range(1, 110, 2):
#     t.circle(i, i)
#     t.goto(0, 0)
# 图案2 蚊香形状
# for i in range(1, 110, 2):
#     t.circle(i, i)

# 图案3
# for i in range(1, 110, 2):
#     t.circle(i, i)
#     t.up()
#     t.goto(0, 0)
#     t.down()

# 图案4
# for i in range(1, 110, 2):
#     t.circle(i, 110-i)
#     t.up()
#     t.goto(0, 0)
#     t.down()

# 同心圆
for i in range(10,110,10):
    t.circle(i)
    t.up()
    t.goto(0,-i)
    t.down()