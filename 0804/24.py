#coding=utf-8
'''
time:2020/9/23 15:57
'''
# import turtle
# from datetime import *
#
#
# # 抬起画笔，向前运动一段距离放下
# def Skip(step):
#     turtle.penup()
#     turtle.forward(step)
#     turtle.pendown()
#
#
# def mkHand(name, length):
#     # 注册Turtle形状，建立表针Turtle
#     turtle.reset()
#     Skip(-length * 0.1)
#     # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
#     turtle.begin_poly()
#     turtle.forward(length * 1.1)
#     # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
#     turtle.end_poly()
#     # 返回最后记录的多边形。
#     handForm = turtle.get_poly()
#     turtle.register_shape(name, handForm)
#
#
# def Init():
#     global secHand, minHand, hurHand, printer
#     # 重置Turtle指向北
#     turtle.mode("logo")
#     # 建立三个表针Turtle并初始化
#     mkHand("secHand", 135)
#     mkHand("minHand", 125)
#     mkHand("hurHand", 90)
#     secHand = turtle.Turtle()
#     secHand.shape("secHand")
#     minHand = turtle.Turtle()
#     minHand.shape("minHand")
#     hurHand = turtle.Turtle()
#     hurHand.shape("hurHand")
#
#     for hand in secHand, minHand, hurHand:
#         hand.shapesize(1, 1, 3)
#         hand.speed(0)
#
#         # 建立输出文字Turtle
#     printer = turtle.Turtle()
#     # 隐藏画笔的turtle形状
#     printer.hideturtle()
#     printer.penup()
#
#
# def SetupClock(radius):
#     # 建立表的外框
#     turtle.reset()
#     turtle.pensize(7)
#     for i in range(60):
#         Skip(radius)
#         if i % 5 == 0:
#             turtle.forward(20)
#             Skip(-radius - 20)
#
#             Skip(radius + 20)
#             if i == 0:
#                 turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
#             elif i == 30:
#                 Skip(25)
#                 turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
#                 Skip(-25)
#             elif (i == 25 or i == 35):
#                 Skip(20)
#                 turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
#                 Skip(-20)
#             else:
#                 turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
#             Skip(-radius - 20)
#         else:
#             turtle.dot(5)
#             Skip(-radius)
#         turtle.right(6)
#
#
# def Week(t):
#     week = ["星期一", "星期二", "星期三",
#             "星期四", "星期五", "星期六", "星期日"]
#     return week[t.weekday()]
#
#
# def Date(t):
#     y = t.year
#     m = t.month
#     d = t.day
#     return "%s %d%d" % (y, m, d)
#
#
# def Tick():
#     # 绘制表针的动态显示
#     t = datetime.today()
#     second = t.second + t.microsecond * 0.000001
#     minute = t.minute + second / 60.0
#     hour = t.hour + minute / 60.0
#     secHand.setheading(6 * second)
#     minHand.setheading(6 * minute)
#     hurHand.setheading(30 * hour)
#
#     turtle.tracer(False)
#     printer.forward(65)
#     printer.write(Week(t), align="center",
#                   font=("Courier", 14, "bold"))
#     printer.back(130)
#     printer.write(Date(t), align="center",
#                   font=("Courier", 14, "bold"))
#     printer.home()
#     turtle.tracer(True)
#
#     # 100ms后继续调用tick
#     turtle.ontimer(Tick, 100)
#
#
# def main():
#     # 打开/关闭龟动画，并为更新图纸设置延迟。
#     turtle.tracer(False)
#     Init()
#     SetupClock(160)
#     turtle.tracer(True)
#     Tick()
#     turtle.mainloop()
#
#
# if __name__ == "__main__":
#     main()







from turtle import *
from time import sleep


def go_to(x, y):
    up()
    goto(x, y)
    down()


def big_Circle(size):  # 函数用于绘制心的大圆
    speed(5)
    for i in range(150):
        forward(size)
        right(0.3)


def small_Circle(size):  # 函数用于绘制心的小圆
    speed(10)
    for i in range(210):
        forward(size)
        right(0.786)


def line(size):
    speed(5)
    forward(51 * size)


def heart(x, y, size):
    go_to(x, y)
    left(150)
    begin_fill()
    line(size)
    big_Circle(size)
    small_Circle(size)
    left(120)
    small_Circle(size)
    big_Circle(size)
    line(size)
    end_fill()


def arrow():
    pensize(10)
    setheading(0)
    go_to(-400, 0)
    left(15)
    forward(150)
    go_to(339, 178)
    forward(150)


def arrowHead():
    pensize(1)
    speed(5)
    color('red', 'red')
    begin_fill()
    left(120)
    forward(20)
    right(150)
    forward(35)
    right(120)
    forward(35)
    right(150)
    forward(20)
    end_fill()


def main():
    pensize(4)
    color('red', 'pink')
    # getscreen().tracer(30, 0) #取消注释后，快速显示图案
    heart(200, 0, 1)  # 画出第一颗心，前面两个参数控制心的位置，函数最后一个参数可控制心的大小
    setheading(0)  # 使画笔的方向朝向x轴正方向
    heart(-80, -100, 1.5)  # 画出第二颗心
    arrow()  # 画出穿过两颗心的直线
    arrowHead()  # 画出箭的箭头
    go_to(400, -300)
    done()


main()
