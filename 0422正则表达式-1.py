# -*- coding: utf-8 -*-
import re

# 特殊符号和字符
'''
literal      匹配文本字符串的字面值literal
re1|re2      匹配正则表达式re1或者re2    foo|bar
.            匹配任何字符串(除了\n之外)  b.b
^            匹配字符串起始部分          ^Dear
$            匹配字符串终止部分          /bin/*sh$
*            匹配0次或者多次前面出现的正则表达式      [A-Za-z0-9]*
+            匹配1次或者多次前面出现的正则表达式      [a-z]+\.com
?            匹配0次或者1次前面出面的正则表达式       foo?
{N}          匹配N次前面出现的正则表达式              [0-9]{3}
{M,N}        匹配M-N次前面出现的正则表达式            [0-9]{5,9}
[...]        匹配来自字符集的任意单一字符             [aeiou]
[..x-y..]    匹配x-y范围中的任意单一字符              [0-9]  [r-u][env-y][us]
[^...]       不匹配此字符集中出现的任何一个字符        [^aeiou]
(*|+|?|{})?  用于匹配上面频繁出现/重复出现符号的非贪婪版本   .*?[a-z]
(...)        匹配封闭的正则表达式，然后另存为子组      ([0-9]{3})?  f(oo|u)bar
\d           匹配十进制的数字  \D与此相反
\w           匹配任何字符数字字符   [A-Za-z0-9_]
\s           匹配任何空格字符[\n\t\r\v\f]      of\sthe
\b           匹配任何单词边界       \bthe\b
\c           逐字匹配任何特殊字符c   \.  \\, \*
\            转义字符                \*  匹配*号
'''
# 想要匹配以美元结尾的字符串  .*\$$
# 对于?匹配的是0次或者1次，如果其跟在{}后面，意思是要求正则表达式引擎匹配尽可能少的次数
# 成为贪婪模式，?要求正则表达式去贪婪模式，就是在当前的正则表达式中尽可能少的匹配字符,留下尽可能多的字符给予后面的匹配模式

# 使用圆括号指定分组   -对正则表达式进行分组  -匹配子组
'''
(Mr?s?\.)?[A-Z][a-z]*[A-Za-z-]+
主要是提取所匹配的模式
可以实现匹配某个字符串以及丢弃不匹配的字符串，但有些时候我们可能对之前匹配成功的字符串感兴趣
能否提取任何已经成功匹配的特定字符串或者子字符串
如果为两个字模式加上圆括号  (\w+)-(\d+) 然后就能分别访问每一个匹配子组
'''
