from time import time

# 数据库要存varchar 时间戳 当唯一索引
def getTimeInteger():
    res =str(int(time()))
    print("打印时间戳",res)
    return res
