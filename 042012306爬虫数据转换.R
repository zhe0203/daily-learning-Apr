library(tidyr)
library(dplyr)
setwd("C:/Users/jk/Desktop/全部数据")
a = list.files("C:/Users/jk/Desktop/全部数据") 

mydata = data.frame()    # 建立空的数据框将数据进行整合

for (i in 1:21){
  df = read.csv(a[i],header= T)     # 读取每一个csv数据
  df = df %>% gather(时间, 票数,-出发地,-目的地) 
  df = df %>% mutate(查询时间 = rep(strsplit(a[i],'\\.')[[1]][1],nrow(df)))
  mydata = rbind(mydata,df)
}

# 数据结果的排序，以便查看数据的类型
mydata = mydata %>% arrange(时间,出发地,目的地)

# 将时间进行处理成标准格式
# 定义一个将年月日时间转换为标准时间格式的函数
get_date = function(x){
  a1 = gsub('.?([0-9]+)月[0-9]+日','\\1',x)  # 返回第二个括号内的数据
  a2 = gsub('.?[0-9]+月([0-9]+)日','\\1',x)
  a1 = ifelse(nchar(a1) == 1,paste0(0,a1),a1)
  a2 = ifelse(nchar(a2) == 1,paste0(0,a2),a2)
  return(paste0(2017,a1,a2))
}
# 将中文日期转换为标准形式
mydata['时间'] = sapply(mydata['时间'],get_date)
mydata['查询时间'] = sapply(mydata['查询时间'],get_date)
# 将字符串转换为时间格式
mydata['时间'] = sapply(mydata['时间'],function(x) strptime(x,'%Y%m%d'))
mydata['查询时间'] = sapply(mydata['查询时间'],function(x) strptime(x,"%Y%m%d"))
# 计算间隔时间
mydata['间隔时间']  = (mydata['时间']-mydata['查询时间'])/3600/24

# 下面进行变换
mydata_1 = mydata[,-5]
# write.csv(mydata_1,'123.csv')
mydata_1 = mydata_1 %>% spread(间隔时间,票数)
write.csv(mydata_1,'123.csv')
