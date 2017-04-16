# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 21:41:12 2016

@author: jk
"""

# 10 Minutes to pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

	dates=pd.date_range("20130101",periods=6)  # 生成时间序列，天数加1
	df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
	df2=pd.DateFrame({'A':1,
                  'B':pd.Timestamp('20130102'),
                  'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                  'D':np.array([3]*4,dtype='int32'),
                  'E':pd.Categorical(["test","train","test","train"]),
                  'F':'foo'})
	df2.dtypes 
	df.head()    # 查看数据的前5行数据
	df.tail()    # 查看数据的最后5行数据

# display the index,columns,and the undrlying numpy data
	df.index    # 查看索引名称
	df.columns     # 查看列名称
	df.values   #查看数据框的值
	df.describe()     # 相当于R中的summary函数，查看数据概况
	df.T       # 数据转置
	df.sort_index(axis=1,ascending=False)    # 数据通过索引的排序
	df.sort_values(by='B')        # 数据通过B列的值进行排序

# select
	df['A']    # 相当于df.A
	df[0:3]    # 提取前3行
	df['20130102':'20130104']   # 按照行名称进行提取数据

# selection by label
# loc 全部是使用行、列的标签名称进行索引
	df.loc[dates[0]]           # loc 表示通过标签进行提取
	df.loc[:,['A','B']]	       # 更加复杂的提取数据
	df.loc['20130102':'20130104',['A','B']]	
	df.loc['20130102',['A','B']] 
	df.loc[dates[0],'A']       # 得到具体的数字

# select by position
# iloc 全部使用整数来进行索引，给出一个参数，则是按照行取数
	df.iloc[3]        # 提取第4行数据
	df.iloc[3:5,0:2]
	df.iloc[[1,2,4],[0,2]]    # 通过行列的列表形式进行索引
	df.iloc[1:3,:]    # 等价于 df.iloc[1:3,]
	df.iloc[:,1:3]    # 选取第1至3列的所有行数据
	df.iloc[1,1]      # 得到某行某列的具体数据
	df.iat[1,1]       # 与iloc结果相同

# boolean indexing
	df[df.A>0]  # 按照逻辑值进行取数     
	df[df>0]
	# using the isin() method for filtering
	df2=df.copy()
	df2['E']=['one','one','two','three','four','three']
	df2[df2['E'].isin(['two','four'])]  # 通过判断E列中数据是否存在in中来进行索引

# setting
	s1=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130102',periods=6))
	df['F']=s1   # 将df数据增加新的列F，数值为s1
	df.at[dates[0],'A']=0   # .at 是通过标签索引  .iat 是通过数值索引
	df.iat[0,1]=0
	df.loc[:,'D']=np.array([5]*len(df))
	df2=df.copy()
	df2[df2>0]=-df2
	[5]*10
	(5,)*10
	(5)*10 # 50

# missing data
# numpy 使用np.nan表示缺失值，缺失值默认不加入计算
	df1=df.reindex(index=dates[0:4],columns=list(df.columns)+'E')
	df1.loc[dates[0]:dates[1],'E']=1
	# 删除所有含缺失值的行
	df['a'][[1,3]]=np.nan    # 将df数据的a列1,3行数据替换为NA值
	df1.dropna(how='any')
	# 填充缺失值
	df1.fillna(value=5)   # 将缺失值数据换成5
	pd.isnull(df1)        # 判断每一个数值是否是缺失和自豪

# stats
	df.mean()         # 默认求每一列的均值
	df.mean(axis=1)   # 求每一行的均值
	s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)   
	# .shift表示数据向后移动的个数
	df.sub(s, axis='index')

# apply
	df.apply(np.cumsum)    # 对于每一列进行累加
	df.apply(lambda x:x.max()-x.min()) # 可通过设置axis进行设置

# histogramming
	s=pd.Series(np.random.randint(0,7,size=10))
	# randint 产生0到7之间的数10个
	# randn  产生的数据服从标准正态分布
	s.value_counts()    # 计算每一个数的个数

# string method
	s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
	s.str.lower()    # 转换成小写  numpy库

# merge
	df = pd.DataFrame(np.random.randn(10, 4))
	pieces=[df[:3],df[3:7],df[7:]]
	pd.concat(pieces)   # 将数据进行合并

# join
	left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
	right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
	pd.merge(left,right,on='key')
	A.merge(B,left_on='1key',right_on='rkey',how='outer')
	# how left(left outer join) right(right outer join) outer(full outer join)	inner(inner join)

# append
	df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
	s=df.iloc[3]
	df.append(s.ignore_index=True)	# igore_index 是否使用原有的行名称

# grouping
	df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],'B' : ['one', 'one', 'two', 'three',
					'two', 'two', 'one', 'three'],'C' : np.random.randn(8),'D' : np.random.randn(8)})
	# grouping and then applying a function sum to the result groups
	df.groupby('A').sum()  # 通过A分组，然后进行各分组求和
	df.groupby(['A','B']).sum()

# reshaping 相当于R中的reshape2 melt dcast
	tuples = list(zip(*[['bar', 'bar', 'baz', 'baz','foo', 'foo', 'qux', 'qux'],['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
	index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
	df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
	df2=df[:4]
	stacked=df2.stack()    # 相当于R中的dcast
	stacked.unstack()      # 与stack相反
	stacked.unstack(1)     # 1,0表示按照不同的行列进行转换
	stacked.unstack(0)

# Pivot Tables
	df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
         'B' : ['A', 'B', 'C'] * 4,'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
         'D' : np.random.randn(12),'E' : np.random.randn(12)})
	pd.pivot_table(df,values='D',index=['A','B'],columns=['C'])

# time series
	rng=pd.date_range('1/1/2012',periods=100,frq='s')
	ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
	rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
	ts = pd.Series(np.random.randn(len(rng)), rng)
	ts_utc=ts.tz_localize('UTC')
	ts_utc.tz_convert('US/Eastern')
	rng = pd.date_range('1/1/2012', periods=5, freq='M')
	ts = pd.Series(np.random.randn(len(rng)), index=rng)
	ps=ts.to_period()
	ps.to_timestamp()

# getting data in/out
	df.to_csv('foo.csv')   # 保存成csv文件
	pd.read_csv('foo.csv')   # 读取csv文件
	# HDF5
	df.to_hdf('foo.h5','df')
	df.read_hdf('foo.h5','df')
	# Excel
	df.to_excel('foo.xlsx',sheet_name='Sheet1')
	pd.read_excel('foo.xlsx','Sheet1',index_col=None,na.values=['NA'])
