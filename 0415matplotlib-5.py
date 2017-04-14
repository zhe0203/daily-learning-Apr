# -*- coding: utf-8 -*-
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 配置文件的使用
# 通过下面的语句可以获取用户配置路径
matplotlib.get_configdir()
# 通过下面的语句可以获取目前使用的配置文件的路径
matplotlib.matplotlib_fname()
# 配置文件的读入可以使用rc_params函数，它返回一个字典
matplotlib.rc_params()
# 在matplotlib模块载入的时候会调用rc_params，并把得到的配置字典保存到rcParams变量中
print(matplotlib.rcParams)
# matplotlib将使用rcParams中的配置进行绘图，可以进行修改，如
matplotlib.rcParams['line.marker'] = 'o'
# 为了方便配置，可以使用rc函数，下面的例子同时配置点标识符，线宽和颜色
matplotlib.rc('lines',marker='x',linewidth=2,color='red')
# 如果希望恢复到缺省的配置的话，可以使用rcdefaults函数
matplotlib.rcdefaults()
# 如果手工修改了配置文件，希望重新从配置文件载入最新的配置的话，可以调用
matplotlib.rcParams.update(matplotlib.rc_params())

'''
下面首先调用pyplot.figure辅助函数创建Figure对象，
然后调用Figure对象的add_axes方法在其中创建一个Axes对象，
add_axes的参数是一个形如[left, bottom, width, height]的列表，
这些数值分别指定所创建的Axes对象相对于fig的位置和大小，
取值范围都在0到1之间：
'''
fig = plt.figure()
ax = fig.add_axes([0.15,0.1,0.7,0.3])

# 绘制轨迹图形
fig, ax = plt.subplots()
fig.set_facecolor('white')

path = mpath.Path
path_data = [
    (path.MOVETO,(1.58,-2.57)),
    (path.CURVE4,(0.35,-1.1)),
    (path.CURVE4, (-1.75, 2.0)),
    (path.CURVE4, (0.375, 2.0)),
    (path.LINETO, (0.85, 1.15)),
    (path.CURVE4, (2.2, 3.2)),
    (path.CURVE4, (3, 0.05)),
    (path.CURVE4, (2.0, -0.5)),
    (path.CLOSEPOLY, (1.58, -2.57)),
]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)

# plot control points and connecting lines
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')

ax.grid(False)
ax.axis('equal')    # 设置x,y轴的坐标系的值相等
ax.set_axis_off()    # 关闭坐标轴的显示

plt.show()

# fill_between的使用
a = np.random.randn(100).cumsum() + 50
b = np.random.randn(100).cumsum() + 50
c = range(100)
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(c,a)
ax1.plot(c,b)
ax1.fill_between(c,a,b,where=(a<b),facecolor='y',edgecolor='k',alpha=0.5)
ax1.fill_between(c,a,b,where=(a>b),facecolor='b',edgecolor='k',alpha=0.5)
ax2.plot(c,a-b)
plt.show()

# 双坐标轴的绘制
fig,ax1 = plt.subplots(figsize=(8,4))
r = np.linspace(0,5,100)
a = 4 * np.pi * r ** 2
v = (4 * np.pi / 3) * r ** 3
ax1.set_title("surface area and volume of a sphere", fontsize=16)
ax1.set_xlabel('radius [m]',fontsize=16)   # 设置x轴的名称
ax1.plot(r,a,lw=2,color='blue')
ax1.set_ylabel(r"surface area ($m^2$)", fontsize=16, color="blue")
# 设置y轴每一个刻度标签的颜色
for label in ax1.get_yticklabels():
    label.set_color('blue')

ax2 = ax1.twinx()   # 设置双坐标轴，利用次坐标轴进行绘图
ax2.plot(r,v,lw=2,color='red')
ax2.set_ylabel(r"volume ($m^3$)", fontsize=16, color="red")
for label in ax2.get_yticklabels():
    label.set_color('red')

fig.tight_layout()

# 画中画需要局部放大的图
fig = plt.figure(figsize=(8,4))
def f(x):
    return 1/(1+x**2)+0.1/(1+((3-x)/0.2)**2)
def plot_and_format_axes(ax,x,f,fontsize):
    ax.plot(x,f(x),lw=2)
    ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(5))
    ax.yaxis.set_major_locator(mpl.ticker.MaxNLocator(4))
    ax.set_xlabel(r"$x$", fontsize=fontsize)
    ax.set_ylabel(r"$f(x)$", fontsize=fontsize)

# 主要的图
ax = fig.add_axes([0.1,0.15,0.8,0.8],axisbg='#f5f5f5')
x = np.linspace(-4,14,1000)
plot_and_format_axes(ax,x,f,18)

# 子图
x0,x1 = 2.5,3.5
ax = fig.add_axes([0.5,0.5,0.38,0.42],axisbg='none')
x = np.linspace(x0,x1,1000)
plot_and_format_axes(ax,x,f,14)
