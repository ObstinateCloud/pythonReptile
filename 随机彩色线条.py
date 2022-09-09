#屏幕范围内随机移动
from random import randint,choice
from turtle import *
from time import sleep
yanSeBiao = ("red","orange","yellow","green","cyan","blue","purple")
xiaoHong = Turtle()
screen = xiaoHong.getscreen()
w = window_width()
h = window_height()
screen.title("画彩色线条小程序")
screen.bgcolor("black")

for i in range(10):
    xiaoHong.pencolor(choice(yanSeBiao))
    x = randint(-w/2,w/2)
    y = randint(-h/2,h/2)
    # xiaoHong.up()
    xiaoHong.goto(x,y)
    # xiaoHong.down()
    # xiaoHong.dot(10)
    sleep(0.1)