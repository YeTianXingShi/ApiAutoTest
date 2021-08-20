import hashlib
import json

from Request.ZhenGeneral import ZhenGeneral
from Request.ZhenHeaders import ZhenHeaders
from Request.ZhenPayload import ZhenPayload
from Request.ZhenRequest import ZhenRequest


class RmeLogin:
    def __init__(self, domain, usernames, password):
        self.domain = domain
        self.usernames = usernames
        hash_md5 = hashlib.md5()
        hash_md5.update(password.encode(encoding='utf-8'))
        self.password = hash_md5.hexdigest()

    def login(self):
        login_general = ZhenGeneral(self.domain, "/login", "POST")

        login_headers = ZhenHeaders()

        login_payload = ZhenPayload()
        login_payload.add_payload('loginName', self.usernames)
        login_payload.add_payload('loginPassword', self.password)
        login_payload.add_payload('loginType', 0)

        login_requests = ZhenRequest(login_general.get_burl(), login_general.get_method(), login_headers.headers,
                                     login_payload.get_payload())
        login_response = login_requests.start_requests()
        login_token = json.loads(login_response)['result']['loginToken']

        return login_token

