class ZhenHeaders:

    def __init__(self):
        self.headers = {}
        self.add_header('Accept', "application/json, text/plain, */*")
        self.add_header('Content-Type', "application/json;charset=UTF-8")

    def add_header(self, key, value):
        self.headers[key] = value

    def del_header(self, key):
        del self.headers[key]
