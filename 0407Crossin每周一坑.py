# _*_ coding: utf-8 _*_

'''
乒乓序列从1开始计数，并且始终向上或向下计数。
在元素k处，如果k是7的倍数或包含数字7，方向将切换。
乒乓序列的前30个元素如下所示，方向交换在第7,14和17，21，第27和28个元素：
1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6
定义一个函数 pingpong ，传入一个正整数参数 n ，返回第 n 个乒乓数
'''

def pingpong(n,k):
    if isinstance(n,int) and n >= 1:
        result = []
        s = 0
        m = [i for i in range(1,n+1) if i % k == 0 or str(k) in str(i)]
        m1 , m2 = m.copy(),m.copy()
        m1.insert(0,0)
        m2.append(n)

        for i,j in enumerate(map(lambda x, y: y - x, m1, m2)):
            if i % 2 == 0:
                for l in range(j):
                    s += 1
                    result.append(s)
            else:
                for l in range(j):
                    s -= 1
                    result.append(s)
        print(result)
        print(result.pop())
    else:
        print('input error')

if __name__ == '__main__':
    pingpong(30,7)
