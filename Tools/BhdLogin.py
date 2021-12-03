import json

from Request.ZhenGeneral import ZhenGeneral
from Request.ZhenHeaders import ZhenHeaders
from Request.ZhenPayload import ZhenPayload
from Request.ZhenRequest import ZhenRequest


class BhdLogin:
    def __init__(self, domain, usernames, password):
        self.domain = domain
        self.usernames = usernames
        self.password = password

    def login(self):
        login_general = ZhenGeneral(self.domain, "/yhdos/usercenter/login", "POST")

        login_headers = ZhenHeaders()
        # 添加波鸿达标记
        login_headers.add_header("X-YH-TenantCode", "BHD")

        login_payload = ZhenPayload()
        login_payload.add_payload('username', self.usernames)
        login_payload.add_payload('password', self.password)

        login_requests = ZhenRequest(login_general.get_burl(), login_general.get_method(), login_headers.headers,
                                     login_payload.get_payload())
        login_response = login_requests.start_requests()
        code = json.loads(login_response)['result']['code']
        access_token = json.loads(login_response)['result']['accessToken']

        # code转token
        url = self.domain + "//yhdos/usercenter/getMultiToken?code=" + code

        code_header = ZhenHeaders()
        code_header.add_header("accessToken", access_token)
        code_header.add_header("X-YH-TenantCode", "BHD")

        code_requests = ZhenRequest(burl=url, method="GET", headers=code_header.headers,
                                    payload="")
        code_response = code_requests.start_requests()

        login_token = json.loads(code_response)['result']['login-token']

        # 门店选择
        shop_payload = ZhenPayload()
        shop_payload.add_payload("shopId", "A035")

        url2 = self.domain + "/yhdos/usercenter/changeCurrentShop"

        shop_requests = ZhenRequest(burl=url2, method="POST", headers=code_header.headers,
                                    payload=shop_payload.get_payload())
        shop_requests.start_requests()

        return login_token


# test
test = BhdLogin(domain="http://cp-cdtmdz-dev.yhdos.devapis.yonghui.cn", usernames="18628343316", password="Ur96Cdvnf3")
print(test.login())
