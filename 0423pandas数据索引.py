# Indexing and Selecting Data
	# s对于series索引数据，只需要指定一个参数
	# 对于DataFrame数据索引，可指定一个，也可指定两个参数
import pandas as pd
import numpy as np
# basics
	# series 使用label
	# DataFrame 使用colname
	# Panel 使用 itemname
	dates=pd.date_range('1/1/2000',periods=8)
	df=pd.DataFrame(np.random.randn(8,4),index=dates,columns=list('ABCD'))
	panel=pd.Panel({'one':df,'two':df-df.mean()})

	s=df['A']   # A列数据
	s[dates[5]]   # A列第5行数据

	panel['two']  # 取panel数据的item
	panel.two     # 返回结果与上述类似
	df[['B','A']]=df[['A','B']]
	df.loc[:,['A','B']]
	df.loc[:,['B', 'A']] = df[['A', 'B']].values  # 将值赋值给新的列

# Attribute Access
	sa = pd.Series([1,2,3],index=list('abc'))
	dfa=df.copy()
	sa.a=5      # 将a的值赋值给5
	dfa.A=list(range(len(dfa.index)))
	dfa['A'] = list(range(len(dfa.index)))  # use this form to create a new column
	x = pd.DataFrame({'x': [1, 2, 3], 'y': [3, 4, 5]})
	x.iloc[1] = dict(x=9, y=99)

# Slicing ranges
	s[:5]   # 取第0行到第4行的数据
	s[::2]  # 取间隔两个数的数据 0 2 4 6 8
	s[::-1]  # 对于数据进行倒排序
	s2=s.copy()
	s2[:5]=0  # 将第0行至第4行数据赋值给0
	# 对于dataframe
	df[:3]
	df[::-1]

# selection by label
# 使用标签索引左右都会包含数据
	df1=pd.DataFrame(np.random.randn(5,4),columns=list('ABCD'),
		index=pd.date_range('20130101',periods=5))
	df1.loc[2:3]  # 错误用法，loc是标签索引
	df1.iloc[2:3] # 正确用法
	df1.loc['20130103':'20130104']
	df1.loc['d':,'A':'C']
	df1.loc['a']>0
	df1.loc[:,df1.loc['a']>0]
	df1.loc['a','A']  # 等价于 df1.at['a','A']

# selection by position
# 使用位置索引数据，左闭右开返回数据，右边位置将不会包含在内
	s1=pd.Series(np.random.randn(5),index=list(range(0,10,2)))
	s1.iloc[:3]  #第0行至第3行数据
	s1.iloc[3]  # 第4行数据
	s1.iloc[:3]=0
	df1.iloc[1:5,2:4]
	df1.iloc[[1,3,5],[1,3]]
	df1.iloc[1:3,:]
	df1.iloc[:,1:3]
	df1.iloc[1, 1]   # 等同于 df1.iat[1,1]
	df1.iloc[1]      # 选取第一列的数据

	x=list('abcdef')
	x[4:10]    # 超出的长度将不会出现数据
	x[8:10]    # 不包含的数据，结果返回 []
	s = pd.Series(x)
	s.iloc[4:10]   # e f
	s.iloc[8:10]   # 空数组  []

	dfl = pd.DataFrame(np.random.randn(5,2), columns=list('AB'))
	df1.iloc[:,2:3]  # 不包含的列，将返回空值
	df1.iloc[:,1:3]  # 仅返回有数组的列

# Selection By Callable
	df1=pd.DataFrame(np.random.randn(6,4),index=list('abcdef'),
		columns=list('ABCD'))
	df1.loc[lambda df:df.A>0,:]
	df1.loc[:,lambda df:['A','B']]
	df1.iloc[:, lambda df: [0, 1]]
	df1[lambda df:df.columns[0]]
	df1.A.loc[lambda s:s>0]

	bb = pd.read_csv('data/baseball.csv', index_col='id')
	(bb.groupby(['year','team'])).sum().loc[lambda df:df.r>100]

# Selecting Random Samples 随机选取数据
	s=pd.Series([0,1,2,3,4,5])
	s.sample()   # 随机选取1个数据
	s.sample(3)  # 随机选取3个数据
	s.sample(frac=0.6)   # 选取百分之多少的数据，按比例选取数据
	s.sample(6,replace=False)   # 无放回的选取数据
	s.sample(7,repalce=True)    # 有放回的选取数据
	# 若想要对每个数取的概率设置不同，可以通过如下方式实现
	example_weights=[0,0,0.2,0.2,0.2,0.4]
	s.sample(n=3,weights=example_weights)
	example_weights2 = [0.5, 0, 0, 0, 0, 0]
	s.sample(n=1,weights=example_weights2)

	df2=pd.DataFrame({'coll':[9,8,7,6],'weight_colun':[0.5,0.4,0.1,0]})
	df2.sample(n=3,weights='weight_column')
	# 随机选取列
	df3=pd.DataFrame({'coll':[1,2,3],'col2':[2,3,4]})
	df3.sample(n=1,axis=1)   # 随机选择列
	# 可以设定随机种子，以便返回结果一样
	df3.sample(n=2,random_state=2)
	df3.sample(n=2,random_state=2)  #返回结果一样

