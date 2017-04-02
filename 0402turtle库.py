# -*- coding: utf-8 -*-
import turtle
# 画图运动控制
# turtle.goto(x,y)  画笔定位到坐标(x,y)
# turtle.forward(distance) 向正方向运动distance距离
# turtle.backward(distance) 向负方向运动distance长的距离
# turtle.right(angle)  向右偏angle度
# turtle.left(angle)  向左偏angle度
# turtlr.home()   回到原点
# turtle.circle(radius,extent=None,steps=None) 圆形radius为半径，extent为圆的角度
# turtle.speed(speed)  画笔的速度

# 空值画笔的速度
# turtle.speed(1)
# 将画笔定位到原点
# turtle.goto(100,100)
# 从原点开始，出一个边长为100的正方形
# for i in range(4):
    # 正向运动100的距离
    # turtle.forward(120)
    # 向右偏90度
    # turtle.right(90)
# 将画笔定位到原点
# turtle.home()
# 画出一个半径为100,占3/4的圆
# turtle.circle(50,270)

# 画笔控制
# turtle.pendown()   落笔，在此状态下会画出运动的轨迹
# turtle.penup()   起笔，在此状态下不会画出运动的轨迹
# turtle.pensize()  画笔粗细
# turtle.pencolor()  画笔颜色
# turtle.fillcolor()   画笔颜色
# turtle.bengin_fill()  开始填充
# turtle.end_fill()  结束填充
# turtle.write(arg,move=False,align='left',font=(“Arial”, 8, “normal”))

## 控制画笔颜色
# turtle.speed(1)
# turtle.pencolor('red')
## 落笔
# turtle.pendown()
## 设置填充颜色
# turtle.fillcolor('blue')
## 开始填充
# turtle.begin_fill()
## 从原点开始，画出一个边长为100的正方形
# for i in range(4):
#     turtle.forward(200)
#     turtle.right(90)
## 结束填充
# turtle.end_fill()
# turtle.penup()  # 起笔
# turtle.goto(100,-100)
# turtle.write('Crossin编程教室',move=False)

turtle.speed(10)
turtle.penup()
turtle.goto(100,300)
turtle.pencolor('#FF6EB4')
turtle.pensize(3)

# 猪鼻子
turtle.fillcolor('#FFE4E1')
turtle.begin_fill()
turtle.pendown()
turtle.right(160)
turtle.circle(30,-60)
turtle.circle(70,extent=-80)
turtle.circle(30,-100)
turtle.circle(50,-40)
turtle.right(-10)
turtle.circle(75,-50)
turtle.circle(20,-50)
turtle.penup()
turtle.end_fill()
# 鼻孔
turtle.goto(100,245)
turtle.dot(15, "#FF3E96")
turtle.goto(130,250)
turtle.dot(15, "#FF3E96")

# 脸部
turtle.goto(100,300)
turtle.pendown()
turtle.right(9)
turtle.circle(800,10)
turtle.circle(500,10)
turtle.circle(300,10)

turtle.left(10)
turtle.circle(200,10)

turtle.right(10)
turtle.circle(100,20)
turtle.circle(50,10)
turtle.circle(200,20)
turtle.circle(160,20)
turtle.circle(120,30)
turtle.circle(60,30)

turtle.circle(250,30)
#
turtle.circle(60,20)

turtle.circle(100,20)
turtle.circle(100,20)
turtle.circle(100,20)
turtle.circle(100,20)

turtle.right(105)
turtle.circle(500,15)
turtle.penup()

# 眼睛
turtle.goto(-90,210)
turtle.pendown()
turtle.circle(18,360)
turtle.penup()


turtle.goto(-103,226)
turtle.pendown()
turtle.dot(15, "#1F1F1F")
turtle.penup()

turtle.goto(0,230)
turtle.pendown()
turtle.circle(18,360)
turtle.penup()
turtle.goto(-15,245)
turtle.pendown()
turtle.dot(15, "#1F1F1F")
turtle.penup()

# 嘴巴
turtle.goto(-120,80)
turtle.pendown()
turtle.right(100)
turtle.circle(50,80)
turtle.circle(50,80)
turtle.penup()

# 脸腮
turtle.fillcolor('#FFE4E1')
turtle.pensize(0)
turtle.pencolor('#fff')
turtle.begin_fill()
turtle.goto(-140,130)
turtle.pendown()
turtle.circle(30,360)
turtle.penup()
turtle.end_fill()

# 耳朵
turtle.pensize(3)
turtle.pencolor('#FF6EB4')
turtle.fillcolor('#FFE4E1')
turtle.begin_fill()
turtle.goto(-130,260)
turtle.pendown()
turtle.right(-15)
turtle.circle(200,12)
turtle.circle(20,180)
turtle.circle(200,12)
turtle.left(73)
turtle.circle(200,9)
turtle.penup()
turtle.end_fill()

turtle.fillcolor('#FFE4E1')
turtle.begin_fill()
turtle.goto(-60,280)
turtle.pendown()
turtle.left(70)
turtle.circle(200,12)
turtle.circle(20,180)
turtle.circle(200,10.5)
turtle.left(74)
turtle.circle(200,9)
turtle.penup()
turtle.end_fill()

# 身体
turtle.goto(-190,10)
turtle.pendown()
turtle.left(200)
turtle.circle(200,30)
turtle.circle(500,15)
turtle.left(89)
turtle.forward(320)
turtle.left(89)
turtle.circle(500,15)
turtle.circle(200,32)

turtle.penup()

# 腿
turtle.goto(-170,-210)
turtle.pendown()
turtle.right(225)
turtle.forward(80)
turtle.pencolor('#1F1F1F')
turtle.pensize(8)
turtle.left(90)
turtle.forward(40)
turtle.penup()

turtle.goto(-40,-210)
turtle.pendown()
turtle.pencolor('#FF6EB4')
turtle.pensize(3)
turtle.right(90)
turtle.forward(80)
turtle.pencolor('#1F1F1F')
turtle.pensize(8)
turtle.left(90)
turtle.forward(40)
turtle.penup()

# 手掌
turtle.pencolor('#FF6EB4')
turtle.pensize(3)
turtle.goto(-220,-30)
turtle.pendown()
turtle.left(210)
turtle.forward(130)
turtle.penup()

turtle.goto(-300,-80)
turtle.pendown()
turtle.left(30)
turtle.forward(35)
turtle.penup()

turtle.goto(-300,-80)
turtle.pendown()
turtle.right(60)
turtle.forward(35)
turtle.penup()

# 另一只手
turtle.goto(35,-30)
turtle.pendown()
turtle.right(210)
turtle.forward(125)
turtle.penup()

turtle.goto(100,-65)
turtle.pendown()
turtle.left(30)
turtle.forward(40)
turtle.penup()
turtle.goto(100,-65)
turtle.pendown()
turtle.right(65)
turtle.forward(40)
turtle.penup()

# 尾巴
turtle.goto(-250,-160)
turtle.pendown()
turtle.left(70)
turtle.circle(100,-10)
turtle.circle(20,-90)
# turtle.right(60)
turtle.circle(10,-120)
turtle.circle(20,-120)
turtle.circle(20,-60)
turtle.circle(100,-10)
turtle.penup()
turtle.done()
