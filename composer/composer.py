from typing import Any
import yaml
import logging

from pytest_bdd import scenarios, given, when, then

_logger = logging.getLogger(__name__)

class RequestData:
    
    def __init__(self, url: str, method, params: dict, rq_body: dict = {}, headers: dict = {}) -> None:
        self.url = url
        self.params = params
        self.rq_body = rq_body
        self.headers = headers
        self.method = method
        
        
class TestCaseComposer:
    
    def __init__(self, filename: str):
        
        self.arrangements = []
        self.actions = []
        self.assertions = []

        _logger.info("parsing yaml file")
        with open(filename, mode='rb') as file:
            rs = yaml.safe_load(file)
        
        self.raw_data = rs
        
        self.test_name = rs.get("name")
        
        self._load_arrangements()
        self._load_actions()
        self._load_assertions()
        
    def _load_arrangements(self):
        # get arranging calls
        api_calls = self.raw_data.get("given")
        
        if not api_calls:
            _logger.warn("no arranging call found")
            
        for call in api_calls:
            self.arrangements.append(RequestData(
                url=call.get("url"),
                params=call.get("params"),
                rq_body=call.get("body"),
                headers=call.get("headers"),
                method=call.get("http-method")
            ))
            
    def _load_actions(self):
        # get assertions call
        actions = self.raw_data.get("when")
        
        if not actions:
            _logger.warn("no action call found") 
                    
        for action in actions:
            self.actions.append(RequestData(
                url=action.get("url"),
                params=action.get("params"),
                rq_body=action.get("body"),
                headers=action.get("headers"),
                method=action.get("http-method")
            ))
            
    def _load_assertions(self):
        assertions = self.raw_data.get("then")
        self.assertions = assertions
    
    def get_arrange_calls(self):
        return self.arrangements

    def get_name(self):
        return self.test_name
    
    def get_action_calls(self):
        return self.actions

    def get_status_codes(self):
        return self.assertions.get("status-code")
    
