# -*- coding: utf-8 -*-
# http://python.jobbole.com/87581/

s = []       # 创建一个栈
s.append(1)  # 往栈内添加一个元素
s.pop()      # 在栈内删除一个元素
not s        # 判断是否为空栈
len(s)       # 获取栈内元素的数量
# s[-1]        # 获取栈顶的元素


# 括号匹配
'''
假如表达式中允许包含三中括号()、[]、{}，其嵌套顺序是任意的，例如：
正确的格式   {()[()]},[{({})}]
错误的格式   [(]),[()),(()}
编写一个函数，判断一个表达式字符串，括号匹配是否正确
'''
## 思路
'''
1、创建一个空栈，用来存储尚未找到的左括号
2、遍历字符串，遇到左括号则压栈，遇到右括号则出栈一个左括号进行匹配
3、在第二步骤过程中，如果空栈情况下遇到右括号，说明缺少左括号，不匹配
4、在第二步骤遍历结束时，栈不为空，说明缺少右括号，不匹配
'''

left = {'(','[','{'}
right = {')',']','}'}
def match(expr):
    '''
    :param expr: 传过来的字符串
    :return:  返回是否是正确的
    '''
    stack = []
    for brackets in expr:
        if brackets in left:    # 如果当前字符在左括号内
            stack.append(brackets)   # 把当前左括号入栈
        elif brackets in right:      # 如果是右括号
            if not stack or not 1 <= ord(brackets) - ord(stack[-1]) <= 2:
                # 如果当前栈为空，()]
                # 如果右括号前去左括号的值不是小于等于2大于等于1
                return False
            stack.pop()    # 配对成功则将配对成功的删除，以便进行下面的配对
    return not stack
result = match('[(){()}]')
print(result)

# 例子2 迷宫问题
'''
用一个二维数组表示一个简单的迷宫，用0表示通路，用1表示阻断，
老鼠在每个点上可以移动相邻的东南西北四个点，
设计一个算法，模拟老鼠走迷宫，找到从入口到出口的一条路径。
'''
## 思路
'''
1、用一个栈来记录老鼠从入口到出口的路径
2、走到某点后，将该点左边压栈，并把该点值设为1，表示走过了
3、从临近的四个点钟可到达的点钟任意取一个，走到该点
4、如果在到达某店后临近的4个点都不走，说明已经走入死胡同，此时退栈，返回第一步尝试其他点
5、反复执行第二、三、四步骤知道找出出口
'''

def initMaze():
    maze = [[0] * 7 for _ in range(5 + 2)]
    walls = [      # 记录了墙的位置
        (1,3),
        (2,1),(2,5),
        (3,3),(3,4),
        (4,2),
        (5,4)
    ]
    for i in range(7):   # 把迷宫的四周设置成墙
        maze[i][0] = maze[i][-1] = 1
        maze[0][i] = maze[-1][i] = 1
    for i , j in walls:  # 把所有墙的点设置为1
        maze[i][j] = 1
    return maze
'''
[1,1,1,1,1,1,1]
[1,0,0,1,0,0,1]
[1,1,0,0,0,1,1]
[1,0,0,1,1,0,1]
[1,0,1,0,0,0,1]
[1,0,0,0,1,0,1]
[1,1,1,1,1,1,1]
'''

def path(maze,start,end):
    i , j = start   # 分解起始点坐标
    ei , ej = end   # 分解结束点的坐标
    stack = [(i , j)]
    maze[i][j] = 1   # 走过的路设置为1
    while stack:
        i , j = stack[-1]   # 获取当前老鼠所站的位置点
        if (i,j) == (ei,ej):
            break
        for di , dj in [(0,-1),(0,1),(-1,0),(1,0)]:
            if maze[i + di][j + dj] == 0:
                maze[i + di][j + dj] == 1
                stack.append((i+di,j+dj))
                break
        else:
            stack.pop()
    return stack
Maze = initMaze()
result = path(maze=Maze,start=(1,1),end=(5,5))
print(result)

# 后缀表达式求值
'''
计算一个表达式时，编译器通常使用后缀表达式，这种表达式不需要括号：
中缀表达式	                    后缀表达式
2 + 3 * 4	                    2 3 4 * +
( 1 + 2 ) * ( 6 / 3 ) + 2	    1 2 + 6 3 / * 2 +
18 / ( 3 * ( 1 + 2 ) )	        18 3 1 2 + * /
'''
## 思路
'''
1、建立一个栈来存储待计算的操作数
2、遍历字符串，遇到操作数则压入栈中，遇到操作符号则出栈操作数（n次）
   进行相应的计算，计算结果是新的操作数压回栈中，待计算
3、按上述过程，遍历完整个表达式，栈中只剩下最终结果
'''

operators = {
    '+': lambda op1,op2: op1 + op2,
    '-': lambda op1,op2: op1 - op2,
    '*': lambda op1,op2: op1 * op2,
    '/': lambda op1,op2: op1 / op2,
}
def evalPostfix(e):
    tokens = e.split()
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in operators.keys():
            f = operators[token]
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f(op1,op2))
    return stack.pop()
result = evalPostfix('2 3 4 * +')
print(result)

# 背包问题
'''
有一个背包能装10kg的物品，现在有6件物品分别为：
物品名称	  重量
物品0	  1kg
物品1	  8kg
物品2	  4kg
物品3	  3kg
物品4	  5kg
物品5	  2kg
编写找出所有能将背包装满的解，如物品1+物品5
'''
def knapsack(t,w):
    n = len(w)
    stack = []
    k = 0
    while stack or k < n:
        while t > 0 and k < n:
            if t >= w[k]:
                stack.append(k)
                t -= w[k]
            k += 1
        if t == 0:
            print(stack)
        k = stack.pop()
        t += w[k]
        k += 1
print(knapsack(10,[1,8,4,3,5,2]))
