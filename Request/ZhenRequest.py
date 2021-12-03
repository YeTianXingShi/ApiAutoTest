import requests


class ZhenRequest:
    def __init__(self, burl, method, headers, payload):
        self.burl = burl
        self.method = method
        self.headers = headers
        self.payload = payload

    @staticmethod
    def _post_z(self):
        r = requests.post(self.burl, headers=self.headers, data=self.payload.encode('utf-8'))
        return r.text

    @staticmethod
    def _file_z(self):
        self.payload = {'file': (open(file=self.payload, mode='rb'))}
        r = requests.post(self.burl, headers=self.headers, files=self.payload)
        return r.text

    @staticmethod
    def _delete_z(self):
        r = requests.delete(self.burl, headers=self.headers)
        return r.text

    @staticmethod
    def _put_z(self):
        r = requests.put(self.burl, headers=self.headers, data=self.payload)
        return r.text

    @staticmethod
    def _get_z(self):
        r = requests.get(self.burl, headers=self.headers, params=self.payload)
        return r.text

    def start_requests(self):
        if self.method == "POST":
            return self._post_z(self)
        elif self.method == "Files":
            return self._file_z(self)
        elif self.method == "DELETE":
            return self._delete_z(self)
        elif self.method == "PUT":
            return self._put_z(self)
        elif self.method == "GET":
            return self._get_z(self)
        else:
            print("请求方式没被支持")
            return 0
