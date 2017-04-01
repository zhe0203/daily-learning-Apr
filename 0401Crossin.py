# -*- coding: utf-8 -*-
# 多重囚徒困境，求进行 N 次博弈下，使用不同的策略，囚犯各自的获刑年限,目前有三种策略：
# 1、nice：不管对方揭发还是沉默，都保持沉默
# 2、rat：不管对方沉默还是揭发，都选择揭发
# 3、tit_for_tat：第一轮选择沉默，第二轮开始如果对方上一轮沉默，本轮就选择沉默，对方上一轮揭发，本轮也选择揭发。
years = {'nice-nice':[1,1],'nice-rat':[5,0],'rat-nice':[0,5],'rat-rat':[2,2]}
def prisoner_delimma(N,strategy1,strategy2):
    person_1 = ['nice']
    person_2 = ['nice']
    if strategy1 == 'tit_for_tat' and strategy2 != 'tit_for_tat':
        person_1.extend(['nice' if strategy2 == 'nice' else 'rat'] * (N-1))
        person_2 = [strategy2] * N
    elif strategy1 != 'tit_for_tat' and strategy2 == 'tit_for_tat':
        person_1 = [strategy1] * N
        person_2.extend(['nice' if strategy1 == 'nice' else 'rat'] * (N-1))
    elif strategy1 == 'tit_for_tat' and strategy2 == 'tit_for_tat':
        person_1 = ['nice'] * N
        person_2 = ['nice'] * N
    else:
        person_1 = [strategy1] * N
        person_2 = [strategy2] * N
    result = ['-'.join([person_1[i],person_2[i]]) for i in range(N)]
    years_1 = sum([years.get(x)[0] for x in result])
    years_2 = sum([years.get(x)[1] for x in result])
    print(years_1,years_2)

if __name__=="__main__":
    prisoner_delimma(4,'nice','nice')
    prisoner_delimma(5,'rat','rat')
    prisoner_delimma(6,'nice','rat')
    prisoner_delimma(4,'rat','tit_for_tat')
    prisoner_delimma(7,'tit_for_tat','tit_for_tat')
