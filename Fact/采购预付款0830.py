import json

from Easy.EasyRequest import EasyRequest

# 本次测试需要的场景有
# 1、标签是否自动传SAP制单
# 2、标签是否需要自动票核
# 3、是否申请预付款不抵扣 是 and 否
# 4、供应商应付账款取值
# 5、供应商未核销预付款金额取值
# 6、付款单位与采购组织的联动
# 7、入库单号导入检验
# 8、自动票核自动制单场景的的采购买手节点入库单场景


# 数据配置情况
# 标签01为 自动制单 自动票核
# 标签02为 非自动制单 自动票核
# 标签03为 非自动制单 非自动票核
# 标签08为 自动制单 非自动票核


# http://glzx-sup-dev.yh-glzx-finance-center.devgw.yonghui.cn/swagger-ui.html#/
#

# 预付款申请单参数
payload1 = json.loads('{"tagCode":"01","tagName":"云超平台","bankAccount":"13900101040013333",'
                      '"depositBank":"中国农业银行南平市分行营业部","paymentUnit":"2104","projectName":"te","currencyUnit":"CNY",'
                      '"dateOfDemand":"2021-08-21","supplierCode":"S00192","supplierName":"福建长富乳品有限公司",'
                      '"firstTempSave":1,"operationFlag":2,"paymentAmount":"12","paymentMethod":"1",'
                      '"purchaseGroup":"U03 烘焙课","attachmentsVOs":[],"paymentPurpose":"te",'
                      '"fullNameOfPayee":"福建长富乳品有限公司","inventoryAmount":"31","paymentUnitName":"福建永辉文化传媒有限公司",'
                      '"saleOfInventory":"23","purchaseOrgCodes":"P002","purchaseOrgNames":"永辉福建大区采购组织",'
                      '"estimateDigestDays":"31","purchaseGroupCodes":"U03","purchaseGroupNames":"烘焙课",'
                      '"expectedDateOfArrival":"2021-08-27","supplierPaymentAmount":"116765.50",'
                      '"unWrittenPaymentAmount":"82940","isApplyPaymentNotDeductible":"0"}')

print(payload1['tagCode'])


class PrePaymentProcess:
    def __init__(self, payload):
        self.payload = payload

    def change_value(self, parameter_key, parameter_value):
        self.payload[parameter_key] = parameter_value
        print("成功修改 " + str(parameter_key) + " 的值为 " + str(parameter_value))

    # 修改标签
    def change_tag(self, tag):
        self.change_value(parameter_key='tagCode', parameter_value=tag)

        # 获取标签名
        if tag == '01':
            name = "云超平台"
        elif tag == '02':
            name = '云超战区'
        elif tag == '03':
            name = '云超PB'
        elif tag == '08':
            name = '1233'
        else:
            name = '后续完善'

        self.change_value(parameter_key='tagName', parameter_value=name)
        return 1

    # 修改供应商
    def change_supplier(self, supplier):
        self.change_value(parameter_key='supplierCode', parameter_value=supplier)
        self.change_value(parameter_key='supplierName', parameter_value='后续完善')

    # 修改付款单位
    def change_payment_unit(self, payment_unit):
        self.change_value(parameter_key='paymentUnit', parameter_value=payment_unit)

    # 修改付款金额
    def change_payment_amount(self, payment_amount):
        self.change_value(parameter_key='paymentAmount', parameter_value=payment_amount)

    # 获取修改完成后的payload
    def get_payload(self):

        # 处理带出值场景
        test_b = EasyRequest(user='80663835', application="order-plan-view", env="test")
        # 此处供应商需要自动
        press = test_b.start(url='/orderPlan/queryVenderUnPayedAmount', method='POST',
                             payload='{"supplierCode": "S00192"}')
        print(self.payload['supplierCode'])
        press = json.loads(press)

        press['result']['unWrittenPaymentAmount'] = "1000000000"

        # 临时
        self.change_value(parameter_key='supplierPaymentAmount',
                          parameter_value=500)
        # self.change_value(parameter_key='supplierPaymentAmount',
        #                   parameter_value=press['result']['supplierPaymentAmount'])
        self.change_value(parameter_key='unWrittenPaymentAmount',
                          parameter_value=press['result']['unWrittenPaymentAmount'])
        return json.dumps(self.payload)


PrePaymentProcess = PrePaymentProcess(payload=payload1)
PrePaymentProcess.change_tag('02')
PrePaymentProcess.change_supplier('S00192')
PrePaymentProcess.change_payment_unit('2104')
PrePaymentProcess.change_payment_amount('10000001')
payload = PrePaymentProcess.get_payload()

# 请求发起
test_a = EasyRequest(user='80663835', application="order-plan-view", env="test")
# test_a.start(rid=1)
test_a.start(rid=2, payload=payload)
# test_a.start(rid=3)
# res = test_a.start(url='/orderPlan/queryVenderUnPayedAmount', method='POST', payload='{"supplierCode": "S00192"}')
# res = json.loads(res)
# print(res['result']['supplierPaymentAmount'])

# print(res['result']['unWrittenPaymentAmount'])
