# -*- coding: utf-8 -*-
import re
'''
compile(pattern,flags=0)     使用任何可选的标记来编译正则表达式的模式，然后返回一个正则表达式对象
match(pattern,string,flags=0)  使用带有可选标记的正则表达式的模式来匹配字符串，匹配成功返回匹配对象，匹配失败，返回None
search(pattern,string,flags=0)  使用可选标记搜索字符串中第一次出现的正则表达式模式，成功返回匹配值，失败返回None
findall(pettern,string)  查找字符串所有出现的正则表达式模式，并返回匹配列表
finditer(pattern,string)  与findall相同，但返回的是一个迭代器，对于每一次匹配，迭代器都返回一个匹配对象
split(pattern,string)  根据正则表达式的模式分隔符，split函数将字符串分割为列表

sub(pattern,repl,string,count=0)  使用repl替换所有正则表达式的模式在字符串中出现的位置,count指定替换的个数
subn(pattern,repl,string)   返回sub替换操作的数目
purge()   消除隐士编译的正则表达式模式

group(num=0)   返回整个匹配对象，或者编号为num的特定子组
groups()   返回一个包含所有匹配子组的元组
groupdict()   返回一个包含所有匹配的命名子组的字典，所有的子组名称作为字典的键

# 常用的模块属性
re.I  re.IGNORECASE    不区分大小写的匹配
re.L   re.LOCALE      根据所使用的本地语言环境通过\w,\W,\b,\s,\S实现匹配
re.M    ^和$分别匹配目标字符串中行的起始和结束，而不是严格匹配整个字符串本身的起始和结尾
'''

# 使用match()方法匹配字符串
m = re.match('foo','foo')     # 模式匹配字符串
if m is not None:
    print(m.group())
print(re.match('foo','seafoo'))    # 从开始位置进行匹配无效，这时候可以使用搜索的功能search

print(re.search('foo','seafoo').group())

m = re.findall('foo','foo on foo')
print(m)

# 匹配多个字符串
bt = 'bat|bet|bit'     # 正则表达式bat\bet\bit
m = re.match(bt,'bat')   # bat是一个匹配
if m is not None:print(m.group())
print(re.match(bt,'blt'))     # 对于blt没有匹配选项

m = re.match(bt,'he bit me!')   # 不能匹配字符串
if m is not None:print(m.group())

# 通过搜搜查找bit
m = re.search(bt,'he bit me!')
if m is not None:print(m.group())

# 匹配单个字符串
anyend = '.end'
m = re.match(anyend,'bend')      # 点号匹配d
if m is not None:print(m.group())

m = re.match(anyend,'end')     # 不匹配任何字符
m = re.match(anyend,'\nend')   # 除了\n之外的任何字符

m = re.search('.end','the end.')   # 在搜索中匹配空格
if m is not None:print(m.group())

patt314 = '3.14'
pi_patt = '3\.14'
m = re.match(pi_patt,'3.14')    # 精确匹配
if m is not None:print(m.group())

m = re.match(patt314,'3014')   # 点号匹配0
if m is not None:print(m.group())

m = re.match(patt314,'3.14')
if m is not None:print(m.group())
