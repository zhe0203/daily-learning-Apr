# -*- coding: utf-8 -*-
# pyplot教程
# http://nbviewer.jupyter.org/github/lijin-THU/notes-python/blob/master/06-matplotlib/06.01-pyplot-tutorial.ipynb
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 对于中文，需在代码前加上以下两行代码，防止乱码的出现
matplotlib.rcParams['font.sans-serif'] = [u'SimHei']  # FangSong/黑体 FangSong/KaiTi
matplotlib.rcParams['axes.unicode_minus'] = False

'''
pyplot包含了一系列类似matlab中绘图函数的相关函数
每个pyplot中的函数对当前的图像进行一些修改，产生新的图像，在图像中产生新的绘图区域，
在绘图区域中画线，给绘图加上标记等等
'''

# plt.show()函数
'''
默认情况下，matplotlib.pyplot不会直接显示图像，只有调用plt.show()函数时，
图像才会显示出来
plt.show()默认是在新窗口打开一幅图像，并且提供了对图像进行操作的按钮
这里我们使图像输出在 notebook 中：%matplotlib inline
对于y轴，x轴标签，刻度进行文字设置的属性，参照plt.text.Text中的参数，进行添加设置
http://matplotlib.org/api/text_api.html#matplotlib.text.Text
'''

# plt.plot()函数
plt.figure(1,facecolor='white',edgecolor='red',figsize=(100,200))
plt.plot([1,2,3,4])
plt.ylabel('y轴',fontsize=22)
plt.xlabel('x轴',fontsize=18,color='red')
# plt.show()

# 基本用法
'''
默认参数: plt.plot(x,y)
指定参数: plt.plot(x,y,format_str)
默认参数，x为0~N-1 plt.plot(y)
指定参数，x 为 0~N-1 plt.plot(y,format_str)
plt.yscale()标准化y轴的方式
'''
plt.figure(2,facecolor='white')
plt.plot([1,2,3,4],[1,4,9,16])
# 设置x中标签的名称，需要根据x轴坐标的值进行设置
plt.xticks(np.arange(1,5),('tom','lab','kitt','jeo'),fontsize=18)
plt.yticks(fontsize=18)
# plt.axis('off')                 # 关闭x,y轴的坐标轴及标签信息
plt.show()

# 字符参数
'''
表示颜色的字符参数:
b 蓝色blue;g绿色green;r红色red;c青色cyan;m品红magenta;y黄色yelloe;k黑色black;w白色white
表示类型的字符串参数
-实线;--虚线;-.虚点线;:点线;.点;,像素点;o圆点;v下三角点
^上三角点;<左三角点;>右三角点;1下三叉点;2上三叉点;3左三叉点
4右三叉点；s正方点;p五角点;*星形点;h六边形点1;H六边形点2
+加号点;x乘号点;D实心菱形点;d瘦菱形点;_横线点
'''
plt.plot([1,2,3,4],[1,4,9,16],'ro')
# plt.show()

# 改变轴的显示范围
# 这里可以使用axis函数指定坐标轴显示的范围
# plt.axis([xmin,xmax,ymin,ymax])
plt.plot([1,2,3,4],[1,4,9,16],'r-.')
plt.axis([0,6,0,20])     # xlim ylim
# plt.show()

# 传入numpy数组
t = np.arange(0,5,0.2)
line1,line2,line3 = plt.plot(t,t,'r--',
                             t,t**2,'bs',
                             t,t**3,'g^')
plt.setp(line1,'color','r','linewidth',1)
# plt.show()

# 线条属性 linewidth改变线条的宽度 color改变线条的颜色
x = np.linspace(-np.pi,np.pi)
y = np.sin(x)
plt.plot(x,y,linewidth=2,color='r')
# plt.show()

# 使用plt.plot()函数返回值来设置线条属性
'''
plot函数返回一个Line2D对象组成的列表，每个对象代表输入的一对组合，例如
line1,line2为两个Line2D对象
    line1,line2 = plt.plot(x1,y1,x2,y2)
返回3个Line2D对象组成的列表
    lines = plt.plot(x1,y1,x2,y2,x3,y3)
我们可以使用这个返回值来对线条的属性进行设置

'''
# 加逗号line中得到的是line2d对象，不加逗号得到的是只有一个line2d对象的列表
line, = plt.plot(x,y,'r-')
# 将糠锯齿关闭
line.set_antialiased(False)
# plt.show()

# 使用plt.setp()修改线条性质
lines = plt.plot(x,y)
# 使用键值对
plt.setp(lines,color='r',linewidth=2.0)
# 或者使用 MATLAB 风格的字符串对
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
# plt.show()

# 可以设置的属性有很多，可以使用 plt.setp(lines) 查看 lines 可以设置的属性，各属性的含义可

# 子图
'''
figure()函数会产生一个指定编号的num图
plt.figure(num)
这里figure(1)其实可以省略，因为默认情况下plt会自动产生一幅图像
使用subplot可以在一幅图中生成多个子图，其参数为:
    plt.subplot(numrows,numcols,fignum)
当numrows*numcols<10时，中间的逗号可以省略，因此plt.subplot(211)相当于plt.subplot(2,1,1)
使用plt.figure()函数一次性展示设置的图片数
'''
# figure函数的属性
'''
figsize：图片的大小属性(width,height)
dpi : 整数，图片像素的大小
facecolor:图片的背景色
edgecolor:边框颜色
'''
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0,5,0.1)
t2 = np.arange(0,5,0.02)

plt.figure(1)     # 可有可无
plt.subplot(211)
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
# plt.show()

# 图形上加上文字 plt.hist()绘制直方图
mu,sigma = 100,15
x = mu + sigma * np.random.randn(10000)
n,bins,patches = plt.hist(x,50,normed=1,facecolor='g',alpha=0.75)
plt.xlabel('Smarts')      # x轴标注
plt.ylabel('Probability')   # y轴标注
plt.title('IQ直方图')        # 图形标题
#  输入特殊符号支持使用 Tex 语法，用 $<some Tex code>$ 隔开。
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')    # 在指定位置放入文字
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
# plt.show()

# 除了使用text在指定位置表上文字之外，还可以使用annotate函数进行注释
# annotate有两个参数，xy注释位置，xytext注释文字的位置

ax = plt.subplot(111)
t = np.arange(0,5,0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t,s,lw=2)
plt.annotate('local max',xy=(2,1),xytext=(3,1.5),
             arrowprops=dict(facecolor='black',shrink=0.05))
plt.ylim(-2,2)
# plt.show()
