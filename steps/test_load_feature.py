import logging
import os
import re

from pytest_bdd import scenarios, given, when, then, parsers
import pytest


import services
import flagging
import caller

_logger = logging.getLogger(__name__)


def walk_get_path(path):
    feature_files = []
    feature_file_pattern = re.compile(r'.*\.feature$', re.IGNORECASE)
    
    def Walk(dir):
        for root, dirs, file_names in os.walk(dir):
            for file in file_names:
                if re.match(feature_file_pattern, file):
                    feature_files.append(os.path.join(root, file))
            for d in dirs:
                Walk(os.path.join(root, d))
    
    _logger.info("getting all feature files")
    Walk(path)
    _logger.info("load files done")

    return feature_files


for file_path in walk_get_path(flagging.args.data):
    scenarios(file_path)


# scenarios("./features/test.feature")

class Context:
    def __init__(self) -> None:
        self.variable = {}


@pytest.fixture
def context():
    return Context()

@given("I do nothing")
def do_noting():
    _logger.info("do no setup")
    
@given(parsers.parse("I create an API {request_method:w} request"))
def set_up_api_request(context, request_method):
    req_data = services.RequestData()
    req_data.set_method(request_method)
    context.variables = {}
    context.variable["rq_data"] = req_data
    
@given(parsers.parse("the endpoint is '{endpoint}'"))
def set_up_endpoint(context, endpoint):
    req_data = context.variable.get("rq_data")
    if not req_data:
        req_data = services.RequestData()
        
    req_data.set_url(flagging.args.host + endpoint)
    context.variable["rq_data"] = req_data
    
@given(parsers.parse("the headers are:"))
def set_up_headers(context):
    req_data = context.variable.get("rq_data")
    if not req_data:
        req_data = services.RequestData()
    
    headers_table = context.table
    
    headers = {}
    for row in headers_table:
        key = row["Key"]
        value = row["Value"]
        headers[key] = value
        
    req_data.set_headers(headers)
    context.variable["rq_data"] = req_data
    
@given(parsers.parse("the request params are"))
def set_up_params(context, ):
    req_data = context.variable.get("rq_data")
    if not req_data:
        req_data = services.RequestData()
        
    req_data.set_params(dict(context.table))
    context.variable["rq_data"] = req_data
    
@when(parsers.parse("I send request"))
def send_api_request(context):
    req_data = context.variable.get("rq_data")
    if not req_data:
        req_data = services.RequestData()
    
    c = caller.Caller(req_data)
    rspn = c()
    
    context.variable["api_response"] = rspn

@then(parsers.parse("The status code should be {status_code:d}"))
def assert_status_code(context, status_code):
    assert context.variable.get("api_response").status_code == status_code