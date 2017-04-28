'''
设定一个长度为N的数字串，将其分为两部分，找出一个切分位置，使两部分的乘积值最大，并返回最大值
'''
def product(num):
    print(max([int(str(num)[0:i])*int(str(num)[i:]) for i in range(1,len(str(num)))]))

product(123456)

'''
输入数字串可以重新打乱排列，比如输入123，打乱之后会有132,213,312,321等情况，其他条件不变，求最大值
'''
from itertools import permutations
def product_2(num):
    print(max([int(''.join(i)[0:j]) * int(''.join(i)[j:]) for i in permutations(str(num)) for j in range(1, len(''.join(i))) ]))

product_2(1234)
