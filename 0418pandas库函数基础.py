# Essential Basic Functionality
# 加载库
	import pandas as pd
	import numpy as np

# 创建一个简单的数据结构
if __name__=='__main__':
	index=pd.date_range('1/1/2000',periods=8)
	s=pd.Series(np.random.randn(5),index=list('abcde'))
	df=pd.DataFrame(np.random.randn(8,3),index=index,columns=['A','B','C'])
	# 创建面板数据
	wp=pd.Panel(np.random.randn(2,5,4),items=['item1','item2'],
				major_axis=pd.date_range('1/1/2000',periods=5),
				minor_axis=['A','B','C','D'])

# head and tail
	long_series = pd.Series(np.random.randn(1000))
	long_series.head()    # 查看前5行数据
	long_series.tail(3)   # 查看后3行数据

# attribute and the raw ndarray(s)
	df[:2]     #前两行的数据
	df.columns=[x.lower() for x in df.columns] # 将列名转化为小写，并赋值给新的列名
	df.values    # 返回数据df的值

# matching /broadcasting behavior
	df = pd.DataFrame({'one' : pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
						'two':pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
						'three' : pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})
	row=df.ix[1]   # 提取第2行的数据
	df.loc[:,'one']
	colums=df['two']
	df.sub(row,axis='columns')  # 按照行进行相减
	df.sub(row,axis=1)
	df.sub(column,axis='index')  # 按照列进行相减
	df.sub(column,axis=0)

	dfmi=df.copy()
	dfmi.indx=pd.MultiIndex.from_tuples([(1,'a'),(1,'b'),(1,'c'),(2,'a')],
										names=['first','second'])
	dfmin.sub(column,axis=0,level='second')  # 选取second列，按列进行相减
	# 对于面板数据
	major_mean=wp.mean(axis='major')
	wp.sub(major_mean,axis='major')
	# divmod 相除并去余数 x//y  x%y
	s=pd.Series(np.arange(10))
	div,rem=divmod(s,3)  # 将每个数与3整除的值赋值给div，余数赋值给rem
	# 使用Index
	idx=pd.Index(np.arange(10))
	div,rem=divmod(idx,3)
	# 也可以对于每一个数分别除以不同的数
	div,rem=divmod(s,[2,2,3,3,4,4,5,5,6,6])

# missing data operation with fill values
	df # df数据包含缺失值
	df.add(df2,fill_value=0)   # 将缺失值替换成0

# Boolean Reductions empty() any() bool()
	(df>0).all() # 是否每一列所有的值都大于0
	(df>0).any() # 是否每一列中存在大于0的数值
	(df>0).any().any()  # True
	df.empty    # 检验数据框是否为空
	pd.DataFrame(columns=list('ABC')).empty   # 该数据框为空
	pd.Series([True]).bool()   # 检验是否为布尔型数据
	pd.Series([[True]]).bool()

# Comparing if objects are equivalent
	df+df==df*2   # 缺失值不相等 np.nan==np.nan
	(df+df==df*2).all()
	# 将缺失值作为相等处理，使用equal
	(df+df).equals(df*2)  # True
	df1=pd.DataFrame({'col':['foo',0,np.nan]})
	df2=pd.	DataFrame({'col':[np.nan,0,'foo']},index=[2,1,0])
	df1.equals(df2)   # False
	df1.equals(df2.sort_index())

# Comparing array-like objects
	pd.Series(['foo','bar','baz'])=='foo'  # 判断是否等于foo
	pd.Index(['foo','bar','baz'])=='foo'
	# 不同数组之间的比较
	pd.Series(['foo', 'bar', 'baz']) == pd.Index(['foo', 'bar', 'qux'])
	pd.Series(['foo', 'bar', 'baz']) == np.array(['foo', 'bar', 'qux'])
	# 比较index 和 series数组，其二者必须相等
	pd.Series(['foo', 'bar', 'baz']) == pd.Series(['foo']) # 这是错误的，必须相等
	np.array([1, 2, 3]) == np.array([2]) # 对于数组可以不相等
	np.array([1, 2, 3]) == np.array([1, 2]) # 这种用法是比较两个数组数组是否相等

# Combining overlapping data sets
	# A.combine_first(B) 使用B的对应值去填充A的NAN值，返回A的值
	df1 = pd.DataFrame({'A' : [1., np.nan, 3., 5., np.nan],
						'B' : [np.nan, 2., 3., np.nan, 6.]})
	df2 = pd.DataFrame({'A' : [5., 2., 4., np.nan, 3., 7.],
						'B' : [np.nan, np.nan, 3., 4., 6., 8.]})
	df1.combine_first(df2)
	# 主要是下面的含义
	combineer=lambda x,y:np.where(pd.isnull(x),y,x) # 如果x中有null值，就填充为y的值
	df1.combine(df2,combiner)
	combine(self,other,func,fill_value=nan)

