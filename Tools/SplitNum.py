# 根据申请单号拆单号查询
import json

from Easy.EasyRequest import EasyRequest


def find_split_no_fresh(apply_no):
    test_b = EasyRequest(user='80663835', application="ordercenter-view", env="test")
    payload2 = '{"page": 1, "size": 200, "menuType": 1, "applyOrderNos": ["Z109130099"]}'
    payload2 = json.loads(payload2)
    payload2['applyOrderNos'] = [apply_no]
    payload2 = json.dumps(payload2)
    a = test_b.start(rid=6, payload=payload2)
    b = json.loads(a)
    if not b['page']['result']:
        # print("没找到 待会再来")
        return 0
    else:
        if b['page']['result'][0]['splitOrderNo'] == "":
            # print("还没拆单完成")
            return 0
        else:
            c2 = b['page']['result'][0]['splitOrderNo']
            print("拆单号为 " + c2)
            return c2


def find_split_no(apply_no):
    test_b = EasyRequest(user='80663835', application="ordercenter-view", env="test")
    payload2 = '{"page": 1, "size": 200, "menuType": 1, "applyOrderNos": ["Z109130099"]}'
    payload2 = json.loads(payload2)
    payload2['applyOrderNos'] = [apply_no]
    payload2 = json.dumps(payload2)
    a = test_b.start(rid=10, payload=payload2)
    b = json.loads(a)
    if not b['page']['result']:
        # print("没找到 待会再来")
        return 0
    else:
        if b['page']['result'][0]['splitOrderNo'] == "":
            # print("还没拆单完成")
            return 0
        else:
            c2 = b['page']['result'][0]['splitOrderNo']
            print("拆单号为 " + c2)
            return c2
