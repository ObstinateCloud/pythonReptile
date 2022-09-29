from turtle import *
from time import sleep
from random import randint

xiaoShe = Turtle()
xiaoShe.shape("turtle")
xiaoShe.speed(0)
xiaoShe.penup()
screen = xiaoShe.getscreen()
screen.title("贪吃蛇-控制")

for i in range(10):
    xiaoShe.stamp()


def yiDongXiaoShe():
    xiaoShe.clearstamps(1)
    xiaoShe.stamp()
    xiaoShe.fd(20)
    screen.ontimer(yiDongXiaoShe, 10)


yiDongXiaoShe()

kuanDu = 800
gaoDu = 600
# 设置窗口宽高
screen.setup(kuanDu, gaoDu)
screen.bgcolor("cyan")

# 增加边框
bianKuang = Turtle(visible=False)
bianKuang.pensize(30)
bianKuang.pencolor("red")
bianKuang.setheading(0)
bianKuang.speed(0)
bianKuang.penup()
bianKuang.goto(-kuanDu / 2, gaoDu / 2)
bianKuang.pendown()
for i in range(2):
    bianKuang.fd(kuanDu)
    bianKuang.right(90)
    bianKuang.fd(gaoDu)
    bianKuang.right(90)

# 创建食物
shiWu = Turtle(visible=False)
shiWu.penup()
shiWu.speed(0)
shiWu.goto(randint(50 - kuanDu / 2, kuanDu / 2 - 50), randint(50 - gaoDu / 2, gaoDu / 2 - 50))
shiWu.fillcolor("green")
shiWu.shape("circle")
shiWu.showturtle()


# 碰撞检测

def dengDaiXiaoShe():
    if shiWu.distance(xiaoShe.pos()) < 15:
        xiaoShe.stamp()
        shiWu.hideturtle()
        shiWu.goto(randint(50 - kuanDu / 2, kuanDu / 2 - 50), randint(50 - gaoDu / 2, gaoDu / 2 - 50))
        shiWu.showturtle()
    screen.ontimer(dengDaiXiaoShe, 1)


# 增加开始游戏代码
youXiKaiShiBiaoZhi = False
# register注册
screen.register_shape("开始游戏0.gif")
screen.register_shape("开始游戏1.gif")
screen.register_shape("开始游戏2.gif")

# 写字
kaiShiYouXi = Turtle(visible=False)
kaiShiYouXi.pencolor("gray")
kaiShiYouXi.speed(0)
kaiShiYouXi.penup()
kaiShiYouXi.sety(100)
kaiShiYouXi.write("贪吃蛇", align="center", font=("黑体", 30, "normal"))
kaiShiYouXi.sety(0)
kaiShiYouXi.showturtle()

# 变色轮滑器
bianSeLunHuanQi = 1


def kaiShiAnNiuBianSe():
    global youXiKaiShiBiaoZhi
    global bianSeLunHuanQi
    bianSeLunHuanQi = 1 - bianSeLunHuanQi
    kaiShiYouXi.shape("开始游戏" + str(bianSeLunHuanQi) + ".gif")
    # 代表游戏未开始
    if youXiKaiShiBiaoZhi == False:
        screen.ontimer(kaiShiAnNiuBianSe, 100)


kaiShiAnNiuBianSe()

dengDaiXiaoShe()
yiDongXiaoShe()


def xiangShang():
    xiaoShe.setheading(90)


def xiangXia():
    xiaoShe.setheading(-90)


def xiangYou():
    xiaoShe.setheading(0)


def xiangZuo():
    xiaoShe.setheading(180)


screen.onkey(xiangShang, "Up")
screen.onkey(xiangXia, "Down")
screen.onkey(xiangYou, "Right")
screen.onkey(xiangZuo, "Left")
listen()