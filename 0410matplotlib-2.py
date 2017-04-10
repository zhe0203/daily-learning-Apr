# -*- coding: utf-8 -*-
# http://nbviewer.jupyter.org/github/lijin-THU/notes-python/blob/master/06-matplotlib/06.02-customizing-plots-with-style-sheets.ipynb
# 使用style来配置pyplot风格
import matplotlib.pyplot as plt
import numpy as np
'''
style是pyplot的一个子模块，方便进行风格转换，pyplot有很多的预设风格
可以使用plt.style.available来查看
'''
print(plt.style.available)
# ['ggplot', 'seaborn-notebook', 'seaborn-poster', 'seaborn-dark-palette', 'seaborn-colorblind',
# 'grayscale', 'bmh', 'seaborn-white', 'dark_background', 'seaborn-paper', 'seaborn-ticks', 'seaborn-talk',
# 'classic', 'seaborn-dark', 'seaborn-whitegrid', 'fivethirtyeight', 'seaborn-darkgrid', 'seaborn-bright',
# 'seaborn-pastel', 'seaborn-deep', 'seaborn-muted']

x = np.linspace(0,2*np.pi)
y = np.sin(x)
plt.plot(x,y)
plt.show()

# 可以模仿R语言中常用的ggplot风格
plt.style.use('seaborn-paper')
plt.plot(x,y)
plt.show()

# 有时候我们不希望改变全局的风格，只是想暂时改变下风格，则可以使用context将风格改变现在在某一个代码块内
with plt.style.context(('dark_background')):
    plt.plot(x,y,'r-o')
    plt.show()

# 在代码块外挥着则仍然是全局风格
with plt.style.context(('dark_background')):
    pass
plt.plot(x,y,'r-o')
plt.show()

# 还可以混搭使用多种风格，补货最右边的一种风格将会最坐标的覆盖
plt.style.use(['dark_background','ggplot'])
plt.plot(x,y,'r-o')
plt.show()

# 还可以自定义风格
'''
自定义文件需要放在matplotlib的配置文件夹mpl_configdir的子文件夹mpl_configdir/stylelib下，以.mplstyle结尾
'''
import matplotlib
print(matplotlib.get_configdir())
'''
里面的内容以 属性：值 的形式保存：
axes.titlesize : 24
axes.labelsize : 20
lines.linewidth : 3
lines.markersize : 10
xtick.labelsize : 16
ytick.labelsize : 16
假设我们将其保存为 mpl_configdir/stylelib/presentation.mplstyle，那么使用这个风格的时候只需要调用：
plt.style.use('presentation')
'''
