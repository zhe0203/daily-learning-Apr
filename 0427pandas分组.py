# Group By: split-apply-combine
import pandas as pd
import numpy as np
	# 将数据按组分开
	# 将每组数据应用于函数
	# 合并数据至一个数据结构
	# 分组数据将不包含NA值
# 将数据按组分割
if __name__=='__main__':
	df=pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
		'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],
		'C' : np.random.randn(8),
		'D' : np.random.randn(8)})
	grouped=df.groupby('A')
	grouped=df.groupby(['A','B'])

	def get_letter_type(letter):
		if letter.lower() in 'aeiou':
			return('vowel')
		else:
			return('consonant')
	grouped = df.groupby(get_letter_type, axis=1)

	lst = [1, 2, 3, 1, 2, 3]
	s=pd.Series([1,2,3,10,20,30],lst)
	grouped=s.groupby(level=0)
	grouped.first()   # 每组中第一个出现的元组
	grouped.lat()     # 每组中最后一个出现的元素
	grouped.sum()    # 对于每组求和

# GroupBy sorting
	df2=pd.DataFrame({'X':['B','B','A','A'],'Y':[1,2,3,4]})
	df2.groupby(['X']).sum()
	df2.groupby(['X'],sort=False).sum()
	df3.groupby(['X']).get_group('A')
	df3.groupby(['X']).get_group('B')

# GroupBy object attributes
	df.groupby('A').groups   #  可以查看每一组的内容
	df.groupby(get_letter_type, axis=1).groups
	# {'consonant': Index([u'B', u'C', u'D'], dtype='object'),
	#  'vowel': Index([u'A'], dtype='object')}

# GroupBy with MultiIndex
	arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
			  ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
	index = pd.MultiIndex.from_arrays(arrays,names=['first','second'])
	s=pd.Series(np.random.randn(8),index=index)
	grouped = s.groupby(level=0)   # 按照第一个索引名称进行分组
	grouped = s.groupby(level=1)   # 按照第二个索引名称进行分组
	grouped.sum()
	s.groupby(level='second').sum()
	s.sum(level='second')
	s.groupby(level=['first', 'second']).sum()

# DataFrame column selection in GroupBy
	grouped = df.groupby(['A'])
	grouped_C = grouped['C']     # 返回的是分组后C列的不同分组数据
	grouped.get_group('foo')['C']  # 返回的是foo组，C列的数据
	grouped_D = grouped['D']

# Iterating through groups¶
	grouped=df.groupby('A')
	for name,group in grouped:
		print(name)
		print(group)

	for name, group in df.groupby(['A', 'B']):  # 返回每一组的数据
		print(name)
		print(group)

# Selecting a group
	grouped.get_group('bar')   # 返回bar组的数据
	df.groupby(['A', 'B']).get_group(('bar', 'one'))

# Aggregation
	# An obvious one is aggregation via the aggregate or equivalently agg method:
	grouped = df.groupby('A')
	grouped.aggregate(np.sum)
	# 上述的返回结果使用分组的元素来充当索引序号，如果不用其，可如下设置
	grouped=df.groupby(['A','B'],as_index=False)
	grouped.aggregate(np.sum)
	df.groupby('A', as_index=False).sum()
	# 当然也可以使用reset_index函数来重新设置索引序号
	df.groupby(['A','B']).sum().reset_index()

	# 计算每组数据的大小，多少  size
	grouped.size()
	grouped.describe()   # 返回每组数据的描述性统计量

# Applying multiple functions at once
	grouped = df.groupby('A')
	grouped['C'].agg([np.sum, np.mean, np.std])  # 对于C列按分组计算值
	grouped['D'].agg({'result1' : np.sum,'result2' : np.mean}) # 对数据进行命名
	# 若果想对每一列数据都进行计算
	grouped.agg([np.sum,np.mean,np.std])

# Applying different functions to DataFrame columns
	grouped.agg({'C' : np.sum,'D' : lambda x: np.std(x, ddof=1)}) #对于数据的每一列计算不同的数值
	# 这里是对于C D两列计算公式
	grouped.agg({'C' : 'sum', 'D' : 'std'})
	grouped.agg({'D':'std','C':'mean'})   # 不能改变数据的输出顺序
	## 若想改变数据的输出顺序，可按照如下操作
	grouped.agg(orderedDict([('D','std'),('C','mean')]))

