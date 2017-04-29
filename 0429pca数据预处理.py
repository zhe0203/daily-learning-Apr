# -*- coding: utf-8 -*-
import pandas as pd
import os
os.chdir(r'C:\Users\jk\Desktop\2016年专业满意度统计')
for i in os.listdir():
    for j,k in pd.read_excel(i,sheetname=None,index_col=[0], header=[0]).items():
        df = pd.read_excel(i,sheetname=j,index_col=[0,1], header=[0])
        if len(df.iloc[0,:]) == 10:
            df = df.iloc[:,[0,1,3,5,7,9]]
        else:
            df = df
        df['得分'] = list(map(lambda x,y,z,k:x*10 + y*7 + z*5 + k*3,df.iloc[:,2],df.iloc[:,3],
                                                            df.iloc[:,4],df.iloc[:,5]))
        name = i.split('.')[0] + '_' + j + '.xlsx'
        df.to_excel(name)
