import time


# 返回时间戳
def get_time():
    a = time.time()
    b = int(a)
    return b


# 获取当前时间到秒
def get_date():
    a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return a
