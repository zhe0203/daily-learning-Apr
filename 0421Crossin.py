# -*- coding: utf-8 -*-

import hashlib

# hashlib 模块
'''
hashlib模块支持的加密算法有md5、sha1、sha224 sha256 sha384 sha512
其中，md5等算法还提供了digest_size和block_size等属性，指示加密后文件的大小
对于其他的算法，只要将代码中替换md5即可
'''
# 以md5加密为例，有两种方法
## 1、追加模式
mm = hashlib.md5()                    # 创建一个md5对象
mm.update('Hello'.encode('utf-8'))    # 通过update方法加密文本
mm.update(' world!'.encode('utf-8'))   # 追加，这两句相当于mm.update('Hello world!'# )
print(mm.digest())                    # 输出加密后的二进制数据
print(mm.hexdigest())                 # 输出加密后的十六进制数据

## 2、一句话
### 如果不需要追加，只用加密一段文本，可用这种形式
print(hashlib.new('md5','Hello world!'.encode('utf-8')).digest())

# base64模块
## 这个模块提供的加密算法并不安全，但十分简单，有时候会用到
import base64
a = 'Hello world!'
b = base64.b64encode(a.encode(encoding='utf-8'))  # 加密
c = base64.b64decode(b) # 解密
print(b)
print(c)

'''
在 python 中有 hashlib 和 base64 两大加密模块，
将一串字符串先经过 hashlib.md5 加密，然后再经过 base64 加密，最后得到一串字符：
'NDRiMWZmMmVjZTk5MTFjMWI1MDNkYTY0MzZlYTAzMTA=\n'

在此给出 4 个选项

我们在一起吧
我选择原谅你
别说话，吻我
多喝热水
请各位大侦探们使用科学的方法算出我说的什么吧！
'''
# 首先利用base64进行解密
a = 'NDRiMWZmMmVjZTk5MTFjMWI1MDNkYTY0MzZlYTAzMTA=\n'
b = base64.b64decode(a)
print(b)
# 其次使用hashlib进行解密
result = ['我们在一起吧','我选择原谅你','别说话，吻我','多喝热水']
for i in result:
    print(hashlib.new('md5',i.encode('utf-8')).hexdigest())
    # if hashlib.new('md5',i.encode('utf-8')).hexdigest() == b:
    #     print(i)