# Setting With Enlargement
	se = pd.Series([1,2,3])
	se[5]=5   # 添加数据
	dfi = pd.DataFrame(np.arange(6).reshape(3,2),
		columns=['A','B'])
	dfi.loc[:,'C']=dfi.loc[:,'A']  # 添加数据
	dfi.loc[3] = 5

# fast scalar value getting and setting
	# .at为标签索引  .iat为数值索引
	# 快速获取某个位置的数据
	s.iat[5]
	df.at[dates[5],'A']
	df.at[dates[5], 'E'] = 7
	df.iat[3,0]=7
	df.at[dates[-1]+1, 0] = 7

# Boolean indexing
	# |for or  & for and  ~ for not
	s=pd.Series(range(-3,4))
	s[s>0]
	s[(s<-1)|(s>0.5)]
	s[~(s<0)]
	# 对数据框的选取方式
	df[df['A']>0]

	df2=pd.DataFrame({'a':['one','one','two','three','two','one','six'],
					  'b':['x','y','y','x','y','x','x'],
					  'c':np.random.randn(7)})
	# 只取 two 和 three的数据
	criterion=df2['a'].map(lambda x:x.startswith('t'))  # 判断是否是t开头的变量
	df2[criterion]
	# 等价于
	df2[[x.startswith('t') for x in df2['a']]]
	df2[criterion & (df2['b']=='x')]
	df2.loc[criterion & (df2['b'] == 'x'),'b':'c']

# indexing with isin
	s=pd.Series(np.arange(5),index=np.arange(5)[::-1],dtype='int64')
	s.isin([2,4,6])   # 判断s的每一个数是否在[2,4,6]数组中
	s[s.isin([2,4,6])]
	s.index.isin([2,4,6])
	s[[2,4,6]]   # 取第2,4,6个数
	
	# 更加复杂的索引
	s_mi=pd.Series(np.arange(6),
		index=pd.MultiIndex.from_product([[0,1],['a','b','c']]))
	s_mi.iloc[s_mi.index.isin([(1,'a'),(2,'b'),('0','c')])]
	s_mi.iloc[s_mi.index.isin(['a','c','e'],level=1)]   # 这里设置level

	df = pd.DataFrame({'vals': [1, 2, 3, 4], 'ids': ['a', 'b', 'f', 'n'],
		'ids2': ['a', 'n', 'c', 'n']})
	values=['a','b',1,3]
	df.isin(values)     # 对于数据框的每一个数值都检验其是否在该数据中
	# 如果想要检查每一列的值是否在也定的数据中，使用如下格式
	values={'ids':['a','b'],'vals':[1,3]}
	df.isin(values)
	values = {'ids': ['a', 'b'], 'ids2': ['a', 'c'], 'vals': [1, 3]}
	row_mask=df.isin(values).all(axis=1)

