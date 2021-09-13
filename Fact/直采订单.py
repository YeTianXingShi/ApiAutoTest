import json
from time import sleep

from Easy.EasyRequest import EasyRequest

test_a = EasyRequest(user='80996805', application="order-fresh", env="test")

# 创建直采单 获取直采单号
a = test_a.start(rid=5)
b = json.loads(a)
c1 = b['result']['applyOrderNo']

print("等待拆单中 预计30S")
sleep(50)

# 去订单明细跟踪查拆单号
test_b = EasyRequest(user='80663835', application="ordercenter-view", env="test")
payload2 = '{"page": 1, "size": 200, "menuType": 1, "applyOrderNos": ["Z109130099"]}'
payload2 = json.loads(payload2)
payload2['applyOrderNos'] = [c1]
payload2 = json.dumps(payload2)
a = test_b.start(rid=6, payload=payload2)
b = json.loads(a)
c2 = b['page']['result'][0]['splitOrderNo']
print("拆单号为" + c2)
