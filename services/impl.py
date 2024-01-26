from typing import Any
import yaml
import logging

from pytest_bdd import scenarios, given, when, then

_logger = logging.getLogger(__name__)

class RequestData:
    
    def __init__(self) -> None:
        self.url = ""
        self.params = dict()
        self.rq_body = dict()
        self.headers = dict()
        self.method = "GET"
        
    def set_url(self, url):
        self.url = url
        
    def set_params(self, params):
        self.params = params
        
    def set_method(self, method):
        self.method = method
        
    def set_headers(self, headers):
        self.headers = headers
        
    def set_rq_body(self, rq_body):
        self.rq_body = rq_body
