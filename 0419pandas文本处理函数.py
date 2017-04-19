# Working with Text Data
import pandas as pd
import numpy as np

if __name__=='__main__':
	s=pd.Series(['A','B','C','Aaba','Baca',np.nan,'CABA','dog','cat'])
	s.str.lower()   # 转换成小写
	s.str.upper()   # 转换成大写
	s.str.len()     # 求每个字符串的长度

	idx=pd.Index([' jack','jill',' jesse ','frank'])
	idx.str.strip()    # 去除空格
	idx.str.lstrip()   # 去除左边的空格
	idx.str.rstrip()   # 去除右边的空格

	df=pd.DataFrame(np.random.randn(3,2),columns=[' column A ',' Column B '],index=range(3))
	df.columns.str.strip()    # 去除列名称中的空格
	df.columns.str.lstrip()   # 去除列名称中左边的空格
	df.columns.str.lower()    # 改成小写
	df.columns.str.strip().str.lower().str.replace(' ','_')  # 将未清除的空格，替换为_

# splitting and replace strings
	s2=pd.Series(['a_b_c','c_d_e',np.nan,'f_g_h'])
	s2.str.split('_')    # 按照 _ 进行分割数据
	s2.str.split('_').str.get(1)   # 返回第2列的数据
	s2.str.split('_').str[1]       # 返回第二列的数据
	s2.str.split('_',expand=True)  # 返回数据框
	s2.str.split('_',expand=True,n=1)  # 分割一个_
	s2.str.rsplit('_', expand=True, n=1)  # 从右边的数据开始分割

	s3=pd.Series(['A','B','C','Aaba','Baca','',np.nan,'CABA','dog','cat'])
	s3.str.replace('^.a|dao','XX-XX',case=False)

	dollars=pd.Series(['12','-$10','$10000'])
	dollars.str.replace('$', '')
	dollars.str.replace(r'-\$', '-')

# extracting substrings
	pd.Series(['a1','b2','c3']).str.extract('([ab])(\d)',expand=True)
	pd.Series(['abv1','bdf2','csdf3']).str.extract('([a-z]+)(\d)',expand=True)
	pd.Series(['a1', 'b2', '3']).str.extract('([ab]?)(\d)', expand=False) # ? 0次或者多次
	pd.Series(['a1','b2','c3']).str.extract('[ab]?(\d)',expand=True)

	s = pd.Series(["a1", "b2", "c3"], ["A11", "B22", "C33"])
	s.index.str.extract("(?P<letter>[a-zA-Z])", expand=True) # 使用？P<letter>对于列名称进行命名
	s.index.str.extract("(?P<letter>[a-zA-Z])(?P<digits>[0-9]+)",expand=True)

# testing for Strings that Match or Contain a Pattern
	pattern=r'[a-z][0-9]'
	pd.Series(['1','2','3a','3b','03c']).str.contains(pattern)
	s4 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
	s4.str.contains('A', na=False)

# Creating Indicator Variables
	s=pd.Series(['a','a|b',np.nan,'a|c'])
	s.str.get_dummies(sep='|')   # 产生稀疏矩阵
	s.str.repeat(3)  # 将a的每个值重复3次

# 其他
	str.startswith(pat, na=nan)   # 判断某个字符是否以某个字符开头
	str.endswith(pat, na=nan)     # 是否以某个字符结尾
	s = pd.Series(['a1', 'b2', 'c3'])
	s.str.extract('([ab])(\d)')
