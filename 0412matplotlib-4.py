# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# figure对象
'''
figure对象是最外层的绘图单位，默认是1开始编号，figure1,figure2
可以使用plt.figure()产生一幅图像，除了默认参数外，可以指定
    num 编号;figsize-图像大小;dpi-分辨率;facecolor-背景色;edgecolor-边界颜色;frameon-边框
'''
# subplot和axes对象 subplot主要是使用网格排列子图
plt.subplot(2,1,1)
plt.xticks([])
plt.yticks([])
plt.text(0.5,0.5,'subplot(2,1,1)',ha='center',va='center',size=24,alpha=0.5)
plt.subplot(2,1,2)
plt.xticks([])
plt.yticks([])
plt.text(0.5,0.5, 'subplot(2,1,2)',ha='center',va='center',size=24,alpha=.5)
plt.show()

# 更加高级的图片布局方式，可以使用gridspec来绘图
import matplotlib.gridspec as gridspec
G = gridspec.GridSpec(3,3)   # 生成3行3列的绘图布局

axes_1 = plt.subplot(G[0,:])    # G[0,:]表示第0行所有列组合成一幅图像
plt.xticks([])
plt.yticks([])
plt.text(0.5,0.5, 'Axes 1',ha='center',va='center',size=24,alpha=.5)

axes_2 = plt.subplot(G[1,:-1])    # G[1,:-1]表示第1行第1,2两列组合成一幅图像
plt.xticks([])
plt.yticks([])
plt.text(0.5,0.5, 'Axes 2',ha='center',va='center',size=24,alpha=.5)

axes_3 = plt.subplot(G[1:,-1])   # 第2,3行第3列组合成一幅图像
plt.xticks([])
plt.yticks([])
plt.text(0.5,0.5, 'Axes 2',ha='center',va='center',size=24,alpha=.5)

aexs_4 = plt.subplot(G[-1,0])
plt.xticks([])
plt.yticks([])
plt.text(0.5,0.5,'Axes 5',ha='center',va='center',size=24,alpha=0.5)

axes_5 = plt.subplot(G[-1,1])
plt.xticks([])
plt.yticks([])
plt.text(0.5,0.5,'Axes 5',ha='center',va='center',size=24,alpha=0.5)
plt.show()

# axes对象subplot返回的是Axes对象，但是Axes对象相对于subplot返回的对象来说更自由一点
# Axes对象可以放置在图像中的任意位置
plt.axes([0.1,0.1,0.8,0.8])
plt.xticks([])   # 设置刻度无
plt.yticks([])
plt.text(0.6,0.6,'axes([0.1,0.1,.8,.8])',ha='center',va='center',size=20,alpha=.5)

plt.axes([0.2,0.2,.3,.3])
plt.xticks([])
plt.yticks([])
plt.text(0.5,0.5, 'axes([0.2,0.2,.3,.3])',ha='center',va='center',size=16,alpha=.5)
plt.show()

# 图形线段模式的设置
x = np.linspace(0, 10, 500)
dashes = [10, 5, 30, 5]  # 10 points on, 5 off, 100 on, 5 off
fig, ax = plt.subplots()
line1, = ax.plot(x, np.sin(x), '--', linewidth=2,label='Dashes set retroactively')
# 这里的set_dashes是设置线段的显示形式，[10,5,30,5]表示，前10个点显示，接着5点个点不显示，接着30个点显示，接着5个点不显示
line1.set_dashes(dashes)

line2, = ax.plot(x, -1 * np.sin(x), dashes=[30, 5, 10, 5],label='Dashes set proactively')
ax.legend(loc='lower right')

plt.show()
'''
对于subplots()函数，返回的是图像figure和Axes
subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
    nrows ncols表示的图像布局的几行几列
    sharex sharey表示的是子图是否共享x y轴，还可以设施all row col
        其中，'row'表示行的子图共享x轴或者y轴
        'col'表示列的子图共享x轴或者y轴
    subplot_kw设置add_subplot()参数
    gridspec_kw设置网格的参数
    fig_kw表示设置的figure参数 matplotlib.axes.Axes
f,(ax1,ax2) = plt.subplots(1,2,sharey=True)
fig,axes = plt.subplots(2,2,subplot_kw=dict(polar=True)
axes[0,0].plot(x,y)
axes[1,1].scatter(x,y)
plt.subplots(2, 2, sharex='col')
plt.subplots(2,2,sharex=True,sharey=True)
'''

# 绘图颜色的填充
x = np.linspace(0, 2 * np.pi, 500)
y1 = np.sin(x)
y2 = np.sin(3 * x)
fig,ax = plt.subplots()
ax.fill(x,y1,'b',x,y2,'r',alpha=0.3)
plt.show()

# 更改图像设置
x = np.linspace(-np.pi, np.pi)
c, s = np.cos(x), np.sin(x)
# 我们使用figure函数来创建一幅新图像，并制定他的大小，使得长宽比更合适
f = plt.figure(figsize=(10,6),dpi=80,facecolor='white')
# 使用color linewidth linestyle参数，指定曲线的颜色，粗细，类型
p = plt.plot(x,c,color='blue',lw=2.5,ls='-')
p = plt.plot(x,s,color='red',lw=2.5,ls='-')

# 设置横纵坐标轴的显示范围
p = plt.xlim(x.min() * 1.1,x.max() * 1.1)
p = plt.ylim(c.min() * 1.1,c.max() * 1.1)

# 设置刻度
p = plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
               ['$-\pi$', '$-\pi/2$', '$0$', '$\pi/2$', '$\pi$'], fontsize='xx-large')
plt.yticks([-1,0,1],
           ['$-1$', '$0$', '$+1$'], fontsize='xx-large')

# 改变坐标轴
ax = plt.gca()   # 得到轴的句柄
# ax.spines参数表示四个坐标轴线
# 将右边和上边的颜色设置为透明
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 将x轴的刻度设置在下面的坐标轴上
ax.xaxis.set_ticks_position('bottom')
# 将y轴的刻度设置在坐标的坐标轴上
ax.yaxis.set_ticks_position('left')
# 设置位置
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))

# 加入图例
plt.legend(['cosine','sine'],loc='upper left',frameon=False)

################# 注释特殊点
t = 2 * np.pi / 3
# 给出两点的坐标x y
plt.plot(x = [t,t],y = [0,np.cos(t)],color='blue',lw=2.5,ls='--')
plt.scatter([t,],[np.cos(t),], 50, color ='blue')
# 在对应的点显示文本
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$', # 文本
             xy=(t, np.sin(t)), # 数据点坐标位置
             xycoords='data',   # 坐标相对于数据
             xytext=(+10, +30), # 文本位置坐标
             textcoords='offset points', # 坐标相对于数据点的坐标
             fontsize=16,       # 文本大小
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")) # 箭头

# 红色虚线
p = plt.plot([t,t],[0,np.sin(t)],color='red',lw=2.5,ls='--')
# 该点处的 sin 值
p = plt.scatter([t,],[np.sin(t),], 50, color ='red')
p = plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
                 xy=(t,np.cos(t)),xycoords='data',
                 xytext=(-90,-50),textcoords='offset points',fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# 让刻度显示在图线的上方
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.65))

# 设置网格线
plt.grid(True)

plt.show()
