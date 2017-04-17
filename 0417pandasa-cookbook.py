import pandas as pd
import numpy as np
import functools

# idioms
if __name__=='__main__':
	df = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]})
	# an if-then on one cloumn
	df.ix[df.AAA>=5,'BBB']=-1;df
	# 对于多个变量进行赋值
	df.ix[df.AAA>=5,['BBB','CCC']]=555;df   # 此处使用loc亦可以
	df.loc[df.AAA>=5,['BBB','CCC']]=555;df
	df.ix[df.AAA<5,['BBB','CCC']]=2000;df
	df_mask = pd.DataFrame({'AAA' : [True] * 4, 'BBB' : [False] * 4,'CCC' : [True,False] * 2})
	df.where(df_mask,-1000)  # df_mask中为True的，都是-1000
	# if-then-else using
	df = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]})
	df['logic']=np.where(df['AAA']>5,'high','low')  # 将AAA列大于5值赋值给high小于5赋值给low

# spliting
	df = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-5]})

# building criteria
	df = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-5]})
	newseries=df.loc[(df['BBB']<25)&(df['CCC']>=-40),'AAA']  # 多条件取AAA值
	df.loc[(df['BBB'] > 25) | (df['CCC'] >= 75), 'AAA'] = 0.1  # 多条件赋值
	# 使用排序函数 argsort
	df.ix[(df.CCC-43).abs().argsort()]   # argsort返回的是从大到小的索引序号
	# using a binary operators
	crit1=df.AAA<=5.5
	crit2=df.BBB==10
	crit3=df.CCC>-40
	allcrit=crit1 & crit2 & crit3
	critlist=[crit1,crit2,crit3]
	allcrit=functools.reduce(lambda x,y: x & y,critlist)
	df[allcrit]

# selection
	df[(df.AAA<=6) & (df.index.isin([0,2,4]))] # 同时使用行名称和值
	df.loc['bar','kar']
	df.ix[0:3] #Same as .iloc[0:3]
	df.ix['bar':'kar'] #Same as 
	df2 = pd.DataFrame(data=data,index=[1,2,3,4]); #Note index starts at 1.
	df2.iloc[1:3] #Position-oriented
	df2.loc[1:3] #Label-oriented
	df2.ix[1:3] #General, will mimic loc (label-oriented)
	df2.ix[0:3] #General, will mimic iloc (position-oriented), as loc[0:3]
	# 使用 ~  表示相反的结果
	df[~((df.AAA<=6) & (df.index.isin([0,2,4])))]  # 与不带~结果相反

# panels
	rng = pd.date_range('1/1/2013',periods=100,freq='D')
	data = np.random.randn(100, 4)
	cols = ['A','B','C','D']
	df1, df2, df3 = pd.DataFrame(data, rng, cols), pd.DataFrame(data, rng, cols), pd.DataFrame(data, rng, cols)
	pf = pd.Panel({'df1':df1,'df2':df2,'df3':df3});pf
	pf=pf.transpose(2,0,1)
	pf.loc[:,:,'F'] = pd.DataFrame(data, rng, cols);pf

# 创建新列，使用 applymap
	 df = pd.DataFrame({'AAA' : [1,2,1,3], 'BBB' : [1,1,2,2], 'CCC' : [2,1,3,1]})
	 source_cols=df.columns
	 new_cols=[str(x)+'_cat' for x in source_cols]
	 df[new_cols]=df[source_cols].applymap(categories.get)  # 添加新的3列
	 df[new_cols]=df[source_cols].applymap(lambda x:'%.2f' % x)  # applymap对于每一列都使用函数计算
	 # 重要的一点
	 df=pd.DataFrame({'AAA':[1,1,1,2,2,2,3,3],'BBB':[2,1,3,4,5,1,2,3]})
	 df.loc[df.groupby('AAA')['BBB'].idxmin()]   #idxmin用来返回分组后的每一组最小值索引位置
	 df.groupby('AAA')['BBB'].min()    # 返回分组后每一组的最小值
	 df.sort_values(by="BBB").groupby("AAA", as_index=False).first()
	 # 排序后，在分组，返回第一个值，即为最小值 as_index=False设置返回值不作为行名称的索引

# multindxing
	df.set_index('row')  # 将数据中的某列值，变换成行名称索引
	df = df.stack(0).reset_index(1)   # 结合使用 melt dcast

# slicing
	coords=[('AA','one'),('AA','six'),('BB','one'),('BB','two'),('BB','six')]
	index=pd.MultiIndex.from_tuples(coords)
	df=pd.DataFrame([11,22,33,44,55],index,columns=['mydata'])
	df.xs('BB',level=0,axis=0)  # 选取了BB的所有数据
	df.xs('six',level=1,axis=0)
	All = slice(None)
	df.loc[(All,'Math'),All]

# sorting
	df.sort_values(by=('Labs','II'),ascending=False)

# missing data
	df = pd.DataFrame(np.random.randn(6,1), index=pd.date_range('2013-08-01', periods=6, freq='B'), columns=list('A'))
	df.ix[3,'A']=np.nan
	df.reindex(df.index[::-1]).ffill()  # df.index[::-1]将数组倒排序

# grouping
	df = pd.DataFrame({'animal': 'cat dog cat fish dog cat cat'.split(),'size': list('SSMMMLL'),'weight': [8, 10, 11, 1, 20, 12, 12],'adult' : [False] * 5 + [True] * 2}); df
	df.groupby('animal').apply(lambda subf: subf['size'][subf['weight'].idxmax()])
	gb=df.groupby(['animal'])
	gb.get_group('cat')   # 返回cat分组的结果
	# expanding apply
	S=pd.Series([i/100.0 for i in range(1,11)])
	def CumRet(x,y):
		return(x*(1+y))
	def Red(x):
		return(functools.reduce(CumRet,x,1.0))
	S.expanding().apply(Red)

	grades = [48,99,75,80,42,80,72,68,36,78]
	df = pd.DataFrame( {'ID': ["x%d" % r for r in range(10)],
   		'Gender' : ['F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'M'],
   		'ExamYear': ['2007','2007','2007','2008','2008','2008','2008','2009','2009','2009'],
 		'Class': ['algebra', 'stats', 'bio', 'algebra', 'algebra', 'stats', 'stats', 'algebra', 'bio', 'bio'],
  		'Participated': ['yes','yes','yes','yes','no','yes','yes','yes','yes','yes'],
  	 	'Passed': ['yes' if x > 50 else 'no' for x in grades],
   		'Employed': [True,True,True,False,False,False,False,True,True,False],'Grade': grades})
   	#    一次使用多个聚合函数时，用agg方法
   	df.groupby('ExamYear').agg({'participated':lambda x:x.value_counts()['yes'],
   								'passed':lambda x:sum(x=='yes'),
   								'employed':lambda x:sum(x),
   								'grade':lambda x:sum(x)/len(x)})
