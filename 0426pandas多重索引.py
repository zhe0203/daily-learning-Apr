# Creating a MultiIndex (hierarchical index) object
import pandas as pd
import numpy as np
# 对于多个索引，若来自数组，则使用MultiIndex.from_arrays
# 对于多个索引，若来自元组，则使用MultiIndex.from_tuples
#  a crossed set of iterables (using MultiIndex.from_product)
	index = pd.MultiIndex.from_product([[0,1,2],['2012-01-01','2012-01-02','2012-01-03']],names=['first', 'second'])
	df = pd.DataFrame(np.random.randn(9, 4), index=index,columns=list('abcd'))
	print(df)
	df_1 = df.loc[(slice(None),'2012-01-01'),:]  # panel数据切片
	print(df_1)

	arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
		['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
	# zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表。
	# 在函数调用中使用*list/tuple的方式表示将list/tuple分开，作为位置参数传递给对应函数
	tuples=list(zip(*arrays))  # 将数组转换成元组
	index=pd.MultiIndex.from_tuples(tuples,names=['first','second'])
	# 也可以使用
	index=pd.MultiIndex.from_arrays(arrays,names=['first','second'])
	s=pd.Series(np.random.randn(8),index=index)

	# 还可以使用如下方法
	iterables=[['bar','baz','foo','qux'],['one','two']] 
	# 相当于R语言中的expand.grid()
	pd.MultiIndex.from_product(iterables,names=['first','second'])

	# 最方便的是直接给定数组arrays
	arrays = [np.array(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux']),
		np.array(['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'])]
	s=pd.Series(np.random.randn(8),index=arrays)
	df=pd.DataFrame(np.random.randn(8,4),index=arrays)

	df=pd.DataFrame(np.random.randn(3,8),index=['A','B','C'],columns=index)
	pd.DataFrame(np.random.randn(6,6),index=index[:6],columns=index[:6])
	pd.Series(np.random.randn(8), index=tuples) # 使用元组作为index
	# 设置数据的显示方式
	pd.set_option('display.multi_sparse',False) # 每一个数据索引都显示
	pd.set_option('display.multi_sparse',True)  # 只显示第一个索引

# Reconstructing the level labels
	index.get_level_values(0)  # 返回每一个index的索引名称
	index.get_level_values('second')
	index.get_level_values(1)

# Basic indexing on axis with MultiIndex
	df['bar']
	df['bar','one']
	df['bar']['one']
	df.columns
	df[['foo','qux']].columns
	df[['foo','qux']].columns.values # 返回真正的索引名称
	df[['foo','qux']].columns.get_level_values(0)
	pd.MultiIndex.from_tuples(df[['foo','qux']].columns.values)

# Data alignment and using reindex
	# 数据的运算
	s+s[:-2]  # 与nan运算，返回nan值
	s+s[::2]
	s.reindex(index[:3])  # 返回前3行数据
	# 按照索引元组进行返回数据
	s.reindex([('foo', 'two'), ('bar', 'one'), ('qux', 'one'), ('baz', 'one')])

# Advanced indexing with hierarchical index
	df.T   # 进行转置
	df.loc['bar']
	df.loc['bar','two']  # 等同于  df['bar','one']
	df.loc[('baz','two'):('qux','one')]
	df.loc[('baz','two'):'foo']
	df.ix[[('bar', 'two'), ('qux', 'one')]]
	def mklbl(prefix,n):
		return(['%s%s' % (prefix,i) for i in range(n)])
	miindex=pd.MultiIndex.from_product([mklbl('A',4),mklbl('B',2),mklbl('C',4),mklbl('D',2)])
	micolumns = pd.MultiIndex.from_tuples([('a','foo'),('a','bar'),('b','foo'),('b','bah')],
											names=['lvl0', 'lvl1'])
	dfmi = pd.DataFrame(np.arange(len(miindex)*len(micolumns)).reshape((len(miindex),len(micolumns))),index=miindex,
		columns=micolumns).sort_index().sort_index(axis=1)
	dfmi.loc[(slice('A1','A3'),slice(None),['C1','C3']),:]
	
	idx=pd.IndexSlice
	dfmi.loc[idx[:,:,['C1','C3']],idx[:,'foo']]
	mask=dfmi[('a','foo')]>200
	dfmi.loc[idx[mask,:,['C1','C3']],idx[:,'foo']]
	dfmi.loc(axis=0)[:,:,['C1','C3']]
	df2.loc(axis=0)[:,:,['C1','C3']] = -10
	df2.loc[idx[:,:,['C1','C3']],:]=df2*1000

# Cross-section
	df.xs('one',level='second') # 选取second的one一列数据
	df.xs('bar',level='first') # df.xs('bar')
	df.loc[(slice(None),'one'),:]	
	df.loc[('bar','one'),:]
	df.loc[(slice('bar'),'one'),:]
	df=df.T
	df.xs('one', level='second', axis=1)
	df.loc[:,(slice(None),'one')]
	df.xs(('one', 'bar'), level=('second', 'first'), axis=1)
	df.loc[:,('bar','one')]
	df.xs('one', level='second', axis=1, drop_level=False) # 保留索引的名称
	df.xs('one',level='second',axis=1,drop_level=True)  #删除索引的名称

# Advanced reindexing and alignment
	midx=pd.MultiIndex(levels=[['zero','one'],['x','y']],
					labels=[[1,1,0,0],[1,0,1,0]])
	df=pd.DataFrame(np.random.randn(4,2),index=midx)
	df2 = df.mean(level=0)
	df2.reindex(df.index,level=0)
	# 将df赋值给df_aligned 将df2赋值给df2_aligned
	df_aligned, df2_aligned = df.align(df2, level=0)

# Swapping levels with swaplevel()
	# 转换索引名称
	df[:5].swaplevel(0,1,axis=0)  # 索引名称互换

# Reordering levels with reorder_levels()
	df[:5].reorder_levels([1,0], axis=0)

# Sorting a MultiIndex 对于索引进行排序
	import random
	random.shuffle(tuples)
	s=pd.Series(np.random.randn(8),index=pd.MultiIndex.from_tuples(tuples))
	s.sort_index()   # 默认level=0
	s.sort_index(level=1)
	# 通过索引name进行排序
	s.index.set_names(['L1', 'L2'], inplace=True)
	s.sort_index(level='L1')
	df.T.sort_index(level=1, axis=1)
	dfm = pd.DataFrame({'jim': [0, 0, 1, 1],
		'joe':['x','x','z','y'],
		'jolie':np.random.rand(4)})
	dfm=dfm.set_index(['jim','joe']) # 将jim 和joe两列设置成行索引名称
	dfm.loc[(1,'z')]
	dfm.index.is_lexsorted()    # 判断是否排序
	dfm.index.is_lexsort_depth  # 返回排序的深度
	dfm.loc[(0,'y'):(1, 'z')]

# Take Methods
	index=pd.Index(np.random.randint(0,1000,10))
	positions=[0,9,3]
	index[positions]
	index.take(positions)
	ser=pd.Series(np.random.randn(10))
	ser.iloc[positions]
	ser.take(positions)
	frm = pd.DataFrame(np.random.randn(5, 3))
	frm.take([1, 4, 3])
	frm.take([0,2],axis=1)
	
	arr=np.random.randn(10)
	arr.take([False,True,False,True])

# Index Types
	df.dtypes   # 查看数据类型
	df.B.cat.categories
	indexf=pd.Index([1.5,2,3,4.5,5])
	sf=pd.Series(range(5),index=indexf)
	sf.loc[3.0]  # 浮点型数据作为索引
