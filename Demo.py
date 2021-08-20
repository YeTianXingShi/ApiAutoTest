import requests


class HttpRequest:
    """HTTP请求基本类"""
    url_domain = ""
    url_body = ""
    http_body = ""

    def __init__(self, url_domain, url_body, http_body):
        self.url_domain = url_domain
        self.url_body = url_body
        self.http_body = http_body

    @staticmethod
    def http_get(url_body):
        r = requests.get(url_body)
        return r.text

    @staticmethod
    def http_put(url_body, http_body):
        r = requests.put(url_body, http_body)
        return r.text

    @staticmethod
    def http_post(url_body, http_header, http_body):
        # headers = {'login-token': 'rme99fa7afa49e24227b55a8699b518b7b0'}
        r = requests.post(url_body, headers=http_header, data=http_body)
        return r.text
        # return 1


# t = HttpRequest("", "http://sit.order-plan-view.sitapis.yonghui.cn/orderPlan/queryOrderPlanList",
#                 '{"page":1,"size":10,"applyStatus":["0"],"tabLabel":2}')
# a = t.http_post(t.url_body,
#                 {'login-token': 'rme1907e37a28ea403b966838538e487bb6',
#                  'Accept': 'application/json, text/plain, */*',
#                  'Content-Type': 'application/json;charset=UTF-8'},
#                 t.http_body)
# print(a)
