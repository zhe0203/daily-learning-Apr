# -*- coding: utf-8 -*-

def race(qiwang,tianji):
    tianji.insert(3, tianji.pop(0))
    print(sorted(zip(qiwang,tianji),reverse=True))

if __name__ == '__main__':
    race([3,6,9],[2,5,8])

# 附加题1  未解决，坐等答案
'''
如果你是某公子手下的谋士，已知同级别中己方的马优于田忌的马，事先不知道对方派遣顺序，
不过可以根据上一轮对方的派出的马匹制定本轮的选择，为公子制定一种派遣策略，使赢得比赛的几率最大。
'''
import random
import numpy as np
g = [3,6,9]
t = [2,5,8]
'''
田忌所有的可能:[('2', '5', '8'), ('2', '8', '5'),
               ('5', '2', '8'), ('5', '8', '2'),
               ('8', '2', '5'), ('8', '5', '2')]
公子所有的可能:[('3', '6', '9'), ('3', '9', '6'),
               ('6', '3', '9'), ('6', '9', '3'),
               ('9', '3', '6'), ('9', '6', '3')]
'''
# 田忌的策略
def tianji_s():
    return random.shuffle(t)

# # 公子的策略，在未知田忌首个出场的情况下，无论公子怎么选择出场马匹，其赢得比赛的概率均相同
def gongzi_s():
    # tianji_s()      # 随机田忌出场的顺序
    # gongzi_game = []
    # gongzi_game.append(random.sample(g,1))   # 随机选择公子出场的马匹
    return random.shuffle(g)



    # return gongzi_game
#
# # 计算赢得比赛的概率
gongzi_win = 0
for i in range(1000):
    tianji_s(),gongzi_s()
    if sum(np.where(np.array(g)-np.array(t) > 0, 1, 0)) >= 2:
        gongzi_win += 1
print('公子赢得比赛的概率为:',gongzi_win / 1000)


from itertools import permutations
# 排列组合暴力求解
# 田忌出马所有可能的组合
gongzi_game = list(permutations('369', 3))
tianji_game = list(permutations('258', 3))
# print(gongzi_game)
# print(tianji_game)

# 对于田忌，无论他第一匹马出什么，计算公子应该出的应的最大的概率的马的序号
df = {}
for i in tianji_game:
    for j in gongzi_game:
        re = sum(np.where(np.array([int(x) for x in j])-np.array([int(y) for y in i]) > 0,1,0))
        # print({i[0]:j[0]},re)
        key = '-'.join([i[0],j[0]])
        if key not in df.keys():
            df[key] = re
        else:
            df[key] += re
# print(df)


# 附加题2
'''
现在将马分为优、上、中、下、劣五等，五局三胜，抽象为列表[2,4,6,8,10],[1,3,5,7,9]
其他条件不变，计算出田忌有多少种赢得比赛的可能
'''
from itertools import permutations
g = [2,4,6,8,10]
t = [1,3,5,7,9]
n = 0
for i in permutations(t, 5):
    for j in permutations(g, 5):
        if sum(np.where(np.array([int(x) for x in i])-np.array([int(y) for y in j]) > 0,1,0)) >= 3:
            n += 1
print(n)  # 3240
