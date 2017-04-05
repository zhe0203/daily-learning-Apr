print(r'\\\n\\')     ## 在字符串前面加上r可以使得转义字

(20,)*3              # 元组(20, 20, 20)

y.ravel()        // 将行变成列

import operator
data = {'a':1.5,'b':1,'c':2}
data.items()    # 将字典返回元组的形式[('a',1.5),('b',1),('c',2)]
#  还可设置成key=operator.itemgetter(1,2)  说明按照第二个第三个元素进行排序
sorted(data.items(),key=operator.itemgetter(1),reverse=True)    # 设置operator.itemgetter(1)说明按照第二个元素进行排序

import numpy as np
mat   # 将数组转换为矩阵
rand = np.random.randn(4,4)    # 返回为array数组模式
rand = np.mat(rand)     # 使用mat函数将其转换为矩阵形式
rand.I                  # 求矩阵的逆

a.astype(float)      # 将数据a转换成浮点型
a.astype(int)
a.dtype              # 返回数据的类型

np.tile([1,2,3],2)   # 将数组重复两次  [1,2,3,1,2,3]
np.tile([1,2,3],(2,1))  # [[1,2,3],[1,2,3]]  行重复两次，列重复1次
np.tile([1,2,3],(2,2))  # 行重复两次，列重复两次

# 可见break的作用是提前结束循环。
n = 1
while n <= 100:
	if n > 10:     # 当n=11时，条件满足，执行break语句
		break      # break语句会结束当前循环
	print(n)
	n = n+1
print('end')

# 可见continue的作用是提前结束本轮循环，并直接开始下一轮循环
n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0:  # 如果n是偶数，执行continue语句
		continue   # continue语句会直接继续下一轮循环，后面的print语句不会被执行
	print(n)

# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]      # 待排序的数据
def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)      # L的每一个数组，作用于by_name函数，并返回每一个数组的第一个数据，按照这个数据进行排序
print(L2)

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return(ax)
	retrun(sum)
f = lazy_sum(1,3,5,7,9)   # 返回函数
f()         # 调用函数f时，才真正计算求和的结果：

# enumerate 函数用于遍历序列中的元素以及它们的下标：
for i,j in enumerate(('a','b','c')):
	print(i,j)
# 0 a
# 1 b
# 2 c

# yield的功能类似于return，但是不同之处在于它返回的是生成器
# 如果一个函数包含yield关键字，这个函数就会变成一个生成器
# 生成器并不会一次返回所有结果，而是每次遇到yield关键字后返回相应的结果，并保留
# 函数的当前运行状态，等待下一次的调用
# 由于生成器也是一个迭代器，那么它就支持next方法来获取下一个值
# 通过yield来创建生成器
def func():
	for i in range(10):
		yield i
# 通过列表来创建生成器
[i for i in range(10)]
# 调用如下
f = func()   # 此时生成器还没有运行
f.next()   # 当i=0时，遇到yield关键字，直接返回 0
f.next()  # 继续上一次执行的位置，进入下一层循环
f.next()  # 当执行完最后一次循环后，结束yield，生成stopiteration异常
f.send(2)  # send()就是next()的功能，加上传值给yield

def func():
	n = 0
	while 1:
		n = yield n  # 可以通过send函数向n赋值
f = func()

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

# pandas 中的 itertuples函数
import pandas as pd 
df = pd.DataFrame({'col1': [1, 2], 'col2': [0.1, 0.2]}, index=['a', 'b'])
for row in df.itertuples():
	print(row)                  # 返回的是对应的每一行数据的Index名称，以及相应的数值
# Pandas(Index='a', col1=1, col2=0.10000000000000001)
# Pandas(Index='b', col1=2, col2=0.20000000000000001)

# append 与 extend 区别
a = [1,2]
b = [3,4,5]
a.append(b)  # [1,2,[3,4,5]]  是在后面加上数组
a.extend(b)  # [1,2,3,4,5]    加上元素

### pandas中的join
df.join(df1)   # join是使用index进行数据的合并

# item的使用
x = np.random.randint(9,size=(3,3))
x.item(3)   #　返回数组中第3个元素
x.item(7)   #  返回数组中第7个元素
x.item((0,1))   # 返回数组中第0行，第1列的元素


# 对于python3无has_key这个函数，可以使用in代替

a = [{'a':2,'b':3},{'a':2,'c':1}]
for i in range(len(a)):
    print(a[i])
    if 'b' in a[i]:
        print(a[i]['b'])
    else:
        print(None)

# 对于上述的代码，可以简写成下面的格式，灵活使用if函数
for i in range(len(a)):
	print(a[i]['b'] if 'b' in a[i] else None)

a = [{'a':2,'b':3},{'a':2,'c':1}]
b = []
for i in range(len(a)):
	b.append(a[i]['b'] if 'b' in a[i] else None)
print(b)
