from turtle import *
from time import sleep

xiaogui = Turtle()


# 定义一个函数 randGo 随便走times次  把重复的代码放进来
def randGo(times):
    for i in range(times):
        xiaogui.fd(30)
        xiaogui.right(360 / times)
    sleep(2)
    xiaogui.clear()


# 把要走的次数放在一个列表里面
times_list = [3, 4, 6, 16, 36]
for i in times_list:
    randGo(i)
