from typing import Any
import yaml
import logging

_logger = logging.getLogger(__name__)

class RequestData:
    
    def __init__(self, url: str, params: dict, rq_body: dict, headers: dict) -> None:
        self.url = url
        self.params = params
        self.rq_body = rq_body
        self.header = headers
        
class Parser:
    
    def __call__(self, filename: str, *args: Any, **kwds: Any) -> RequestData:
        _logger.info("parsing yaml file")
        with open(filename, mode='rb') as file:
            rs = yaml.safe_load(file)
        
        return RequestData(
            url= 
        )