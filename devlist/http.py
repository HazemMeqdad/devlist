from __future__ import annotations
from requests import request


BASE = "https://devlist.dev/api"


class Payload(dict):
    ...


class Rout(object):
    def __init__(self, method: str, rout: str, *args, **kwargs) -> None:
        self.method = method
        self.rout = rout
        self.args = args
        self.kwargs = kwargs
    
    def request(self) -> Payload | bool:
        re = request(
            method=self.method,
            url=f"{BASE}{self.rout}",
            *self.args,
            **self.kwargs
        )
        if isinstance(re.json(), bool):
            return re.json()
        return Payload(re.json())



