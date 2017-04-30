# -*- coding: utf-8 -*-
# 创建字符集[]  分清[cr][23]与r2d2|c3po之间的差别

import re
m = re.match('[cr][23][dp][o2]','c3po')    # 匹配 c3po
if m is not None:print(m.group())

m = re.match('r2d2|c3po','c2do')    # 不匹配c2do
if m is not None:print(m.group())

# 正则表达式最为常见的情况包括特殊字符的使用、正则表达式模式的重复出现，以及使用圆括号对匹配模式的各部分进行分组和提取操作
patt = '\w+@(\w+\.)?\w+\.com'
print(re.match(patt,'nobody@xxx.com').group())
print(re.match(patt,'nobody@www.xxx.com').group())

patt = '\w+@(\w+\.)*\w+\.com'    # 对于括号中的字符进行多个匹配
print(re.match(patt,'nobody@www.xxx.yyy.zzz.com').group())

m = re.match('\w\w\w-\d\d\d','abc-123')
print(m.group())

m = re.match('(\w\w\w)-(\d\d\d)','abc-123')
print(m.group())      # 完整匹配
print(m.group(1))     # 子组1
print(m.group(2))     # 子组2
print(m.groups())     # 全部子组

# groups返回所有匹配形式的所有子组的元组
m = re.match('(ab)','ab')
print(m.group())
print(m.group(1))
print(m.groups())

m = re.match('(a(b))','ab')
print(m.group(),m.group(1),m.group(2),m.groups())

# 匹配字符串的起始和结尾以及单词的边界
# 该操作更多的用于搜索而不是匹配，因为match()总是从字符串开始位置进行匹配
m = re.search('^The','The end.')     #　匹配
print(m.group())
m = re.search('^The','end.The')
# print(m.group())     #　不匹配

'''
the              任何包含the的字符串
\bthe            任何以the开始的字符串
\bthe\b          仅仅匹配单词the
\Bthe            任何包含但并不以the作为起始的字符串
'''

m = re.search(r'\bthe','bite the dog')   #　在边界
print(m.group())

m = re.search(r'\bthe','bitethe dog')   #　有边界
if m is not None:print(m.group())

m = re.search(r'\Bthe','bitethe dog')
if m is not None:print(m.group())
