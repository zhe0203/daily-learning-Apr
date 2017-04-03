import numpy as np
import pandas as pd

## 计算阶乘数据
def fun(x):
    if x==1:
        return(1)
    else:
        return(x*fun(x-1))
if __name__=="__main__":
    print(fun(5))

## 计算pi的值
pd.set_option('display.max_rows', 5)  # 将数据显示为5行
x=pd.Series(np.random.rand(10000))
y=pd.Series(np.random.rand(10000))
df=pd.DataFrame({'x':x,'y':y})
df1=pd.DataFrame({'x1':df['x'].apply(lambda x:x**2),
                  'y1':df['y'].apply(lambda y:y**2)})
df1['z1']=df1.apply(sum,axis=1)
df1['z2']=np.where(df1['z1']<=1,1,0)
# print(df1.apply(sum)['z2']*4/10000)