# Descriptive statistics
	# Series: no axis argument needed
	# DataFrame: “index” (axis=0, default), “columns” (axis=1)
	# Panel: “items” (axis=0), “major” (axis=1, default), “minor” (axis=2)
	df.mean(0)  # 对于每一列求均值
	df.mean(1)  # 对于每一行求均值
	df.sum(0,skipna=False)  # 是否将nan值纳入计算
	df.sum(axis=1,skipna=Ture)  # nan值不计入计算
	ts_stand = (df - df.mean()) / df.std()
	xs_stand = df.sub(df.mean(1), axis=0).div(df.std(1), axis=0)
	df.cumsum()  # 对于每一列进行累积求和
	df.count(axis=0)   # 计算每一行非null值的个数
	# nunique() 返回非null值唯一值的个数
	series=pd.Series(np.random.randn(500))
	series[20:500]=np.nan
	series[10:20]=5
	series.nunique()

# 浏览数据概况 summary  python中用describe不包含缺失值
	series = pd.Series(np.random.randn(1000))
	series[::2] = np.nan  # [::2] 表示间隔2取数
	series.describe()
	frame = pd.DataFrame(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
	frame.ix[::2] = np.nan
	frame.describe()     # 返回数据概况
	series.describe(percentiles=[.05, .25, .75, .95])  # 设置分位点
	# 对于非数值型数据,将会返回针对这组数据简单的概况
	s = pd.Series(['a', 'a', 'b', 'b', 'a', 'a', np.nan, 'c', 'd', 'a'])
	s.describe()
	# 对于两列中既有数值，又有非数值的，会返回含有数值的那一列
	frame = pd.DataFrame({'a': ['Yes', 'Yes', 'No', 'No'], 'b': range(4)})
	frame.describe()
	frame.describe(include=['object'])  # 仅返回非数值的那一列
	frame.describe(inclue=['number'])   # 近返回数值的那一列
	frame.describe(include='all')      # 返回所有的列

# index of Min/Max Values
	s1 = pd.Series(np.random.randn(5))
	s1.idxmin()  # 返回最小值的索引序号 与np中argmin()相似
	s1.idxmax()   # 返回最大值的索引序号 与np中argmax()相似
	df1.idxmin(axis=0)  # 返回每一列的最小值索引序号
	df1.idxmin(axis=1)  # 返回每一行的最小是的索引序号
	# 当含有两个及以上的最小值时，返回的是最前面的那个索引序号

# Value counts (histogramming) / Mode
	data = np.random.randint(0, 7, size=50)
	s=pd.Series(data)
	s.value_counts()    # 计算每个数出现个数
	pd.value_counts(data)
	# 得到数组中出现最多的数值
	s5 = pd.Series([1, 1, 3, 3, 3, 5, 5, 7, 7, 7])
	s5.mode()

# 分组数据
	arr=np.random.randn(20)
	factor=pd.cut(arr,4)  # 分成4组
	factor=pd.cut(arr,[-5,-1,0,1,5])  # 给定分组区间
	factor=pd.cut(arr,[0,0.25,0.5,0.75,1])  # 将数据按照比例均匀分开
	pd.value_counts(factor)
	arr = np.random.randn(20)
	factor = pd.cut(arr, [-np.inf, 0, np.inf])

# function application
	# 对于行、列数据 使用 apply()
	# 对于每一个数据 使用 applymap()
	# 对于数据组 使用 pipe() 管道函数 %>%
	(df.pipe(h)
		.pipe(g,arg1=a)
		.pipe(f,arg2=2,arg3=3)
		)
	import statsmodels.formula.api as sm
	bb = pd.read_csv('data/baseball.csv', index_col='id')
	(bb.query('h>0')
		.assign(ln_h=lambda df:np.log(df))
		.pipe((sm.possiom,'data').'hr~ln_h+year+g+C(lg)')
		.fit()
		.summary())

# apply()
	df.apply(np.mean)   # 对于每一列求均值
	df.apply(np.mean,axis=1)
	df.apply(lambda x:x.max()-x.min())
	df.apply(np.cumsum)
	df.apply(np.exp)

	tsdf=pd.DataFrame(np.random.randn(1000,3),columns=['A','B','C']，
				index=pd.date_range('1/1/2000',periods=1000))
	tsdf.apply(lambda x:x.idxmax())  # 返回每一列最大值索引的位置
	def subtract_and_divide(x, sub, divide=1):
		return (x - sub) / divide
	df.apply(subtract_and_divide, args=(5,), divide=3)

# Applying elementwise Python functions
	f=lambda x:len(str(x))
	df.applymap(f)  # 对于df中的每一个数使用函数f
	s = pd.Series(['six', 'seven', 'six', 'seven', 'six'],
					index=list('abcde'))
	t=pd.Series({'six':6,'seven':7})
	s.map(t)  # 对于s中的每一个six和seven都将其变成对应的数字

# Reindexing and altering labels
	s=pd.Series(np.random.randn(5),index=list("abcde"))
	s=reindex(['e','b','f','d'])   # 对于无f的一行数据，将显示NA值
	# 进行数据框的重新排列
	df.reindex(index=['c','f','b'],columns=['three','two','one']) #基于原始数据进行重新排序
	rs=s.reindex(df.index)

# reindexing to align with another object
	df.reindex_like(df2)   # 返回与df2相似的索引的序号数据

# Aligning objects with each other with align
	s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
	s1=s[:4]
	s2=s[1:]
	s1.align(s2)
	s1.align(s2,join='inner')  # 取s1和s2的交集
	s1.align(s2,join='left')
	df.align(df2, join='inner', axis=0)

# filling while reindexing
	# pad/ffill 向前填充
	# bfil/backfill 向后填充
	# nearest 最近填充
	rng=pd.date_range('1/3/2000',periods=8)
	ts=pd.Series(np.random.randn(8),index=rng)
	ts2=ts[[0,3,6]]    # 取第0行，第3行，第6行
	ts2.reindex(ts.index)   # 无数据的行将被填充为NA值
	ts2.reindex(ts.index,mothod='ffill')
	ts2.reindex(ts.index,mothod='bfill')
	ts2.reindex(ts.index, method='nearest')
	# 等价于
	ts2.reindex(ts.index).fillna(method='ffill')
	ts2.reindex(ts.index, method='ffill', limit=1) # 最大向前填充1个值
	ts2.reindex(ts.index,method='ffill',tolerance='1 day')

# dropping label from an axis
	df.drop(['a','d'],axis=0)  # 删除a d行数据
	df.reindex(df.index.difference(['a','d'])) # difference排除以外数据

# renaming/mapping labels
	s.rename(str.upper)
	df.rename(columns={'one':'foo','two':'bar'},index={'a':'apple','b':'banana','d':'durian'})

# .dt accessor
	s=pd.Series(pd.date_range('20130101 09:10:12',periods=4))
	s.dt.hour     # 提取小时数据
	s.dt.second   # 提取秒数据
	s.dt.year     # 提取年数
	s[s.dt.day==2]
	stz = s.dt.tz_localize('US/Eastern')   # 转换时间数据
	# strftime
	s = pd.Series(pd.date_range('20130101', periods=4))
	s.dt.strftime('%Y/%m/%d')
	s=pd.Series(pd.timedelta_range('1 day 00:00:05',period=4,frq='s'))
	s.dt.components   # 返回所有的时间内容

# Vectorized string methods
	s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
	s.str.lower()   # 转换成小写
	df1[['one', 'two', 'three']].sort_values(by=['one','two']) # 排序

# smallest / largest values
	s = pd.Series(np.random.permutation(10))
	s.sort_values()   # 排序，升序
	s.nsmallest(3)   # 返回最小的3个数
	s.nlargest(3)    # 返回最大的3个数
	# dataframe
	df = pd.DataFrame({'a': [-2, -1, 1, 10, 8, 11, -1],'b': list('abdceff'),'c': [1.0, 2.0, 4.0, 3.2, np.nan, 3.0, 4.0]})
	df.nlargest(3,'a')   # 返回a列最大的3个数
	df.nlargest(5,['a','c'])
	df.nsmallest(3,'a')

# object conversion
	# to_numeric()
	m=['1.1',2,3]
	pd.to_numeric(m)  # 将m变换为数值型数据 [1.1,2,3]
	m = ['apple', 2, 3]
	pd.to_numeric(m)  # array([ nan,   2.,   3.])
	# to_datetime
	import datetime
	m = ['2016-07-09', datetime.datetime(2016, 3, 2)]
	pd.to_datetime(m)
	# to_timedelta
	m = ['5us', pd.Timedelta('1day')]
	pd.to_timedelta(m)

	df=pd.DataFrame([['2016-07-09',datetime.datetime(2016,3,2)]]*2,dtype='o')
	df.apply(pd.to_datetime)
