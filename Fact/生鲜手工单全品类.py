import json
from time import sleep

from Easy.EasyRequest import EasyRequest
from Tools.ExcelUpdate import excel_update
from Tools.TimeNow import get_date
from Tools.TimeNow import get_time

test_a = EasyRequest(user='80663835', application="order-fresh", env="test")
excel_normal = '../Files/手工单正常.xlsx'


# 导入
def fresh_additional_import(request, file):
    a = request.start(rid=7, payload=file)
    b = json.loads(a)
    if b['response']['errorCount'] != "0":
        print("导入失败，请检查导入数据")
        print(b['response']['filePath'])
        exit(400)
    return a


# 清空列表
def fresh_additional_del_all(request):
    # url = "/fresh/dis_order/delAll?lastSelectTime=" + get_date()
    a = request.start(rid=8)
    return a


# 生成订单
# 注意时间
def fresh_additional_audit(request):
    sleep(10)
    payload = """{"ignorePrice": true, "voucherDate": 1631836800000, "lastSelectTime": "2021-10-11 23:50:58", 
               "modifyArrivalDate": false}"""
    payload = json.loads(payload)
    payload['lastSelectTime'] = get_date()
    payload['voucherDate'] = get_time() * 1000
    payload = json.dumps(payload)
    a = request.start(rid=9, payload=payload)
    b = json.loads(a)
    num = b['response']['resultData']
    print("申请单号为 " + num)
    return num


# excel 修改商品编码
def update_product(file, product1, product2):
    excel_update(file=file, key='A2', value=product1)
    excel_update(file=file, key='A3', value=product2)


# excel 修改门店
def update_shop(file, shop):
    excel_update(file=file, key='F2', value=shop)
    excel_update(file=file, key='F3', value=shop)


def update_addtype(file, addtype):
    excel_update(file=file, key='M2', value=addtype)
    excel_update(file=file, key='M3', value=addtype)


# 手工单导入到拆单流程 返回拆单号
def fresh_additional(file, product1, product2, shop, request, order_type, addtype=""):
    # 清空列表
    # fresh_additional_del_all(request)

    # 修改商品
    update_product(file, product1, product2)

    # 修改门店
    update_shop(file, shop)

    # 出单方式修改
    update_addtype(file, addtype)

    # 导入模板
    fresh_additional_import(request=request, file=file)

    # # 生成订单
    # order_no = fresh_additional_audit(request)
    #
    # # 获取拆单号
    # c = 0
    # while c == 0:
    #     sleep(10)
    #     if order_type == "fresh":
    #         print("生鲜订单明细跟踪(新)查询")
    #         c = find_split_no_fresh(order_no)
    #     else:
    #         print("订单明细跟踪(新)查询")
    #         c = find_split_no(order_no)
    # return


# fresh_additional(file=excel_normal, product1="812711", product2="812712", shop="9010", request=test_a)

# 直送 生鲜 食百 加工
product01 = [["812503", "812504"], ["810850", "810851"], ["812388", "812389"]]

# 配送 生鲜 食百 加工
product02 = [["812774", "812775"], ["811680", "811681"], ["813473", "813474"]]

# 货到即配 生鲜 食百 加工
product03 = [["812764", "812765"], ["811487", "811488"], ["813463", "813464"]]

shop_code = "9010"
dc_code = ["W001", "W003"]

# fresh_additional(file=excel_normal, product1=product02[2][0], product2=product02[2][1], shop=shop_code,
#                  request=test_a, order_type="shibai", addtype="库存加配")

# 门店
fresh_additional(file=excel_normal, product1=product01[0][0], product2=product01[0][1], shop=dc_code[1],
                 request=test_a, order_type="fresh", addtype="直送")
fresh_additional(file=excel_normal, product1=product01[1][0], product2=product01[1][1], shop=dc_code[0],
                 request=test_a, order_type="shibai", addtype="直送")
fresh_additional(file=excel_normal, product1=product01[2][0], product2=product01[2][1], shop=dc_code[0],
                 request=test_a, order_type="shibai", addtype="直送")

fresh_additional(file=excel_normal, product1=product02[0][0], product2=product02[0][1], shop=shop_code,
                 request=test_a, order_type="fresh", addtype="库存加配")
fresh_additional(file=excel_normal, product1=product02[1][0], product2=product02[1][1], shop=shop_code,
                 request=test_a, order_type="shibai", addtype="库存加配")
fresh_additional(file=excel_normal, product1=product02[2][0], product2=product02[2][1], shop=shop_code,
                 request=test_a, order_type="shibai", addtype="库存加配")

fresh_additional(file=excel_normal, product1=product03[0][0], product2=product03[0][1], shop=shop_code,
                 request=test_a, order_type="fresh", addtype="货到即配")
fresh_additional(file=excel_normal, product1=product03[1][0], product2=product03[1][1], shop=shop_code,
                 request=test_a, order_type="shibai", addtype="货到即配")
fresh_additional(file=excel_normal, product1=product03[2][0], product2=product03[2][1], shop=shop_code,
                 request=test_a, order_type="shibai", addtype="货到即配")

# 申请单类型查询
# SELECT x.order_type FROM yh_srm_odercenter_fresh_test.fresh_split_order_mid x where verification_id ="E1J1400013";


# dc选择 出单方式选择 商品大类选择
# def fresh_additional_start(dc_choose):
#     if dc_choose == "DC":
#         pass
#     elif dc_choose == "Shop":
#         pass

# 手工单导入

# 11部类导入 直送 库存加配 货到即配
# 食品部类导入 直送 库存加配 货到即配
# 加工部类导入

# 配送中心类型组合 02 04 通过修改渠道中心数据库实现
# 地点组合门店和DC

# 商品数据
# 生鲜 直送 812503
# 812504
# 812505
# 812506

# 生鲜 库存加配
# 生鲜 货到即配

# 食百 直送 810850
# 810851
# 810852
# 810853


# 食百 库存加配 04
# 食百 货到即配 04

# 加工 直送 812388
# 812389
# 812390
# 812391

# 加工 库存加配 04
# 加工 货到即配 04

# 以上商品分别从DC和门店下单
# DC为W001 和 W003
# 门店为9010

# 区分分配表和一般模板
# 拆单
