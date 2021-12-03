from Request.ZhenGeneral import ZhenGeneral
from Request.ZhenPayload import ZhenPayload
from Request.ZhenRequest import ZhenRequest


class AveragePrice:
    def __init__(self, domain):
        self.domain = domain

    def search(self, product, shop):
        search_general = ZhenGeneral(self.domain, "/open/api/searchAveragePrice/locationCode/productCode", "POST")
        search_payload = ZhenPayload()
        search_payload.add_payload('productCode', product)
        search_payload.add_payload('shopCode', shop)
        search_requests = ZhenRequest(search_general.get_burl(), search_general.get_method(), search_general.headers,
                                      search_payload.get_payload())
