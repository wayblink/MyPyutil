
#coding: utf-8

import datetime

now = datetime.datetime.strptime("20180304", "%Y%m%d")
# 现在的时间
# now = datetime.datetime.now()
# 递增的时间
delta = datetime.timedelta(days=1)
# 一天后的时间
enddate = datetime.datetime.now()+delta
# 一天后的时间转换成字符串
endnow = str(enddate.strftime('%Y%m%d'))

#可以进行时间判断
print enddate > now
