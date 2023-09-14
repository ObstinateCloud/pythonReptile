#自定义海龟图形
from turtle import *
from time import sleep
print("海龟本来的图形：",getshapes())






xingZhuang = Turtle()
#开始记录多边形顶点,当前海龟位置是第一个顶点，这个顶点会作为图形的旋转重心
xingZhuang.begin_poly()
for i in range(4):
    xingZhuang.fd(100)
    xingZhuang.right(90)
xingZhuang.end_poly()
#得到刚才所画图形的每个顶点，形成元祖
p = xingZhuang.get_poly()
print(p)
register_shape("不一样的正方形",p)
print("海龟现在的图形:",getshapes())
xingZhuang.clear()
xingZhuang.hideturtle()
del xingZhuang

sleep(5)
t = Turtle(shape = "不一样的正方形")
t.fillcolor('red')
def xuanZhuan():
    t.right(10)
    ontimer(xuanZhuan,10)
xuanZhuan()