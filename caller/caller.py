from typing import Any
from composer import RequestData
import requests

class Caller:
    
    def __init__(self, comp: RequestData) -> None:
        self.request_kwargs = {
            "url": comp.url,
            "json": comp.rq_body,
            "headers": comp.headers,
            "params": comp.params
        }
        self.http_method = comp.method
        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        match str(self.http_method).upper():
            case "POST":
                return self.post()
                
            case "GET":
                return self.get()
            
            case "PUT":
                return self.put()
            
            case "DELETE":
                return self.delete()
        
    def get(self):
        return requests.get(**self.request_kwargs)
    
    def post(self):
        return requests.post(**self.request_kwargs)
    
    def put(self):
        return requests.put(**self.request_kwargs)
    
    def delete(self):
        return requests.delete(**self.request_kwargs)
    
    