# the where() method and masking
	s=pd.Series(np.arange(5),index=np.arange(5)[::-1])
	s[s>0]   # 返回仅含有大于0的数值
	s.where(s>0)   # 不大于0 的数值也会返回，当做NAN值
	# 对于数据框
	df.where(df<0)   # 返回结果的维度与之前一样
	df.where(df<0,-df)  # 若小于0，将该数值赋值给-df
	s2=s.copy()
	s2[s2<0]=0
	df2=df.copy()
	df2[df2<0]=0
	df_orig = df.copy()
	df_orig.where(df>0,-df,inplace=True)   # 添加inplace将会改变原有数据
	np.where(df < 0, df, -df)

	df2=df.copy()
	df2.where(df2>0,df2['A'],axis='index')
	# 等价于
	df.apply(lambda x,y:x.where(x>0,y),y=df['A'])

	df3=pd.DataFrame({'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]})
	df3.where(lambda x:x>4,lambda x:x+10)  # 多个函数运算

	s.mask(s >= 0)   # mask取相反的值
	df.mask(df>=0)  # 返回小于等于0的数值

# The query() Method (Experimental)
	n=10
	df=pd.DataFrame(np.random.randn(10,3),columns=list('abc'))
	df[(df.a<df.b) & (df.b<df.c)]
	df.query('(a<b) & (b<c)')

	df = pd.DataFrame(np.random.randint(n / 2, size=(n, 2)), columns=list('bc'))
	df.index.name='a'
	df.query('a<b and b<c')

	df = pd.DataFrame(np.random.randint(n, size=(n, 2)), columns=list('bc'))
	df.query('index<b<c')
	# Note If the name of your index overlaps with a column name, the column name is given precedence. For example,
	df=pd.DataFrame({'a':np.random.randint(5,size=5)})
	df.index.name='a'
	df.query('a>2')   # 此时使用的是列名称
	# 若想使用行名称
	df.query('index>2')

	# MultiIndex query() Syntax
	n=10
	colors=np.random.choice(['red','green'],size=n)
	foods=np.random.choice(['eggs','ham'],size=n)
	index = pd.MultiIndex.from_arrays([colors, foods], names=['color', 'food'])   # 设置更加复杂的索引标签
	df = pd.DataFrame(np.random.randn(n, 2), index=index)
	df.query('color=="red"')

	df.index.names = [None, None]  # 将数据序列名称未设置
	df.query('ilevel_0=="red"')
	df.query('ilevel_1=="ham"')   # index level 0

	# query() Use Cases
	df=pd.DataFrame(np.random.randn(n,3),columns=list('abc'))
	df2=pd.DataFrame(np.random.randn(n+2,3),columns=df.columns)
	expr='0.0<=a<=c<=0.5'
	map(lambda frame:frame.query(expr),[df,df2]) # map第二个参数为可迭代对象
	df.query('a < b < c')

# The in and not in operators
	df = pd.DataFrame({'a': list('aabbccddeeff'), 'b': list('aaaabbbbcccc'),
		'c':np.random.randint(5,size=12),'d':np.random.randint(9,size=12)})
	df.query('a in b')  # a中的数据包含在b中
	df[df.a.isin(df.b)]
	df.query('a not in b')
	df[~df.a.isin(df.b)]
	df.query('a in b and c < d')
	df[df.b.isin(df.a) & (df.c<df.d)]

# Special use of the == operator with list objects
	df.query('b==["a","b","c"]')
	df[df.b.isin(["a", "b", "c"])]
	df.query('c == [1, 2]')
	df.query('c != [1, 2]')
	df.query('[1, 2] in c')
	df.query('[1,2] not in c')
	df[df.c.isin([1,2])]

# boolean oprators
	df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
	df['bools'] = np.random.rand(len(df)) > 0.5
	df.query('~bools')   # 返回False值
	df.query('bools')
	df.query('not bools')==df[~df.bools]  # 判断两个数据每一个值是否相等
	shorter = df.query('a < b < c and (not bools) or bools > 2')
	longer = df[(df.a < df.b) & (df.b < df.c) & (~df.bools) | (df.bools > 2)]

# Duplicate Data 重复的数据
	# 使用duplicated and drop_duplicates 删除重复数据
	df2 = pd.DataFrame({'a': ['one', 'one', 'two', 'two', 'two', 'three', 'four'],
		'b': ['x', 'y', 'x', 'y', 'x', 'x', 'x'],
		'c': np.random.randn(7)})
	df2.duplicated('a')
	df2.duplicated('a', keep='last')
	df2.duplicated('a', keep=False)  # 显示所有的重复值，都是True
	df2.drop_duplicates('a')  # 近保留第一个
	df2.drop_duplicates('a',keep='last')  #保留最后一个
	df2.drop_duplicates('a', keep=False) # 将是重复值的数据全部删除
	df2.duplicated(['a', 'b'])
	df2.drop_duplicates(['a', 'b'])
	df3 = pd.DataFrame({'a': np.arange(6),
						 'b': np.random.randn(6)}, index=['a', 'a', 'b', 'c', 'b', 'a'])
	df3.index.duplicated()
	df3[~df3.index.duplicated()]
	df3[~df3.index.duplicated(keep='last')]

# Dictionary-like get() method	
	s=pd.Series([1,2,3],index=['a','b','c'])
	s.get('a')
	s.get('x',default=-1)  #　当不存在该数据时，返回-1

# The select() Method
	df.select(lambda x:x=='A',axis=1)

# The lookup() Method
	dflookup = pd.DataFrame(np.random.rand(20,4), columns = ['A','B','C','D'])
	dflookup.lookup(list(range(0,10,2)), ['B','C','A','B','D']) # B列的第0个数据 C列的第2个数据

# Index objects
	index=pd.Index(['e','d','a','b'])
	'd' in index
	index = pd.Index(['e', 'd', 'a', 'b'], name='something')
	index.name     # 'something'
	ind=pd.Index([1,2,3])
	ind.rename('apple')
	ind.set_names(['apple'],inplace=True)
	ind.name='bob'
	index.levels[1]
	index.set_levels(["a", "b"], level=1)
	# union(|)   interaction(&)
	a = pd.Index(['c', 'b', 'a'])
	b = pd.Index(['c', 'e', 'd'])
	a|b
	a&b
	a.difference(b)
	idx1.symmetric_difference(idx2)  # 出现在idx1或者idx2中，但不出现在两者中
	idx1.difference(idx2).union(idx2.difference(idx1)) 

# Set / Reset Index
	data=pd.DataFrame({'a':['bar','bar','foo','foo'],
				'b':['one','two','one','two'],
				'c':['z','y','x','w'],'d':[1,2,3,4]})
	indexed1 = data.set_index('c')  #将c列变成行索引名称
	indexed2 = data.set_index(['a', 'b']) # 将a,b列
	frame = data.set_index('c', drop=False)  # c列不删除
	frame.set_index(['a','b'],append=True)
	data.set_index(['a', 'b'], inplace=True)  # inplace是否改变data数据

# Reset the index
	data.reset_index()  # 返回原有设置
	frame.reset_index(level=1)

	dfb['c'][dfb.a.str.startswith('o')] = 42
