

from Request.ZhenRequest import ZhenRequest
from Request.ZhenPayload import ZhenPayload
from Request.ZhenGeneral import ZhenGeneral
from Request.ZhenHeaders import ZhenHeaders
from Tools.RmeLogin import RmeLogin
from Easy.EasyRequest import EasyRequest

domain1 = "http://sit.order-plan-view.sitapis.yonghui.cn"
domain2 = "http://sit.usercenter.sitapis.yonghui.cn"

a_general = ZhenGeneral(domain1, "/orderPlan/queryOrderPlanList", "POST")
a_login = RmeLogin(domain2, "80663835", "Cc123456")
a_headers = ZhenHeaders()
a_payload = ZhenPayload()

a_headers.add_header('login-token', a_login.login())

a_payload.add_payload('page', "1")
a_payload.add_payload('size', "10")
a_payload.add_payload('applyStatus', ["0"])
a_payload.add_payload('tabLabel', "5")
#
# a_requests = ZhenRequest(a_general.get_burl(), a_general.get_method(), a_headers.headers, a_payload.get_payload())
# c = a_requests.start_requests()
# print(c)


url = 'http://sit.order-fresh.sitapis.yonghui.cn/fresh/shoppingcart/pc/upload?normalBusiness=0'
url2 = 'http://httpbin.org/post'
url3 = 'http://sit.order-fresh.sitapis.yonghui.cn/fresh/dis_order/upload'
# files = {'file': open('Files/test.xlsx', 'rb')}
files = {'file': ('test.xls', open('Files/test.xlsx', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
files2 = {'file': ('test2.xls', open('Files/test2.xlsx', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

# a_headers.del_header('Content-Type')
# b_requests = ZhenRequest(url3, "Files", a_headers.headers, files2).start_requests()
# print(b_requests)

payload = '{"page": "1", "size": "10", "applyStatus": ["0"], "tabLabel": "5"}'
d = EasyRequest(env="test", app="order-plan-view", usernames="80663835", password="Cc123456")
d.start(method="POST", url="/orderPlan/queryOrderPlanList", payload=payload)

