# -*- coding: utf-8 -*-
# 结巴中文分词：做最好的Python中文分词组件

import jieba

# 分词
'''
jieba.cut 方法接受三个参数:需要分词的字符串，cut_all参数用来精致是否采用全模式;HMM参数用来控制是否使用HMM模型
jieba.cut_for_search 需要分词的字符串，是否使用HMM模型。该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细
待分词的字符串可以是unicode或者UTF-8字符串，GBK字符串，不建议直接输入GBK字符串，可能无法预料地错误解码成UTF-8
jieba.cut jieba.cut_for_search返回的是一个可迭代的genrator,可以使用for循环来获取分此后得到的每一个词语的unicode
jieba.lcut jieba.lcut_for_search直接返回list
jieba.Tokenizer(dictionary=DEFAULT_DICT)新建自定义分词器，可用于同时使用不同词典，jieba.ct为默认分词器
'''
seg_list = jieba.cut('我来到北京清华大学',cut_all=True)    # 全模式
print('/ '.join(seg_list))  # 我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学

seg_list = jieba.cut('我来到北京清华大学',cut_all=False)   # 精确模式
print("/ ".join(seg_list))  # 我/ 来到/ 北京/ 清华大学

seg_list = jieba.cut('他来到了网易杭研大厦')    # 默认是精确模式
print(', '.join(seg_list))  # 他, 来到, 了, 网易, 杭研, 大厦

seg_list = jieba.cut_for_search('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')    # 搜索引擎模式
print(', '.join(seg_list))  # 小明, 硕士, 毕业, 于, 中国, 科学, 学院, 科学院, 中国科学院, 计算, 计算所, ，, 后, 在, 日本, 京都, 大学, 日本京都大学, 深造

seg_list = jieba.cut('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')
print(', '.join(seg_list))

# 添加定义字典
'''
开发者可以指定自己的定义的字典，以便包含jieba词库里没有的词，虽然jieba有新词识别能力，但是自行添加新词可以保证更高的争取率
用法: jieba.load_userdict(file_name)   # file_name为文件类型对象或自定义词典的路径
词典格式和dict.txt一样，一个词占一行，每一行分三部分，词语，词频，词性，用空格隔开，顺序不可颠倒
词频省略时使用自动计算的能保证分出该词的词频
'''
import jieba.posseg as pseg
jieba.load_userdict('userdict.txt')
jieba.add_word('石墨烯')
jieba.add_word('凱特琳')
jieba.del_word('自定义词')

test_sent = (
"李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
"例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
"「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
)

words = jieba.cut(test_sent)
print('/'.join(words))

print('='*50)

result = pseg.cut(test_sent)
for w in result:
    print(w.word,'/',w.flag,',',end=' ')
print('\n' + '=' * 50)

terms = jieba.cut('easy_install is great')
print('/'.join(terms))
terms = jieba.cut('python 的正则表达式是好用的')
print('/'.join(terms))
print("="*40)
# test frequency tune
testlist = [('今天天气不错',('今天','天气')),
            ('如果放到post中将出错。',('中','将')),
            ('我们中出了一个叛徒',('中','出'))]
for sent,seg in testlist:
    print('/'.join(jieba.cut(sent,HMM=False)))
    word = ''.join(seg)
    print('%s Before: %s, After: %s' % (word, jieba.get_FREQ(word), jieba.suggest_freq(seg, True)))
    print('/'.join(jieba.cut(sent, HMM=False)))
    print("-" * 40)

# 调整词典
'''
使用add_word()和del_word()可在程序中动态修改词典
使用suggest_freq(segment,tune=True)可调节单个词语的词频，使其能被分出来
注意:自动计算的词频在使用HMM新词发现功能时可能无效
'''
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
jieba.suggest_freq(('中','将'),True)  # 利用调节词频使中、将都能被分出来
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
jieba.suggest_freq('台中', True)
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))

# 基于 TF-IDF 算法的关键词抽取
import jieba.analyse
'''
jieba.analyse.extract_tags
sentence 为提取的文本
topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
withWeight 为是否一并返回关键词权重值，默认值为 False
allowPOS 仅包括指定词性的词，默认值为空，即不筛选
jieba.analyse.TFIDF(idf_path=None) 新建 TFIDF 实例，idf_path 为 IDF 频率文件
'''
import jieba.analyse
import sys
from optparse import OptionParser
USAGE = "usage:    python extract_tags.py [file name] -k [top k]"
parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()

if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]
if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

content = open(file_name, 'rb').read()
tags = jieba.analyse.extract_tags(content, topK=topK)
print(",".join(tags))

# 词性标注
import jieba.posseg as pseg
words = pseg.cut("我爱北京天安门")
for word, flag in words:
    print('%s %s' % (word, flag))

# 并行分词
import sys
import time
sys.path.append("../../")
import jieba

jieba.enable_parallel()
url = sys.argv[1]
content = open(url,"rb").read()
t1 = time.time()
words = "/ ".join(jieba.cut(content))
t2 = time.time()
tm_cost = t2-t1
log_f = open("1.log","wb")
log_f.write(words.encode('utf-8'))
print('speed %s bytes/second' % (len(content)/tm_cost))

# 返回词语在原文的起止位置
result = jieba.tokenize(u'永和服装饰品有限公司')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))

result = jieba.tokenize(u'永和服装饰品有限公司', mode='search')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
