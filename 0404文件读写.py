# 数据的读写
w  # 以写方式打开
a  # 以追加模式打开
r+ # 以读写模式打开
w+ # 以读写模式打开
a+ # 以读写模式打开
rb # 以二进制读模式打开
wb # 以二进制写模式打开
ab # 以二进制追加模式打开
rb+ # 以二进制读写模式打开
wb+ # 以二进制读写模式打开
ab+ # 以二进制读写模式打开

os.getcwd()    # 返回当前python脚本的目录路径
os.listdir()   # 返回指定目录下的所有文件和目录名
os.remove()  # 用来删除一个文件
os.path.isfile()   # 判断是否为文件
os.path.isdir()   # 判断是否为目录
os.listdir(dirname)   # 列出dirname下的目录和目录
os.psth.getsize()   # 返回文件的大小

### 读文件
f = open('test.txt','r')  # r表示读，这样就成功打开了一个文件
f.read()   # 成功打开，使用read()方法可以一次读取文件的全部内容
f.close()  # 调用close()方法关闭文件
### 由于读写都有可能产生ioerror，一旦出错，后面的f.close()就不会被调用，为了保证无论是否出错都能正确地关闭文件
try:
	f = open('test.txt','r')
	print(f.read())
finally:
	if f:
		f.close()
### 以上更为简单的代码是
with open('test.txt','r') as f:
	print(f.read())
read(size)   # 防止数据量大，可以每次最多读取size个字节的内容
readline()   # 每次读取一行内容
f.readline()   # 读取第一行信息
f.readline()   # 再次执行读取下一行的信息
read = open(result)
line = read.readline()
while line:
	print(line)
	line = read.readline()  #如果没有这行会造成死循环  
read.close()

readlines()  # 一次读取所有内容并按行返回list 
for line in f.readlines():
	print(line.strip())   # 把末尾的'\n'删掉

### 读取二进制文件，比如图片、视频等，需要使用'rb'
f = open('test.jpg','rb')
f.read()    # 返回十六进制的字节

### 字符编码
f = open('text.txt','r',encoding='gbk')
f.read()
f = open('test.txt','r',encoding='gbk',errors=''ignore) # 忽略编码错误的处理方式

### 写文件 w表示写文件 wb表示写二进制文件
f = open('test.txt','w')
f.write('hello world!')
f.close()
# 请给open()函数传入encoding参数，将字符串自动转换成指定编码
with open('test.txt','w') as f:
	f.write('hello world!')

### 可以定义读入文件的函数
def loaddataset():
	datamat=[]
	labelmat=[]
	fr = open('test.txt')
	for line in fr.realines():
		linearr = line.strip().split()
		datamat.append([1.0,float(linearr[0]),float(linearr[1])])
		labelmat.append([int(linearr[2])])
	return(datamat,labelmat)

# StringIO 表示在内存中读写str 和BytesIO
# 很多时候，数据读写不一定是文件，也可以在内存中读写
from io import StringIO
f = StringIO()   # 首先创建一个stringIO
f.write('hello')   # 5
f.write(' ')       # 1
f.write('world!')  # 6
## 使用getvalue用于获得写入后的str
print(f.getvalue())   # hello world! 

### 读取stringis的方式
f = StringIO('hello!\nhi!\ngoodbye!')
while True:
	s = f.readline()   # 读取一行
	if s == '':
		break
	print(s.strip())
### 若果要操作二进制使用BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()

# 操作文件和目录
import os
os.name   　　　　　# 返回操作系统的类型
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
os.environ     # 返回操作系统的环境变量
os.environ.get('PATH')        # 获取某个环境变量

## 操作文件和目录
os.path.abspath('.')  # 查看当前目录的绝对路径
os.path.join('/Users/michael', 'testdir') # # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.mkdir()         # 然后创建一个目录:
os.rmdir('/Users/michael/testdir')      # 删掉一个目录:

os.path.split('/Users/michael/testdir/file.txt')   # 拆分路劲
('/Users/michael/testdir', 'file.txt')

os.path.splitext('/path/to/file.txt')   # 可以直接让你得到文件扩展名
('/path/to/file', '.txt')

# 对文件重命名
os.rename('test.txt','test.py')
os.remove('test.py')     # 删掉文件

# 列出当前目录下所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]

[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

# json
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)       # 把dict变成一个json对象

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)   # 转换成python字典形式