# Transformation
	index=pd.date_range('10/1/1999',periods=1100)
	ts=pd.Series(np.random.normal(0.5,2,1100),index)
	ts=ts.rolling(window=10,min_periods=100),mean().dropna()
	key=lambda x:x.year
	zscore=lambda x:(x-x.mean())/x.std()
	transformed = ts.groupby(key).transform(zscore)
	grouped=ts.groupby(key)

	### 对于分组后的数据
	grouped_trans=transformed.groupby(key)
	grouped_trans.mean()   # 计算变型后的分组每一组的值
	grouped_trans.std()

	# 使用每一组的均值去代替组内的缺失值
	countries = np.array(['US', 'UK', 'GR', 'JP'])
	key = countries[np.random.randint(0, 4, 1000)]
	grouped = data_df.groupby(key)
	grouped.count()
	f=lambda x:x.fillna(x.mean())
	transformed=grouped.transform(f)
	# ffill bfill fillna

# filtration
	sf=pd.Series([1,1,2,3,3,3])
	# fiter按条件返回原数据中的值 必须是一个函数def
	sf.groupby(sf).filter(lambda x:x.sum()>2)  # 筛选每组之和大于2的那一组的值
	dff = pd.DataFrame({'A': np.arange(8), 'B': list('aabbbbcc')})
	dff.groupby('B').filter(lambda x: len(x) > 2) # 返回组内元素大于2的那一组数值
	dff.groupby('B').filter(lambda x: len(x) > 2, dropna=False)
	dff['C']=np.arange(8)
	dff.groupby('B').filter(lambda x:len(x['C'])>2)
	dff.groupby('B').head(2)   # 返回每组数据的前两个数据

# Dispatching to instance methods
	grouped=df.groupby('A')
	grouped.agg(lambda x:x.std())

	s=pd.Series([9,8,7,5,19,1,4.2,3.3])
	g=pd.Series(list('abababab'))
	gb=s.groupby(g)
	gb.nlargest(3)   # 返回每一组最大的3个数据
	gb.nsmallest(3)  # 返回每组最小的3个数据

# Flexible apply
	grouped=df.groupby('A')  # 按照A列进行分组
	grouped['C'].apply(lambda x:x.describe())   # 对于分组的C列返回描述性统计量

	grouped=df.groupby('A')['C']
	def f(group):
		return(pd.DataFrame({'original':group,
							 'demeaned':group-group.mean()}))
	# 下面代码是对于C列运用上述的自定义函数进行运算
	grouped.apply(f)

	def f(x):
		return(pd.Series([ x, x**2 ], index = ['x', 'x^2']))
	s.apply(f)

	#apply can act as a reducer, transformer, or filter function, depending on exactly what is passed to it

# Grouping with ordered factors
	data=pd.Series(np.random.randn(10))
	# 按照数据分切分，其每一组的数据的计算方式
	factor=pd.qcut(data,[0,0.25,0.5,0.75,1])
	data.groupby(factor).mean()
	# [-2.617, -0.684]    -1.331461
	# (-0.684, -0.0232]   -0.272816
	# (-0.0232, 0.541]     0.263607
	# (0.541, 2.369]       1.166038

# Taking the first rows of each group
	df=pd.DataFrame([[1,2],[1,4],[5,6]],columns=['A','B'])
	df.groupby('A').head()
	df.groupby('A').tail(1)

# Taking the nth row of each group
	df = pd.DataFrame([[1, np.nan], [1, 4], [5, 6]], columns=['A', 'B'])
	g = df.groupby('A')
	g.nth(0)  # 返回每一组的第一个数据
	g.nth(1)  # 返回每一组的第二个数据
	g.nth(-1)  # 返回每一组的最后一个数据
	g.nth(0,dropna='any')  # 删除缺失值
	g.first()
	g.nth(-1, dropna='any')
	g.last()
	g.B.nth(0, dropna=True)
	# 通过设置as_index=False可以将索引位置不设置为索引标签
	g = df.groupby('A',as_index=False)  #

# Enumerate group items
	df=pd.DataFrame(list('aaabba'),columns=['A'])
	df.groupby('A').cumcount()  # 对于每一组的值进行计数
	df.groupby('A').cumcount(ascending=False)  # kwarg only

	df = pd.DataFrame({'a':[1,0,0], 'b':[0,1,0], 'c':[1,0,0], 'd':[2,3,4]})
	df.groupby(df.sum(),axis=1).sum()
