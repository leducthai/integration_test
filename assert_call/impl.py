from typing import Any
from caller import Caller

class StatusCodeAssertion:
    
    def __init__(self, api_calls: list[Caller], status: list[str] ) -> None:
        self.response_status = []
        self.status = status
        self._call_apis(api_calls=api_calls)
        
    def _call_apis(self, api_calls: list[Caller]):
        for api in api_calls:
            response = api()
            self.response_status.append(response.status_code)
            
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for i in range(len(self.status)):
            assert self.status[i] == self.response_status[i]