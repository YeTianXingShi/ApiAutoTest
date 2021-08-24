from DBcore.DbConfig import DbConfig
from Request.ZhenGeneral import ZhenGeneral
from Request.ZhenHeaders import ZhenHeaders
from Request.ZhenPayload import ZhenPayload
from Request.ZhenRequest import ZhenRequest
from Tools.RmeLogin import RmeLogin


# 创建requests请求信息 此处初始化域名和用户的token信息  域名信息区分环境和应用
# 发起请求 请求时需要的数据为 接口url 请求参数 额外的header信息(选填) 请求方式


class EasyRequest:
    # 需要的字段 环境 url method payload name password
    def __init__(self, user, application, env):
        self.application = application

        # 数据库连接
        con = DbConfig().get_connect()
        cursor = con.cursor()

        # 查询用户登录数据
        sql_uer = "SELECT x.* FROM yh_test_tool.aat_users x WHERE user_names =%s"
        cursor.execute(sql_uer, user)
        result = cursor.fetchone()
        db_password = result['password']

        # 关闭数据库链接
        con.close()

        self.domain = {}
        if env == "test":
            # todo 改成数据库配置
            self.domain['order-plan-view'] = "http://sit.order-plan-view.sitapis.yonghui.cn"
            self.domain['user-center'] = "http://sit.usercenter.sitapis.yonghui.cn"

        # 登录
        easy_login = RmeLogin(domain=self.domain['user-center'], usernames=user, password=db_password)
        token = easy_login.login()

        # token放入headers
        self.easy_headers = ZhenHeaders()
        self.easy_headers.add_header('login-token', token)

    def start(self, rid, payload=''):
        # 数据库连接
        con = DbConfig().get_connect()
        cursor = con.cursor()

        # 查询请求相关数据
        sql_request = "SELECT * FROM yh_test_tool.aat_requests WHERE id = %s"
        cursor.execute(sql_request, rid)
        result = cursor.fetchone()
        db_url = result['url']
        db_payload = result['payload']
        db_headers = result['headers']
        db_remark = result['remark']
        db_method = result['method']

        # 关闭数据库链接
        con.close()

        # 请求信息初始化
        easy_general = ZhenGeneral(domain=self.domain[self.application], url=db_url, method=db_method)

        # todo payload拓展
        # 请求参数封装
        easy_payload = ZhenPayload()

        # todo header信息拓展

        if payload == '':
            # 发送请求
            easy_request = ZhenRequest(burl=easy_general.get_burl(), method=easy_general.get_method(),
                                       headers=self.easy_headers.headers,
                                       payload=db_payload)
            print("参数来自数据库")
        else:
            easy_request = ZhenRequest(burl=easy_general.get_burl(), method=easy_general.get_method(),
                                       headers=self.easy_headers.headers,
                                       payload=payload)
            print("参数来自带调用入参")

        response = easy_request.start_requests()

        # 返回请求结果
        print(response)
        return response
