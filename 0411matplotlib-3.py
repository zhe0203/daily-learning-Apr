# -*- coding: utf-8 -*-
# http://nbviewer.jupyter.org/github/lijin-THU/notes-python/blob/master/06-matplotlib/06.03-working-with-text---basic.ipynb
# 处理文本
import matplotlib.pyplot as plt
import numpy as np
'''
matplotlib对文本的支持十分完善，包括数学公式，unicode文字，栅格和向量输出，文字转换行，文字旋转等一些列操作
'''

# 基础文本函数
'''
text()在Axes对象的任意位置添加文本
xlabel()添加x轴标题
ylabel()添加y轴标题
title()给Axes对象添加标题，对于figure中绘制的图像进行添加标题
figtext()在Figure对象的任意位置添加文本
suptitle()给Figure对象添加标题 是对于整幅图像的添加
anotate()给Axes对象添加注释(可选择是否添加箭头标记)
'''

# plt.figure()返回一个Figure对象
fig = plt.figure(figsize=(12,9),facecolor='white')
# 设置这个Figure对象的标题
# 事实上，如果我们直接调用plt.figure()函数，他会自动找到当前的Figure对象
fig.suptitle('bold figure suptitle',fontsize=14,fontweight='bold')
# Axes对象表示Figure对象中的子图
ax = fig.add_subplot(111)
# subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=None, hspace=None)
fig.subplots_adjust(top=0.9)     # 调整图片的位置

# 可以直接使用set_xxx的方法来设置标题
ax.set_title('axes title')
# 也可以直接调用title()因为会自动定位到当前的Axes对象
# plt.title('axes title')

ax.set_xlabel('xlabel')
# 也可直接调用plt.xlabel()函数，会自动定位到当前的Axes对象
ax.set_ylabel('ylabel')

# 添加文本，斜体加文本框
ax.text(3,8,'boxed italics text in data coords',style='italic',
        bbox={'facecolor':'red','alpha':0.5,'pad':10})
# 数学公式，用$$输入Tex公式
ax.text(2,6,r'an equation:$E=mc^2$',fontsize=15)

# Unicode支持
# ax.text(3,2,unicode('unicode: Institut f\374r Festk\366rperphysik', 'latin-1'))

# 颜色，对其方式 文本属性的设置可以通过plt.text.Text()中的对应函数来进行设置
ax.text(0.95,0.01,'colored text in axes corrds',verticalalignment='bottom',
        horizontalalignment='right',transform=ax.transAxes,color='green',fontsize=15)

# 注释文本和箭头
ax.plot([2],[1],'o')
ax.annotate('annotate',xy=(2,1),xytext=(3,4),arrowprops=dict(facecolor='black',shrink=0.05))

# 设置显示范围
ax.axis([0,10,0,10])
plt.show()

import matplotlib.patches as patches
# 建立一个方形的坐标系
left,width = 0.25,0.5
bottom,height = 0.25,0.5
right = left + width
top = bottom + height
fig = plt.figure(figsize=(10,7))
# axes coordinates are 0,0 is bottom left and 1,1 is upper right
ax = fig.add_axes([0,0,1,1])
p = patches.Rectangle(
    (left,bottom),width,height,
    fill=False,transform=ax.transAxes,clip_on=False
)
ax.add_patch(p)
ax.text(left,bottom,'left top',horizontalalignment='left',
        verticalalignment='top',transform=ax.transAxes,
        size='xx-large')
ax.text(left, bottom, 'left bottom',
        horizontalalignment='left',
        verticalalignment='bottom',
        transform=ax.transAxes,
        size='xx-large')

ax.text(right, top, 'right bottom',
        horizontalalignment='right',
        verticalalignment='bottom',
        transform=ax.transAxes,
        size='xx-large')

ax.text(right, top, 'right top',
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes,
        size='xx-large')

ax.text(right, bottom, 'center top',
        horizontalalignment='center',
        verticalalignment='top',
        transform=ax.transAxes,
        size='xx-large')

ax.text(left, 0.5*(bottom+top), 'right center',
        horizontalalignment='right',
        verticalalignment='center',
        rotation='vertical',
        transform=ax.transAxes,
        size='xx-large')

ax.text(left, 0.5*(bottom+top), 'left center',
        horizontalalignment='left',
        verticalalignment='center',
        rotation='vertical',
        transform=ax.transAxes,
        size='xx-large')

ax.text(0.5*(left+right), 0.5*(bottom+top), 'middle',
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=20, color='red',
        transform=ax.transAxes)

ax.text(right, 0.5*(bottom+top), 'centered',
        horizontalalignment='center',
        verticalalignment='center',
        rotation='vertical',
        transform=ax.transAxes,
        size='xx-large')

ax.text(left, top, 'rotated\nwith newlines',
        horizontalalignment='center',
        verticalalignment='center',
        rotation=45,
        transform=ax.transAxes,
        size='xx-large')

ax.set_axis_off()
plt.show()

# 注释文本
'''
text()函数在Axes对象的指定位置添加文本，而annotate()则是对某一点添加注释文本，需要
考虑两个位置：一是注释点的坐标xy,二是注释文本的位置坐标xytext
'''
fig = plt.figure()
ax = fig.add_subplot(111)
t = np.arange(0,5,0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t,s,lw=2)
ax.annotate('local max',xy=(2,1),xytext=(3,1.5),
            arrowprops=dict(facecolor='black',shrink=0.05))
ax.set_ylim(-2,2)
plt.show()

# 使用不同的坐标系
fig = plt.figure()
ax = fig.add_subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)

ax.annotate('local max', xy=(3, 1),  xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )

ax.set_ylim(-2,2)
plt.show()

# 极坐标系注释文本
# 产生极坐标系需要在subplot的参数中设置polar=True
fig = plt.figure()
ax = fig.add_subplot(111,polar=True)
r = np.arange(0,1,0.001)
theta = 2*2*np.pi*r
line, = ax.plot(theta,r,color='#ee8d18',lw=3)

ind = 800
thisr,thistheta = r[ind],theta[ind]
ax.plot([thistheta],[thisr],'o')
ax.annotate('a polar annotation',
            xy=(thistheta, thisr),  # theta, radius
            xytext=(0.05, 0.05),    # fraction, fraction
            textcoords='figure fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom',
            )
plt.show()

# 处理文本(数学表达式) Tex语法
plt.title(r'$\alpha_i > \beta^j$')
plt.show()
# 使用_和^表示上下标记
# r'$\sum_{i=0}^\infty x_i$'
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t,s)
ax.set_title(r'$\alpha_i > \beta_i$', fontsize=20)
ax.text(1,-0.6,r'$sum_{i=0}^\infty x_i$',fontsize=20)
ax.text(0.6,0.6,r'$\mathal{A}\ \mathrm{sin}(2 \omega t)$')
ax.set_ylabel('volts (mV)')
ax.set_xlabel('time (s)')
plt.show()
