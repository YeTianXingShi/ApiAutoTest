import json


class ZhenPayload:

    def __init__(self):
        self.payload = {}

    def add_payload(self, key, value):
        self.payload[key] = value

    def get_payload(self):
        if isinstance(self.payload, dict):
            payload = json.dumps(self.payload)
            return payload
        elif isinstance(self.payload, str):
            return "error"

    def file_payload(self):
        pass
