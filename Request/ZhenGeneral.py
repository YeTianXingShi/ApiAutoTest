class ZhenGeneral:
    def __init__(self, domain, url, method):
        self.domain = domain
        self.url = url
        self.method = method

    def get_burl(self):
        burl = self.domain + self.url
        return burl

    def get_method(self):
        method = self.method
        return method
