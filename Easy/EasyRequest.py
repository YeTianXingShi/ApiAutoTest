from Request.ZhenRequest import ZhenRequest
from Request.ZhenPayload import ZhenPayload
from Request.ZhenGeneral import ZhenGeneral
from Request.ZhenHeaders import ZhenHeaders
from Tools.RmeLogin import RmeLogin


class EasyRequest:
    # 需要的字段 环境 url method payload name password
    def __init__(self, env, app,  usernames, password):
        self.domain = {}
        if env == "test":
            self.domain['order-plan-view'] = "http://sit.order-plan-view.sitapis.yonghui.cn"
            self.domain['user-center'] = "http://sit.usercenter.sitapis.yonghui.cn"

        # 登录
        easy_login = RmeLogin(self.domain['user-center'], usernames, password)
        token = easy_login.login()

        # token放入headers
        easy_headers = ZhenHeaders()
        easy_headers.add_header('login-token', token)
        self.headers = easy_headers.headers

    def start(self, method, url, payload):
        # 请求信息初始化
        easy_general = ZhenGeneral(domain=self.domain["order-plan-view"], url=url, method=method)

        # 请求参数封装
        # easy_payload = ZhenPayload()

        # 发送请求
        easy_request = ZhenRequest(burl=easy_general.get_burl(), method=easy_general.get_method(), headers=self.headers,
                                   payload=payload)
        response = easy_request.start_requests()

        # 返回请求结果
        print(response)
        return response
