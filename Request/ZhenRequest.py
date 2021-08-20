import requests


class ZhenRequest:
    def __init__(self, burl, method, headers, payload):
        self.burl = burl
        self.method = method
        self.headers = headers
        self.payload = payload

    @staticmethod
    def _post_z(self):
        r = requests.post(self.burl, headers=self.headers, data=self.payload)
        return r.text

    @staticmethod
    def _file_z(self):
        r = requests.post(self.burl, headers=self.headers, files=self.payload)
        return r.text

    def start_requests(self):
        if self.method == "POST":
            return self._post_z(self)
        elif self.method == "Files":
            return self._file_z(self)
        else:
            return 0
